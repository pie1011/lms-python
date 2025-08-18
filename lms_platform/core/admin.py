from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile, Course, Module, Assignment, Enrollment, Submission
from django import forms

# Import the UserAdmin from Django's auth module to customize the User model admin
from django.contrib.auth.admin import UserAdmin

# For demo user admin restrictions
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


class LMSAdminSite(admin.AdminSite):
    """
    Custom admin site that provides real data counts for the dashboard
    """
    site_title = "LMS Platform Admin"
    site_header = "LMS Platform Administration"
    index_title = "Welcome to LMS Platform Admin"
    
    def index(self, request, extra_context=None):
        """
        Override the default admin index to provide real data counts
        """
        extra_context = extra_context or {}
        
        # Get real counts from the database
        extra_context.update({
            # User counts
            'total_users': User.objects.count(),
            'total_profiles': UserProfile.objects.count(),
            'students_count': UserProfile.objects.filter(role='student').count(),
            'instructors_count': UserProfile.objects.filter(role='instructor').count(),
            'admins_count': UserProfile.objects.filter(role='admin').count(),
            
            # Academic content counts
            'total_courses': Course.objects.count(),
            'total_modules': Module.objects.count(),
            'total_assignments': Assignment.objects.count(),
            
            # Activity counts
            'total_enrollments': Enrollment.objects.count(),
            'active_enrollments': Enrollment.objects.filter(status='active').count(),
            'total_submissions': Submission.objects.count(),
            'graded_submissions': Submission.objects.filter(status='graded').count(),
            'pending_submissions': Submission.objects.filter(status='submitted').count(),
            
            # Recent activity (last 7 days)
            'recent_enrollments': Enrollment.objects.filter(
                enrollment_date__gte=timezone.now() - timedelta(days=7)
            ).count(),
        })
        
        return super().index(request, extra_context)


# Create our custom admin site instance
admin_site = LMSAdminSite(name='lms_admin')


class CourseAdmin(admin.ModelAdmin):
    """ Custom admin for Course model to filter instructors """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "instructor":
            # Only show users who have instructor role
            instructor_profiles = UserProfile.objects.filter(role='instructor')
            instructor_users = [profile.user.id for profile in instructor_profiles]
            kwargs["queryset"] = User.objects.filter(id__in=instructor_users)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class EnrollmentAdmin(admin.ModelAdmin):
    """ Custom admin for Enrollment model to filter students """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            # Only show users who have student role
            student_profiles = UserProfile.objects.filter(role='student')
            student_users = [profile.user.id for profile in student_profiles]
            kwargs["queryset"] = User.objects.filter(id__in=student_users)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SubmissionAdmin(admin.ModelAdmin):
    """ Custom admin for Submission model to filter students """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            # Only show users who have student role
            student_profiles = UserProfile.objects.filter(role='student')
            student_users = [profile.user.id for profile in student_profiles]
            kwargs["queryset"] = User.objects.filter(id__in=student_users)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AssignmentAdminForm(forms.ModelForm):
    """ Custom form for Assignment model to handle specific field types and validation.
    This form allows for better control over how the fields are displayed in the admin interface.
    """
    class Meta:
        model = Assignment
        fields = '__all__'
        widgets = {
            'due_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Enter assignment description...'
                }
            ),
            'instructions': forms.Textarea(
                attrs={
                    'rows': 6,
                    'placeholder': 'Enter detailed instructions for students...'
                }
            ),
        }


class AssignmentAdmin(admin.ModelAdmin):
    form = AssignmentAdminForm
    list_display = ['assignment_name', 'module', 'due_date', 'max_points', 'assignment_type']
    list_filter = ['assignment_type', 'due_date', 'module__course']
    search_fields = ['assignment_name', 'description']


# Custom mixin to restrict demo user actions
class DemoUserMixin:
    """
    Mixin to allow demo users full visual access but prevent actual changes
    """
    
    def has_add_permission(self, request):
        # Always return True so Add buttons show up
        return True
    
    def has_change_permission(self, request, obj=None):
        # Always return True so Edit links show up
        return True
    
    def has_delete_permission(self, request, obj=None):
        # Always return True so Delete buttons show up
        return True
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        """Override form view to handle demo user submissions"""
        
        if request.user.username == 'PortfolioDemo' and request.method == 'POST':
            # Demo user submitted a form - show success message and redirect
            action = "updated" if object_id else "created"
            
            messages.success(
                request,
                f'🎭 Demo Mode: {self.model._meta.verbose_name} would have been {action} successfully! '
                f'The form validation and interface work perfectly, but no actual data was modified for this demonstration.'
            )
            
            # Redirect to changelist
            return HttpResponseRedirect(
                reverse(f'admin:{self.model._meta.app_label}_{self.model._meta.model_name}_changelist')
            )
        
        # For GET requests or normal users, show the form normally
        return super().changeform_view(request, object_id, form_url, extra_context)
    
# Mixin to handle demo user delete actions
class DemoUserMixin:
    """
    Mixin to allow demo users full visual access but prevent actual changes
    """
    
    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True
    
    def get_queryset(self, request):
        """Ensure we can override delete actions"""
        return super().get_queryset(request)
    
    def delete_view(self, request, object_id, extra_context=None):
        """Override delete view for demo users - both GET and POST"""
        
        if request.user.username == 'PortfolioDemo':
            # For demo user, show message and redirect (both GET and POST)
            messages.success(
                request,
                f'🎭 Demo Mode: {self.model._meta.verbose_name} would have been deleted successfully! '
                f'The delete process works perfectly, but no actual data was removed for this demonstration.'
            )
            
            return HttpResponseRedirect(
                reverse(f'admin:{self.model._meta.app_label}_{self.model._meta.model_name}_changelist')
            )
        
        return super().delete_view(request, object_id, extra_context)
    
    def delete_model(self, request, obj):
        """Prevent actual deletion for demo users"""
        if request.user.username == 'PortfolioDemo':
            return  # Don't delete anything
        super().delete_model(request, obj)
    
    def delete_queryset(self, request, queryset):
        """Prevent bulk deletion for demo users"""
        if request.user.username == 'PortfolioDemo':
            return  # Don't delete anything
        super().delete_queryset(request, queryset)

# Update existing admin classes to use the mixin

class CourseAdmin(DemoUserMixin, admin.ModelAdmin):
    """ Custom admin for Course model to filter instructors """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "instructor":
            # Only show users who have instructor role
            instructor_profiles = UserProfile.objects.filter(role='instructor')
            instructor_users = [profile.user.id for profile in instructor_profiles]
            kwargs["queryset"] = User.objects.filter(id__in=instructor_users)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class EnrollmentAdmin(DemoUserMixin, admin.ModelAdmin):
    """ Custom admin for Enrollment model to filter students """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            # Only show users who have student role
            student_profiles = UserProfile.objects.filter(role='student')
            student_users = [profile.user.id for profile in student_profiles]
            kwargs["queryset"] = User.objects.filter(id__in=student_users)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SubmissionAdmin(DemoUserMixin, admin.ModelAdmin):
    """ Custom admin for Submission model to filter students """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            # Only show users who have student role
            student_profiles = UserProfile.objects.filter(role='student')
            student_users = [profile.user.id for profile in student_profiles]
            kwargs["queryset"] = User.objects.filter(id__in=student_users)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AssignmentAdmin(DemoUserMixin, admin.ModelAdmin):
    form = AssignmentAdminForm
    list_display = ['assignment_name', 'module', 'due_date', 'max_points', 'assignment_type']
    list_filter = ['assignment_type', 'due_date', 'module__course']
    search_fields = ['assignment_name', 'description']


# Add mixin to other admin classes
class UserProfileAdmin(DemoUserMixin, admin.ModelAdmin):
    pass


class ModuleAdmin(DemoUserMixin, admin.ModelAdmin):
    pass



# Register models with both the default admin and our custom admin
# Default admin (keep existing functionality)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Submission, SubmissionAdmin)

# Custom admin with dashboard data AND demo user restrictions
admin_site.register(UserProfile, UserProfileAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(Module, ModuleAdmin)
admin_site.register(Assignment, AssignmentAdmin)
admin_site.register(Enrollment, EnrollmentAdmin)
admin_site.register(Submission, SubmissionAdmin)

# Register Django's built-in User model with demo restrictions
from django.contrib.auth.admin import UserAdmin

class DemoUserAdmin(DemoUserMixin, UserAdmin):
    pass

admin_site.register(User, DemoUserAdmin)
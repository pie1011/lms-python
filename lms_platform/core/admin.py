from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile, Course, Module, Assignment, Enrollment, Submission
from django import forms

# Import the UserAdmin from Django's auth module to customize the User model admin
from django.contrib.auth.admin import UserAdmin

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


# Register models with both the default admin and our custom admin
# Default admin (keep existing functionality)
admin.site.register(UserProfile)
admin.site.register(Course, CourseAdmin)
admin.site.register(Module)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Submission, SubmissionAdmin)

# Custom admin with dashboard data
admin_site.register(UserProfile)
admin_site.register(Course, CourseAdmin)
admin_site.register(Module)
admin_site.register(Assignment, AssignmentAdmin)
admin_site.register(Enrollment, EnrollmentAdmin)
admin_site.register(Submission, SubmissionAdmin)

# Register Django's built-in User model with our custom admin
admin_site.register(User, UserAdmin)


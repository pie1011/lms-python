from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, Course, Module, Assignment, Enrollment, Submission
from django import forms

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
    
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Course, CourseAdmin)
admin.site.register(Module)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)  # Use custom admin
admin.site.register(Submission, SubmissionAdmin)  # Use custom admin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, Course, Module, Assignment, Enrollment, Submission

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

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Course, CourseAdmin)
admin.site.register(Module)
admin.site.register(Assignment)
admin.site.register(Enrollment, EnrollmentAdmin)  # Use custom admin
admin.site.register(Submission, SubmissionAdmin)  # Use custom admin
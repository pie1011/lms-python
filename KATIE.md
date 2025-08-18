# KATIE.md

This file provides guidance when working with code in this repository.

## Project Overview

Django Learning Management System (LMS) called "lms_platform" - a portfolio project demonstrating full-stack Django development for education technology. Features user authentication, role-based permissions, complex database relationships, real-world business logic, and **multiple user portal interfaces**.

## Learning & Development Approach

**Preferred Communication Style:**
- **Tutorial-style learning experience** - treat this as an educational walkthrough
- **Step-by-step processes** - break complex tasks into manageable steps
- **One step at a time** - wait for confirmation before proceeding to next step
- **Decision-making collaboration** - ask about approach preferences (e.g., Option A vs Option B)
- **Hands-on learning** - focus on practical implementation over theory
- **Troubleshooting together** - debug issues systematically when they arise
- **Document after major features** - update README and KATIE.md after completing significant functionality

## Key Architecture

### Models (core/models.py)
- **UserProfile**: Extends Django User with roles (Student/Instructor/Admin)
- **Course**: Academic courses with instructor assignment
- **Module**: Organized course content with sequencing
- **Assignment**: Tasks with due dates and point values
- **Enrollment**: Student-course relationships with grade tracking
- **Submission**: Student work with grading capabilities

### Admin System (core/admin.py)
- **Custom Admin Site**: `LMSAdminSite` with real-time dashboard data
- **Demo User System**: `DemoUserMixin` allows portfolio viewing without data modification
- **Role-based Filtering**: Course/Enrollment/Submission admins filter by user roles
- **Password Management**: Superusers can change passwords; demo users cannot

### Student Portal System ✨ NEW! (core/views.py)
- **Student Authentication**: `student_login`, `student_dashboard`, `student_logout` views
- **Role-Based Access**: Only users with student role can access `/student/` portal
- **Real-Time Data**: Dashboard shows enrollments, assignments, submissions, grades
- **Template Inheritance**: `templates/student/base.html` with dedicated navigation

### Templates & Styling
- **Admin Templates**: `templates/admin/` with beautiful modern styling
- **Student Templates**: `templates/student/` with dedicated portal interface ✨ NEW!
- **CSS Architecture**: 
  - `static/css/admin-styles.css` - Admin interface design system
  - `static/css/student-styles.css` - Student portal styles ✨ NEW!
- **Form Styling**: Custom change_form.html with Django fieldset integration

## Development Commands

```bash
# Setup and run
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver

# Data management
python manage.py setup_production    # Creates sample data
python manage.py create_demo_user    # Creates demo users
python manage.py createsuperuser     # Create admin users
```

## Key Users & Access

- **SuperKatie**: Superuser account (full admin access)
- **PortfolioDemo**: Admin demo user (view-only, password: ViewOnly123)
- **student1**: Student demo user (student portal access, password: password123) ✨ NEW!
- **Admin Portal**: `/admin/` - Custom admin site with real-time data
- **Student Portal**: `/student/` - Dedicated student interface ✨ NEW!

## Current Status

✅ **Completed**: 
- Database models and relationships
- Beautiful custom admin interface with real-time dashboard
- **Student Portal with authentication and dashboard** ✨ NEW!
- **Student course overview and assignment tracking** ✨ NEW!
- Demo user system for portfolio presentation (both admin and student)
- Form styling with proper Django integration
- Role-based permissions and filtering
- **Organized CSS architecture with separate portal styles** ✨ NEW!

🚧 **Next**: Course detail views and assignment submission interface

## Technical Notes

- **Demo User Protection**: Uses `DemoUserMixin` to prevent data modification while showing full UI
- **Student Portal Security**: Role validation ensures only students access student portal
- **Multi-Portal Architecture**: Separate URL routing, templates, and CSS for admin vs student
- **Form Rendering**: Uses Django's `{% include "admin/includes/fieldset.html" %}` with custom CSS
- **Permission System**: Password changes blocked for demo users, enabled for superusers
- **Styling**: Custom CSS targets Django's form classes with organized external stylesheets

## Common Issues & Solutions

- **Dictionary Display**: Fixed by using Django's default form rendering instead of custom field access
- **Form Styling**: Apply styles to Django's CSS classes with `!important` to override defaults
- **Password Links**: Set `has_change_password_permission` context variable in admin views
- **Static Files**: Run `collectstatic` after CSS changes
- **Student Portal CSS**: Import `modern-lms.css` in `student-styles.css` for design consistency
- **Template Inheritance**: Use proper Django block structure for extending base templates
# KATIE.md

This file provides guidance when working with code in this repository.

## Project Overview

Django Learning Management System (LMS) called "lms_platform" - a portfolio project demonstrating full-stack Django development for education technology. Features user authentication, role-based permissions, complex database relationships, and real-world business logic.

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

### Templates & Styling
- **Custom Templates**: `templates/admin/` with beautiful modern styling
- **CSS Architecture**: `static/css/admin-styles.css` with design system
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
python manage.py create_demo_user    # Creates PortfolioDemo user
python manage.py createsuperuser     # Create admin users
```

## Key Users & Access

- **SuperKatie**: Superuser account (full admin access)
- **PortfolioDemo**: Demo user (view-only for portfolio, password: ViewOnly123)
- **Custom Admin URL**: `/admin/` uses custom admin site with real-time data

## Current Status

✅ **Completed**: 
- Database models and relationships
- Beautiful custom admin interface with real-time dashboard
- Demo user system for portfolio presentation
- Form styling with proper Django integration
- Role-based permissions and filtering

🚧 **Next**: Student portal development

## Technical Notes

- **Demo User Protection**: Uses `DemoUserMixin` to prevent data modification while showing full UI
- **Form Rendering**: Uses Django's `{% include "admin/includes/fieldset.html" %}` with custom CSS
- **Permission System**: Password changes blocked for demo users, enabled for superusers
- **Styling**: Custom CSS targets Django's form classes (.form-row, .module.aligned, etc.)

## Common Issues & Solutions

- **Dictionary Display**: Fixed by using Django's default form rendering instead of custom field access
- **Form Styling**: Apply styles to Django's CSS classes with `!important` to override defaults
- **Password Links**: Set `has_change_password_permission` context variable in admin views
- **Static Files**: Run `collectstatic` after CSS changes
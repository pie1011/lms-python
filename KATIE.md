# KATIE.md

This file provides guidance when working with code in this repository.

## Project Overview

Django Learning Management System (LMS) called "lms_platform" - a portfolio project demonstrating full-stack Django development for **HR Learning & Development**. Features corporate training management, role-based permissions, complex database relationships, and **multiple professional portal interfaces**.

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
- **UserProfile**: Extends Django User with roles (Employee/Trainer/HR Admin)
- **Course**: Corporate training programs (Safety, Compliance, Leadership, Tech Skills)
- **Module**: Organized training content with sequencing
- **Assignment**: HR assessments with due dates and point values (Knowledge Checks, Case Studies, Scenarios)
- **Enrollment**: Employee-training relationships with progress tracking
- **Submission**: Employee work with professional grading and feedback

### Admin System (core/admin.py)
- **Custom Admin Site**: `LMSAdminSite` with real-time dashboard data
- **Demo User System**: `DemoUserMixin` allows portfolio viewing without data modification
- **Role-based Filtering**: Course/Enrollment/Submission admins filter by user roles
- **Password Management**: Superusers can change passwords; demo users cannot

### Employee Portal System ✨ (core/views.py)
- **Employee Authentication**: `student_login`, `student_dashboard`, `student_logout` views
- **Role-Based Access**: Only users with student role can access `/student/` portal
- **Real-Time Data**: Dashboard shows training enrollments, assessments, submissions, scores
- **Corporate Training Focus**: HR-focused content and professional terminology

### Templates & Styling
- **Landing Page**: Professional navigation with Employee Portal and Staff Portal dropdown
- **Admin Templates**: `templates/admin/` with beautiful modern styling
- **Employee Templates**: `templates/student/` with corporate training interface
- **CSS Architecture**: 
  - `static/css/admin-styles.css` - HR admin interface design system
  - `static/css/student-styles.css` - Employee portal styles
- **Form Styling**: Custom change_form.html with Django fieldset integration

## Development Commands

```bash
# Setup and run
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver

# HR Training data management
python manage.py setup_production    # Creates corporate training data
python manage.py create_demo_user    # Creates demo users
python manage.py createsuperuser     # Create admin users
```

## Key Users & Access

- **SuperKatie**: Superuser account (full HR admin access)
- **PortfolioDemo**: Admin demo user (view-only, password: ViewOnly123)
- **demo_employee**: Employee demo user (training portal access, password: training123) ✨
- **HR Admin Portal**: `/admin/` - Custom admin site with real-time data
- **Employee Portal**: `/student/` - Dedicated employee training interface

## Current Status

✅ **Completed**: 
- Database models for HR Learning & Development
- Beautiful custom admin interface with real-time dashboard
- **Complete Employee Portal with corporate training focus** ✨
- **Professional landing page with dropdown navigation** ✨
- **Corporate training data (Safety, Compliance, Leadership, Tech Skills)** ✨
- **HR-focused assessments and realistic employee progress** ✨
- Demo user system for portfolio presentation (both admin and employee)
- Form styling with proper Django integration
- Role-based permissions and filtering
- **Organized CSS architecture with professional corporate styling** ✨

🚧 **Next**: Course detail views and assignment submission interface for employees

## Sample Corporate Training Data

### 🏢 **Training Programs:**
- **SAFE101** - Workplace Safety Fundamentals (Emergency Procedures, Hazard Identification)
- **COMP201** - Compliance and Ethics Training (Code of Conduct, Anti-Harassment)
- **LEAD301** - Leadership Development Program (Team Management, Decision Making)
- **TECH401** - Digital Skills for Modern Workplace (Cybersecurity, Productivity Tools)

### 📝 **Professional Assessments:**
- Emergency Response Knowledge Check
- Workplace Hazard Assessment
- Ethics Case Study Analysis
- Bystander Intervention Scenarios

### 👥 **Corporate Users:**
- **Demo Employee** (portfolio demonstration)
- **Sarah Martinez & David Chen** (Corporate Trainers)
- **Jennifer Brown** (HR Administrator)

## Technical Notes

- **Demo User Protection**: Uses `DemoUserMixin` to prevent data modification while showing full UI
- **Employee Portal Security**: Role validation ensures only employees access training portal
- **Multi-Portal Architecture**: Separate URL routing, templates, and CSS for admin vs employee
- **Corporate Focus**: Professional terminology, HR-focused content, workplace training scenarios
- **Form Rendering**: Uses Django's `{% include "admin/includes/fieldset.html" %}` with custom CSS
- **Permission System**: Password changes blocked for demo users, enabled for superusers
- **Styling**: Custom CSS targets Django's form classes with organized external stylesheets

## Common Issues & Solutions

- **Dictionary Display**: Fixed by using Django's default form rendering instead of custom field access
- **Form Styling**: Apply styles to Django's CSS classes with `!important` to override defaults
- **Password Links**: Set `has_change_password_permission` context variable in admin views
- **Static Files**: Run `collectstatic` after CSS changes
- **Employee Portal CSS**: Import `modern-lms.css` in `student-styles.css` for design consistency
- **Template Inheritance**: Use proper Django block structure for extending base templates
- **Corporate Data**: Use `setup_production` to create realistic HR training content
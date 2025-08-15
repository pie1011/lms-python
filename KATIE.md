# KATIE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django Learning Management System (LMS) called "lms_platform" - a portfolio project demonstrating full-stack Django development skills for education technology applications. The project showcases user authentication, role-based permissions, complex database relationships, file uploads, and real-world business logic.

## Database Schema

### Tables & Relationships

#### 1. Users & Authentication
```
Users (Django built-in)
├── id (primary key)
├── username
├── email
├── password
└── is_active

UserProfile
├── id (primary key)
├── user_id (foreign key → Users)
├── role (Student/Instructor/Admin)
├── first_name
├── last_name
├── phone_number
└── profile_picture
```

#### 2. Academic Structure
```
Courses
├── id (primary key)
├── course_code (e.g., "MATH101")
├── course_name (e.g., "Introduction to Mathematics")
├── description
├── credits
├── term (Spring 2024, Fall 2024, etc.)
├── instructor_id (foreign key → Users)
├── max_enrollment
├── created_at
└── updated_at

Modules
├── id (primary key)
├── course_id (foreign key → Courses)
├── module_name (e.g., "Module 1: Addition")
├── description
├── order_number (for sequencing)
├── content (lesson material)
├── created_at
└── updated_at

Assignments
├── id (primary key)
├── module_id (foreign key → Modules)
├── assignment_name (e.g., "Addition Homework")
├── description
├── due_date
├── max_points
├── assignment_type (Homework/Quiz/Exam/Project)
├── instructions
├── created_at
└── updated_at
```

#### 3. Student Progress & Grades
```
Enrollments (Student ↔ Course relationship)
├── id (primary key)
├── student_id (foreign key → Users)
├── course_id (foreign key → Courses)
├── enrollment_date
├── current_grade (calculated from submissions)
├── final_grade (locked at term end)
├── status (Active/Completed/Dropped)
└── gpa_points (for GPA calculation)

Submissions (Student work)
├── id (primary key)
├── student_id (foreign key → Users)
├── assignment_id (foreign key → Assignments)
├── submission_date
├── submission_content (text response)
├── file_upload (uploaded files)
├── grade (points received)
├── max_points (from assignment)
├── feedback (instructor comments)
├── graded_by (foreign key → Users)
├── graded_at
└── status (Submitted/Graded/Late)
```

### Key Relationships Summary

#### One-to-Many Relationships:
- **Course** → Many **Modules**
- **Module** → Many **Assignments**  
- **Assignment** → Many **Submissions**
- **User (Instructor)** → Many **Courses** (they teach)
- **User (Student)** → Many **Submissions**

#### Many-to-Many Relationships:
- **Students** ↔ **Courses** (via Enrollments table)

### Permission Levels by Role:

- **Admin:** Create/edit/delete Courses, Users, everything. View all system data and reports.
- **Instructor:** Create/edit Modules and Assignments for their courses. Grade submissions for their courses. View enrolled students and their progress.
- **Student:** View enrolled courses and modules. Submit assignments. View their own grades and feedback. Cannot see other students' grades.

## Development Progress

### Phase 1: Foundation
- [x] Project setup and Django configuration
- [x] Project renamed from hello_world to lms_platform
- [x] Database schema design and documentation
- [ ] Django models implementation
- [ ] Custom user model with roles
- [ ] Django admin interface customization

### Phase 2: Core Functionality
- [ ] User authentication & role-based permissions
- [ ] Course management (Admin/Instructor views)
- [ ] Module creation and content management
- [ ] Assignment creation and management
- [ ] Student enrollment system
- [ ] Assignment submission system
- [ ] Grading system

### Phase 3: User Interfaces
- [ ] Admin dashboard
- [ ] Instructor portal (course management, grading)
- [ ] Student portal (course view, submission interface)
- [ ] Role-based navigation and access control

### Phase 4: Enhanced Features
- [ ] File upload system for assignments
- [ ] Grade calculation and GPA tracking
- [ ] Email notifications
- [ ] Calendar view of due dates
- [ ] Responsive design

## Development Commands

### Setup and Dependencies
```bash
# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
# Start the development server
python manage.py runserver

# Collect static files (required before deployment)
python manage.py collectstatic
```

### Database Management
```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### Django Management
```bash
# Start a Django shell
python manage.py shell

# Run Django's built-in tests
python manage.py test
```

## Architecture

### Project Structure
- `lms_platform/` - Main Django project directory
  - `settings.py` - Django configuration with environment variable management
  - `urls.py` - Main URL routing
  - `models.py` - Database models (to be implemented)
  - `views.py` - Application views (to be implemented)
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, images)
- `manage.py` - Django management script
- `db.sqlite3` - SQLite database file (development)

### Key Configuration
- Uses `python-decouple` for environment variable management
- Configured for both development (SQLite) and production (PostgreSQL) databases
- Static files served with whitenoise for production deployment
- Environment variables for sensitive configuration

### Environment Variables
The application uses environment variables via `python-decouple`:
- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode toggle
- `DATABASE_URL` - Database connection string
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts

## Deployment Notes

- **Target Platform:** Render (free tier)
- **Database:** PostgreSQL in production, SQLite in development
- **Static Files:** Managed by whitenoise
- **Process:** Auto-deploy from GitHub main branch
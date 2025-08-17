# KATIE.md

This file provides guidance to when working with code in this repository.

## Project Overview

This is a Django Learning Management System (LMS) called "lms_platform" - a portfolio project demonstrating full-stack Django development skills for education technology applications. The project showcases user authentication, role-based permissions, complex database relationships, file uploads, and real-world business logic.

## Learning & Development Approach

**Preferred Communication Style:**
- **Tutorial-style learning experience** - treat this as an educational walkthrough
- **Step-by-step processes** - break complex tasks into manageable steps
- **One step at a time** - wait for confirmation before proceeding to next step
- **Decision-making collaboration** - ask about approach preferences (e.g., Option A vs Option B)
- **Hands-on learning** - focus on practical implementation over theory
- **Troubleshooting together** - debug issues systematically when they arise

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

### Phase 1: Foundation ✅ COMPLETED
- [x] Project setup and Django configuration
- [x] Project renamed from hello_world to lms_platform
- [x] Database schema design and documentation
- [x] Django models implementation (UserProfile, Course, Module, Assignment, Enrollment, Submission)
- [x] Custom user model with roles (Student, Instructor, Admin)
- [x] Django admin interface customization with role-based filtering
- [x] Production deployment to Render with PostgreSQL
- [x] Automated production data setup via Django management commands

### Phase 2: Core Functionality ✅ COMPLETED (Admin Interface)
- [x] Basic user management through Django admin
- [x] Course creation and instructor assignment (admin interface)
- [x] Module creation and content management (admin interface)
- [x] Assignment creation and management (admin interface)
- [x] Student enrollment system (admin interface)
- [x] Assignment submission system (admin interface)
- [x] Production superuser and sample data creation
- [x] **Beautiful admin dashboard with real functionality** ✨
- [x] **Styled admin list views with proper data display** ✨
- [x] **Clean template inheritance system** ✨
- [x] **Organized CSS architecture (no more inline styles)** ✨
- [ ] Grading workflow and grade calculation
- [ ] Frontend views for students and instructors
- [ ] User authentication & role-based permissions for frontend

### Phase 3: User Interfaces 🚧 IN PROGRESS
- [x] **Modern admin dashboard** - Complete with cards, stats, and quick actions
- [x] **Styled admin list views** - Beautiful tables with data, search, and pagination
- [ ] **Styled admin forms** - Currently working on add/edit forms
- [ ] Instructor portal (course management, grading)
- [ ] Student portal (course view, submission interface)
- [ ] Role-based navigation and access control

### Phase 4: Enhanced Features
- [ ] File upload system for assignments
- [ ] Grade calculation and GPA tracking
- [ ] Email notifications
- [ ] Calendar view of due dates
- [ ] Responsive design

## Recent Implementations

### Django Models (All Implemented)
- **UserProfile:** Extends Django User with role-based permissions (Student/Instructor/Admin)
- **Course:** Academic courses with instructor assignment and term tracking
- **Module:** Organized course content with sequencing
- **Assignment:** Tasks/assessments with types, due dates, and point values
- **Enrollment:** Student-course relationships with grade tracking
- **Submission:** Student work with grading and feedback capabilities

### Admin Interface Customizations
- **CourseAdmin:** Instructor dropdown filtered to users with 'instructor' role only
- **EnrollmentAdmin:** Student dropdown filtered to users with 'student' role only  
- **SubmissionAdmin:** Student dropdown filtered to users with 'student' role only
- All models registered with proper string representations for user-friendly display

### Template System ✅ COMPLETED
- **Template Inheritance:** Proper Django template inheritance with admin/base.html
- **CSS Organization:** All styles moved to external CSS files (no inline styles)
- **admin/index.html:** Clean dashboard extending base template with real content
- **admin/change_list.html:** Styled list views that properly display data
- **admin/base.html:** Master template with navigation, sidebar, and consistent layout
- **Static Files:** Properly configured CSS loading and collection

### Styling Architecture ✅ COMPLETED
- **modern-lms.css:** Core design system with CSS variables and components
- **admin-styles.css:** Admin-specific styles including dashboard cards, tables, forms
- **Template Structure:** Clean separation of concerns between HTML and CSS
- **Responsive Design:** Mobile-friendly admin interface
- **Design System:** Consistent color palette, typography, and component styling

### Database Relationships Tested
- ✅ Course → Module → Assignment hierarchy
- ✅ Student enrollment in courses
- ✅ Assignment submissions by students
- ✅ Role-based user filtering throughout admin interface
- ✅ Sample data creation and display in admin interface

### Production Deployment ✅ COMPLETED
- **Platform:** Render (free tier)
- **Database:** PostgreSQL (production) / SQLite (development)
- **Deployment:** Automatic from GitHub main branch
- **Live URL:** https://lms-python-otqx.onrender.com
- **Environment Variables:** SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL
- **Static Files:** Served via WhiteNoise with proper collection
- **Management Commands:** Automated production data setup

### Django Management Commands
- **setup_production:** Creates superuser and sample data for production
  - SuperKatie superuser account
  - Sample users for each role (student, instructor, admin)
  - Test course: MATH102 - Intermediate Mathematics
  - Sample module, assignment, enrollment, and submission data
  - Prevents duplicate data creation on redeployment

## Architecture

### Project Structure
- `lms_platform/` - Main Django project directory
  - `settings.py` - Django configuration with environment variable management
  - `urls.py` - Main URL routing
  - `core/models.py` - Database models (implemented)
  - `core/views.py` - Application views (basic index view implemented)
  - `core/admin.py` - Custom admin configurations
  - `templates/` - HTML templates (admin templates implemented)
  - `static/` - Static files (CSS organized and implemented)
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
- **Static Files:** Managed by whitenoise with proper collection
- **Process:** Auto-deploy from GitHub main branch
- **Static File Collection:** Must run `collectstatic` before deployment

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
python manage.py collectstatic --noinput
```

### Database Management
```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Set up production data (sample users, courses, etc.)
python manage.py setup_production
```

### Django Management
```bash
# Start a Django shell
python manage.py shell

# Run Django's built-in tests
python manage.py test
```

## Troubleshooting Notes

### Template Issues Resolved
- **Template inheritance:** Learned proper Django block structure for admin templates
- **Static files:** Resolved CSS loading issues by moving from inline styles to external files
- **Data display:** Fixed Django admin list views by using proper `{% result_list cl %}` template tags
- **Debug technique:** Used temporary debug output in templates to identify missing context variables

### Common Development Workflow
1. Make changes to templates or CSS
2. Run `python manage.py collectstatic --noinput` if CSS changes made
3. Hard refresh browser (Ctrl+F5) to clear cache
4. Test functionality before proceeding to next step

## Next Development Goals
- [ ] Style admin add/edit forms
- [ ] Add real data counts to dashboard
- [ ] Create instructor and student frontend portals
- [ ] Implement file upload functionality
- [ ] Add grade calculation features

---

*This project demonstrates modern Django development practices including proper template inheritance, CSS organization, database design, and production deployment. The development approach emphasizes step-by-step learning and collaborative problem-solving.*
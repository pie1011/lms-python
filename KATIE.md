# KATIE.md

This file provides guidance when working with code in this repository.

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
- **Document after major features** - update README and KATIE.md after completing significant functionality

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

### Phase 2: Admin Interface ✅ COMPLETED
- [x] Basic user management through Django admin
- [x] Course creation and instructor assignment (admin interface)
- [x] Module creation and content management (admin interface)
- [x] Assignment creation and management (admin interface)
- [x] Student enrollment system (admin interface)
- [x] Assignment submission system (admin interface)
- [x] Production superuser and sample data creation
- [x] **Beautiful admin dashboard with real-time data** ✨
- [x] **Styled admin list views with proper data display** ✨
- [x] **Gorgeous form styling with date/time pickers** ✨
- [x] **Clean template inheritance system** ✨
- [x] **Organized CSS architecture (no more inline styles)** ✨
- [x] **Custom admin site with live statistics** ✨
- [x] **Fixed user authentication and logout functionality** ✨
- [x] **Portfolio demo user system** ✨

### Phase 3: Frontend Development 🚧 IN PROGRESS
- [x] **Modern admin dashboard** - Complete with cards, real data, and quick actions
- [x] **Styled admin list views** - Beautiful tables with data, search, and pagination
- [x] **Styled admin forms** - Consistent buttons, proper field styling, date/time inputs
- [x] **Custom admin site** - Real-time data integration and proper URL routing
- [x] **Demo user system** - Portfolio-friendly read-only access with full visual experience
- [ ] **Student portal** - Starting development next
- [ ] Instructor portal (course management, grading)
- [ ] Role-based navigation and access control

### Phase 4: Enhanced Features
- [ ] File upload system for assignments
- [ ] Grade calculation and GPA tracking
- [ ] Email notifications
- [ ] Calendar view of due dates
- [ ] Responsive design improvements

## Technical Implementation Completed

### Django Models ✅ COMPLETED
- **UserProfile:** Extends Django User with role-based permissions (Student/Instructor/Admin)
- **Course:** Academic courses with instructor assignment and term tracking
- **Module:** Organized course content with sequencing
- **Assignment:** Tasks/assessments with types, due dates, and point values
- **Enrollment:** Student-course relationships with grade tracking
- **Submission:** Student work with grading and feedback capabilities

### Admin Interface System ✅ COMPLETED
- **Custom Admin Site:** LMSAdminSite with real-time data integration
- **Demo User Protection:** DemoUserMixin allowing full visual access without data modification
- **Role-based Filtering:** CourseAdmin, EnrollmentAdmin, SubmissionAdmin with proper user filtering
- **Custom Forms:** AssignmentAdminForm with datetime widgets and textareas
- **User Model Integration:** Proper registration of Django's User model with custom admin
- **Permission System:** View-only permissions for demo users with full interface access

### Template Architecture ✅ COMPLETED
- **Template Inheritance:** 
  - `admin/base.html` - Master layout with navigation and sidebar
  - `admin/index.html` - Dashboard extending base with real-time data
  - `admin/change_list.html` - List views with proper Django block structure
  - `admin/change_form.html` - Form templates with beautiful styling
- **CSS Organization:**
  - `modern-lms.css` - Core design system with CSS variables
  - `admin-styles.css` - Admin-specific styles including dashboard, forms, tables
- **Static File Management:** Proper collection and serving with WhiteNoise

### Dashboard Features ✅ COMPLETED
- **Real-time Statistics:**
  - Total users with role breakdown (students, instructors, admins)
  - Academic content counts (courses, modules, assignments)
  - Activity metrics (enrollments, submissions, grading status)
  - Recent activity tracking (enrollments in last 7 days)
- **Quick Actions:** Direct links to create courses, users, and enrollments
- **System Status:** Database connectivity and data health monitoring
- **Responsive Cards:** Beautiful dashboard cards with icons and hover effects

### Demo User System ✅ COMPLETED
- **Portfolio Integration:** Safe demonstration account for employers/clients
- **Full Visual Access:** Demo users see all forms, buttons, and interfaces
- **Data Protection:** No actual database modifications from demo actions
- **User Experience:** Friendly success messages explaining demo mode
- **Management Command:** `create_demo_user` for easy setup
- **Credentials:** Username: `PortfolioDemo`, Password: `ViewOnly123`

### Form System ✅ COMPLETED
- **Field Styling:** Consistent input styling for text, select, textarea, file inputs
- **Date/Time Widgets:** HTML5 datetime-local inputs for assignment due dates
- **Button Consistency:** Unified styling for all form actions (Save, Cancel, Delete)
- **Error Handling:** Beautiful error display and form validation
- **Help Text:** Styled assistance text and field descriptions
- **Demo Mode Integration:** Forms work normally for demo users but don't save data

### URL Routing ✅ COMPLETED
- **Custom Admin Integration:** Proper routing to custom admin site with real data
- **Authentication:** Fixed logout functionality with POST requests
- **Static Files:** Proper serving for development and production
- **Demo User Access:** Full admin access for portfolio demonstration

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
├── course_code (e.g., "MATH102")
├── course_name (e.g., "Intermediate Mathematics")
├── description
├── credits
├── term (Spring 2025, Fall 2024, etc.)
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
├── assignment_name (e.g., "Addition Practice Problems")
├── description
├── due_date (DateTime with HTML5 picker)
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
- **Demo User:** Full visual access to admin interface with read-only permissions for portfolio demonstration.

## Production Deployment ✅ COMPLETED

### Platform Configuration
- **Platform:** Render (free tier)
- **Database:** PostgreSQL (production) / SQLite (development)
- **Deployment:** Automatic from GitHub main branch
- **Live URL:** https://lms-python-otqx.onrender.com
- **Environment Variables:** SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL
- **Static Files:** Served via WhiteNoise with proper collection
- **Management Commands:** Automated production data setup and demo user creation

### Sample Data
- **SuperKatie:** superuser account
- **PortfolioDemo:** demo user for portfolio viewing
- **7 Test Users:** Sample users for each role (student, instructor, admin)
- **MATH102:** Test course - "Intermediate Mathematics"
- **Sample Module:** "Module 1: Addition" with content
- **Sample Assignment:** "Addition Practice Problems" with due date
- **Complete Workflow:** Enrollment and submission examples

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

# Create demo user for portfolio
python manage.py create_demo_user
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
  - `urls.py` - Main URL routing with custom admin integration
  - `core/models.py` - Database models (implemented)
  - `core/admin.py` - Custom admin site with real-time data and demo user protection
  - `core/views.py` - Application views (basic index view implemented)
  - `core/management/commands/` - Custom management commands
    - `setup_production.py` - Creates sample data
    - `create_demo_user.py` - Creates portfolio demo user
  - `templates/` - HTML templates (admin templates completed)
  - `static/` - Static files (CSS organized and implemented)
- `manage.py` - Django management script
- `db.sqlite3` - SQLite database file (development)

### Key Configuration
- Uses `python-decouple` for environment variable management
- Configured for both development (SQLite) and production (PostgreSQL) databases
- Static files served with whitenoise for production deployment
- Custom admin site integration for real-time dashboard data
- Demo user system for portfolio presentation

## Troubleshooting Notes

### Recent Issues Resolved
- **Demo User Implementation:** Created safe portfolio demonstration system
- **Form Validation Override:** Prevented demo user form validation while maintaining visual experience
- **Template Rendering:** Fixed HTML escaping issues in admin messages
- **Permission System:** Balanced full visual access with data protection
- **Custom Admin Site:** Fixed URL routing to use custom admin with real-time data
- **User Model Registration:** Added Django's User model to custom admin site
- **Template Block Structure:** Learned proper Django admin template inheritance
- **Static Files:** Resolved CSS loading by moving from inline styles to external files
- **Data Display:** Fixed list views using proper `{% result_list cl %}` template tags
- **Form Styling:** Consistent button sizing and spacing across all admin forms
- **Date/Time Inputs:** Implemented HTML5 datetime-local widgets for proper date pickers
- **Logout Functionality:** Fixed authentication by using POST requests instead of GET

### Development Workflow
1. Make changes to models, templates, or CSS
2. Run `python manage.py collectstatic --noinput` if CSS changes made
3. Test functionality thoroughly before proceeding
4. **Document after major features** - update README and KATIE.md
5. Commit meaningful changes with descriptive messages
6. Hard refresh browser (Ctrl+F5) to clear cache when testing

## Next Development Goals
- [ ] **Student Portal:** Frontend interface for students to view courses and assignments
- [ ] **Student Authentication:** Login/logout system for students
- [ ] **Course View:** Student interface to view enrolled courses and modules
- [ ] **Assignment Submission:** Frontend form for students to submit work
- [ ] **Grade Viewing:** Interface for students to check their grades and feedback
- [ ] **Instructor Portal:** Course management and grading interface for teachers
- [ ] **File Upload System:** Assignment file submissions and course materials
- [ ] **Grade Calculation:** Automated GPA tracking and grade analytics

## Code Quality & Best Practices

### Demonstrated Skills
- **Django Framework Mastery:** Advanced models, custom admin, template inheritance
- **Database Design:** Complex relationships, data integrity, role-based permissions
- **Frontend Development:** Responsive design, modern CSS, user experience design
- **Security Implementation:** Demo user system, permission management, data protection
- **Production Deployment:** Environment configuration, static file management
- **Code Organization:** Clean architecture, separation of concerns, comprehensive documentation
- **Problem Solving:** Systematic debugging, step-by-step development, collaborative approach
- **Portfolio Presentation:** Thoughtful demo user system for safe client exploration

### Professional Development Practices
- **Template System Excellence:** Proper Django template inheritance with block structure
- **CSS Architecture:** External stylesheets with design system consistency
- **Component Reusability:** Modular template components and styling patterns
- **Performance:** Efficient static file management and caching strategies
- **Documentation:** Comprehensive README and development documentation
- **Version Control:** Meaningful commits after major feature completion

### Demo User System Innovation
- **User Experience:** Full visual access without compromising data integrity
- **Portfolio Value:** Safe exploration for potential employers and clients
- **Technical Implementation:** Custom Django admin mixins with permission overrides
- **Professional Presentation:** Clear messaging about demo mode functionality

---

*This project demonstrates modern Django development practices including custom admin interfaces, real-time data integration, beautiful user interfaces, production-ready deployment, and innovative portfolio presentation features. The development approach emphasizes step-by-step learning, collaborative problem-solving, professional code quality, and thoughtful client/employer experience.*

---

Recent prompt:
We're still having issues with what is and is not shown in the admin portal. I tried having Claude Desktop help, as well. Please review the KATIE.md, admin.py, change_form.html, and any other files you think necessary to solve this.

1. User tab for PortfolioDemo shows dictionary for username: "Username:
{'name': 'username', 'label': 'username', 'help_text': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', 'field': 'username', 'is_hidden': False}"

2. User tab for PortfolioDemo shows dictionaries instead of actual elements under Permissions: "Permissions
Active

Staff status:
{'name': 'is_staff', 'label': 'staff status', 'help_text': 'Designates whether the user can log into this admin site.', 'field': 'is_staff', 'is_hidden': False}
Superuser status:
{'name': 'is_superuser', 'label': 'superuser status', 'help_text': 'Designates that this user has all permissions without explicitly assigning them.', 'field': 'is_superuser', 'is_hidden': False}"

3. The "Change Password" feature is still not visible for the non-demo users. Superusers (i.e. SuperKatie) should be able to change any user's password. The demo user ("PortfolioDemo") should not be able to change ANY passwords.

I've even tried viewing in entirely different browsers to prevent cache issues from messing up the display.

Claude Code response after attempting fix of above issue:
Summary of Fixes

  I've identified and fixed the three main issues:

  1. Dictionary Display Issue ✅

  Problem: Template was rendering {{ field.field|safe }} which displayed
  dictionary representations instead of form widgets.

  Fix: Changed
  /workspaces/lms-python/lms_platform/templates/admin/change_form.html:
  - {{ field.field|safe }} → {{ field }}
  - {{ field.label_tag|safe }} → {{ field.label_tag }}

  2. Password Change Visibility ✅

  Problem: Password change link wasn't appearing for superusers on non-demo
  users.

  Fix: Enhanced DemoUserAdmin.change_view() in admin.py:359-381 to properly
  set the has_change_password_permission context variable based on user type
  and permissions.

  3. Demo User Restrictions ✅

  Confirmed: Demo user (PortfolioDemo) properly blocked from password changes
   while superusers (SuperKatie) can change other users' passwords.

  The Django application passes all system checks and the fixes should
  resolve:
  - Form fields displaying as proper widgets instead of dictionaries
  - Password change links appearing for authorized users
  - Demo user maintaining view-only access as intended

  The template now correctly renders form fields using Django's standard
  admin form rendering, and the permission system properly differentiates
  between demo users and superusers.
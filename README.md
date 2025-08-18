# LMS Platform

A comprehensive Learning Management System built with Django, demonstrating full-stack web development skills and modern deployment practices.

🔗 **Live Demo:** [https://lms-python-otqx.onrender.com](https://lms-python-otqx.onrender.com)

## 🎭 Try the Demo!

**Experience the full admin interface without making any changes:**

- **Username:** `PortfolioDemo`
- **Password:** `ViewOnly123`

*Explore all features, forms, and functionality - the interface works perfectly but no data is modified!*

## Overview

This LMS Platform is a portfolio project showcasing professional Django development skills, complex database design, and production deployment capabilities. The system supports three user roles (Students, Instructors, Administrators) with a complete academic workflow from course creation to assignment submission and grading.

## Features

### ✅ Completed Features
- **User Management**: Role-based authentication (Student, Instructor, Admin)
- **Academic Structure**: Courses → Modules → Assignments hierarchy
- **Enrollment System**: Student-course relationships with grade tracking
- **Assignment Management**: Creation, submission, and grading workflow with date/time pickers
- **Modern Admin Interface**: Custom-styled admin dashboard with real-time data
- **Demo User System**: Portfolio-friendly demo account with read-only access
- **Responsive Design**: Mobile-friendly admin interface with consistent styling
- **Production Deployment**: Live on Render with PostgreSQL database
- **Automated Setup**: Django management commands for production data

### 🎨 Design & User Experience
- **Beautiful Dashboard**: Real-time statistics and quick actions with live database counts
- **Styled List Views**: Professional tables with search, filtering, and pagination
- **Modern Forms**: Clean form styling with proper date/time inputs and validation
- **Template Inheritance**: Organized, maintainable template structure
- **CSS Architecture**: External stylesheets with design system consistency
- **User-Friendly Navigation**: Intuitive admin sidebar and breadcrumbs
- **Demo Mode**: Safe exploration mode for portfolio viewers

### 🛡️ Security & Access Control
- **Role-Based Permissions**: Custom admin filtering based on user roles
- **Demo User Protection**: Full visual access without data modification capabilities
- **Secure Authentication**: Proper logout handling and session management
- **Permission System**: Django's built-in permissions with custom extensions

### 🚧 In Development
- **Student Portal**: Frontend interface for students to view courses and submit assignments
- **Instructor Portal**: Course management and grading interface for teachers
- **File Upload System**: Assignment file submissions and course materials
- **Grade Calculations**: Automated GPA tracking and grade analytics
- **Email Notifications**: Alerts for assignments, grades, and deadlines

## Technology Stack

- **Backend**: Django 5.2.2
- **Database**: PostgreSQL (production), SQLite (development)
- **Deployment**: Render with automated GitHub integration
- **Static Files**: WhiteNoise for production static file serving
- **Server**: Gunicorn for production WSGI
- **Styling**: Custom CSS with modern design patterns
- **Security**: Django permissions with custom demo user system

## Database Schema

The system implements a comprehensive academic data model:

```
Users (Django Auth) ←→ UserProfile (roles)
     ↓
Course → Module → Assignment → Submission
     ↓              ↓
Enrollment ←→ Student    Student
```

### Key Relationships
- **Course** has many **Modules** (organized content)
- **Module** has many **Assignments** (tasks/assessments)  
- **Assignment** has many **Submissions** (student work)
- **Students** enroll in **Courses** (many-to-many via Enrollments)
- **Submissions** contain grades and feedback

## Installation & Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/pie1011/lms-python.git
   cd lms-python
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py setup_production  # Creates sample data
   python manage.py create_demo_user   # Creates portfolio demo user
   ```

5. **Static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

### Production Deployment

The application is configured for deployment on Render:

1. **Environment Variables**:
   - `SECRET_KEY`: Django secret key
   - `DEBUG`: Set to `False` for production
   - `DATABASE_URL`: PostgreSQL connection string
   - `ALLOWED_HOSTS`: Your domain name

2. **Build Command**:
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py setup_production && python manage.py create_demo_user
   ```

3. **Start Command**:
   ```bash
   gunicorn lms_platform.wsgi:application
   ```

## Usage

### Demo Access (Portfolio Viewers)
Access the admin interface at `/admin/` with demo credentials:
- **Username:** `PortfolioDemo`
- **Password:** `ViewOnly123`

**Demo Features:**
- **Full Visual Access**: See all forms, buttons, and interfaces
- **Safe Exploration**: Click anything without affecting real data
- **Success Feedback**: Friendly messages explaining demo mode
- **Complete Experience**: Experience the full functionality safely

### Full Administrative Access
Access with superuser credentials for complete functionality:

**Dashboard Features:**
- **Real-time Statistics**: Live user counts, course enrollment data, and submission metrics
- **Quick Actions**: Direct links to create courses, users, and enrollments
- **System Status**: Database connectivity and data health monitoring
- **Beautiful Design**: Modern cards, responsive layout, and intuitive navigation

**Administrative Capabilities:**
- **User Management**: Create and manage student, instructor, and admin accounts
- **Course Creation**: Set up courses with modules and assignments
- **Enrollment Management**: Enroll students in courses and track progress
- **Assignment Tools**: Create assignments with due dates and point values
- **Grading System**: Review and grade student submissions

### Sample Data
The production deployment includes sample data:
- **8 Test Users**: Including demo user and all role types
- **Sample Course**: "MATH102 - Intermediate Mathematics"
- **Course Content**: Module and assignment examples
- **Complete Workflow**: Enrollment and submission examples

## Project Structure

```
lms-python/
├── lms_platform/           # Main Django project
│   ├── core/              # Core application
│   │   ├── models.py      # Database models
│   │   ├── admin.py       # Custom admin with demo user protection
│   │   ├── management/    # Custom management commands
│   │   │   └── commands/
│   │   │       ├── setup_production.py
│   │   │       └── create_demo_user.py
│   │   └── ...
│   ├── templates/         # Template system
│   │   ├── admin/         # Custom admin templates
│   │   │   ├── base.html  # Master admin layout
│   │   │   ├── index.html # Dashboard with real data
│   │   │   ├── change_list.html # Styled list views
│   │   │   └── change_form.html # Beautiful forms
│   │   └── index.html     # Landing page
│   ├── static/           # Static files
│   │   ├── css/          # Organized stylesheets
│   │   │   ├── modern-lms.css # Core design system
│   │   │   └── admin-styles.css # Admin interface styles
│   │   └── js/           # JavaScript functionality
│   ├── settings.py       # Django configuration
│   └── urls.py           # URL routing with custom admin
├── requirements.txt      # Python dependencies
├── KATIE.md             # Development documentation
└── README.md            # This file
```

## Development Highlights

### Technical Skills Demonstrated
- **Django Framework**: Advanced models, custom admin, template inheritance
- **Database Design**: Complex relationships, data integrity, role-based permissions
- **Frontend Development**: Responsive design, modern CSS, user experience
- **Security**: Custom permission systems, demo user implementation
- **Production Deployment**: Environment configuration, static file management
- **Code Organization**: Clean architecture, separation of concerns, documentation

### Professional Development Practices
- **Template Inheritance**: DRY principles with Django's template system
- **CSS Architecture**: External stylesheets, design systems, maintainable code
- **Database Management**: Custom management commands, automated data setup
- **Version Control**: Meaningful commits, documented progress, collaborative workflow
- **Problem Solving**: Systematic debugging, step-by-step development approach
- **Portfolio Presentation**: Demo user system for safe client/employer exploration

## Portfolio Value

This project demonstrates:
- **Full-Stack Capabilities**: Backend logic, database design, frontend styling
- **Real-World Application**: Practical business logic for education technology
- **Production Readiness**: Deployed application with professional deployment practices
- **User Experience Focus**: Intuitive interfaces, responsive design, modern aesthetics
- **Security Awareness**: Safe demo modes, permission systems, data protection
- **Technical Depth**: Advanced Django features, custom admin interfaces, complex data relationships
- **Professional Presentation**: Thoughtful demo user system for portfolio viewing

## Contributing

This is a portfolio project, but feedback and suggestions are welcome! Please open an issue to discuss potential improvements.

## License

This project is for educational and portfolio purposes.

---

**Portfolio Project by Katie Harshman**  
🔗 [Portfolio Website](https://katieharshman.com)  
🔗 [Live Demo](https://lms-python-otqx.onrender.com) - Try it with `PortfolioDemo` / `ViewOnly123`  
🔗 [GitHub Repository](https://github.com/pie1011/lms-python)

*Demonstrating modern Django development with professional design, real-world functionality, production deployment practices, and thoughtful portfolio presentation.*

# LMS Platform

A comprehensive Learning Management System built with Django, demonstrating full-stack web development skills and modern deployment practices.

🔗 **Live Demo:** [https://lms-python-otqx.onrender.com](https://lms-python-otqx.onrender.com)

## Overview

This LMS Platform is a portfolio project showcasing professional Django development skills, complex database design, and production deployment capabilities. The system supports three user roles (Students, Instructors, Administrators) with a complete academic workflow from course creation to assignment submission and grading.

## Features

### ✅ Completed Features
- **User Management**: Role-based authentication (Student, Instructor, Admin)
- **Academic Structure**: Courses → Modules → Assignments hierarchy
- **Enrollment System**: Student-course relationships with grade tracking
- **Assignment Management**: Creation, submission, and grading workflow
- **Admin Interface**: Customized Django admin with role-based filtering
- **Production Deployment**: Live on Render with PostgreSQL database
- **Automated Setup**: Django management commands for production data

### 🚧 Planned Features
- Frontend student/instructor portals
- File upload system for assignments
- Grade calculation and GPA tracking
- Email notifications
- Calendar integration
- Responsive design

## Technology Stack

- **Backend**: Django 5.2.2
- **Database**: PostgreSQL (production), SQLite (development)
- **Deployment**: Render
- **Static Files**: WhiteNoise
- **Server**: Gunicorn

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
   ```

5. **Run development server**
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
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py setup_production
   ```

3. **Start Command**:
   ```bash
   gunicorn lms_platform.wsgi:application
   ```

## Usage

### Admin Interface
Access the Django admin at `/admin/` with superuser credentials:
- **Administrators**: Full system access
- **Instructors**: Course and assignment management 
- **Students**: Limited to their own data

### Sample Data
The production deployment includes sample data:
- Test course: "MATH101 - Introduction to Mathematics"
- Sample module: "Module 1: Addition"
- Example assignment and submission workflow

## Project Structure

```
lms-python/
├── lms_platform/           # Main Django project
│   ├── core/              # Core application
│   │   ├── models.py      # Database models
│   │   ├── admin.py       # Admin customizations
│   │   ├── management/    # Custom commands
│   │   └── ...
│   ├── settings.py        # Django configuration
│   └── urls.py           # URL routing
├── requirements.txt       # Python dependencies
├── KATIE.md              # Development documentation
└── README.md             # This file
```

## Development Process

This project demonstrates:
- **Database Design**: Complex relationships and data modeling
- **Django Best Practices**: Models, admin, management commands
- **Production Deployment**: Environment configuration, static files
- **Code Quality**: Documentation, version control, testing
- **Problem Solving**: Debugging deployment issues, browser caching

## Portfolio Highlights

### Technical Skills Demonstrated
- Django framework proficiency
- PostgreSQL database design
- Production deployment and DevOps
- Custom Django admin interfaces
- Database relationship modeling
- Environment-based configuration

### Professional Development Practices
- Comprehensive documentation (KATIE.md)
- Version control with meaningful commits
- Production-ready configuration
- Automated deployment pipeline
- Code organization and structure

## Contributing

This is a portfolio project, but feedback and suggestions are welcome! Please open an issue to discuss potential improvements.

## License

This project is for educational and portfolio purposes.

---

**Portfolio Project by Katie Harshman**  
🔗 [Portfolio Website](https://katieharshman.com)  
🔗 [Live Demo](https://lms-python-otqx.onrender.com)
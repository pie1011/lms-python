# KATIE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django web application named "hello_world" - a simple starter project set up for GitHub Codespaces development. The project uses Django 5.2.2 with SQLite as the database and includes browser reload functionality for development.

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
- `hello_world/` - Main Django project directory
  - `settings.py` - Django configuration with Codespaces-specific setup
  - `urls.py` - Main URL routing
  - `core/views.py` - Core application views
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, images)
- `manage.py` - Django management script
- `db.sqlite3` - SQLite database file

### Key Configuration
- Uses `python-decouple` for environment variable management
- Configured for GitHub Codespaces with automatic CSRF trusted origins
- Includes `django-browser-reload` for live reloading during development
- Static files served from `hello_world/static/` in development
- Templates located in `hello_world/templates/`

### Environment Variables
The application uses environment variables via `python-decouple`:
- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode toggle
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- Codespaces-specific variables are automatically detected and configured

## Development Notes

- The project is configured for GitHub Codespaces with port forwarding on port 8000
- Browser reload is enabled for development - changes to templates and static files trigger automatic reloads
- The main view is a simple index page rendering `templates/index.html`
- Admin interface is available at `/admin/` after creating a superuser
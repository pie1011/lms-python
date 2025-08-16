from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from lms_platform.core.models import UserProfile, Course, Module, Assignment, Enrollment, Submission


class Command(BaseCommand):
    help = 'Set up production data for the LMS including superuser, sample users, course, and assignments'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting production data setup...'))

        # Create superuser
        self.create_superuser()
        
        # Create sample users with profiles
        student_user = self.create_sample_users()
        
        # Create sample course
        course = self.create_sample_course()
        
        # Create sample module
        module = self.create_sample_module(course)
        
        # Create sample assignment
        assignment = self.create_sample_assignment(module)
        
        # Create enrollment
        enrollment = self.create_sample_enrollment(student_user, course)
        
        # Create sample submission
        self.create_sample_submission(student_user, assignment)

        self.stdout.write(
            self.style.SUCCESS('Production data setup completed successfully!')
        )

    def create_superuser(self):
        """Create superuser if it doesn't exist"""
        username = 'SuperKatie'
        password = 'lms-password123'
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(f'Superuser "{username}" already exists.')
            return
        
        superuser = User.objects.create_superuser(
            username=username,
            email='superkatie@lms.com',
            password=password,
            first_name='Super',
            last_name='Katie'
        )
        
        # Create admin UserProfile
        UserProfile.objects.create(
            user=superuser,
            role='admin',
            first_name='Super',
            last_name='Katie',
            phone_number='555-0001'
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Created superuser: {username}')
        )

    def create_sample_users(self):
        """Create sample users for each role"""
        users_data = [
            {
                'username': 'student1',
                'email': 'student1@lms.com',
                'first_name': 'Alice',
                'last_name': 'Student',
                'role': 'student',
                'phone': '555-0002'
            },
            {
                'username': 'instructor1',
                'email': 'instructor1@lms.com',
                'first_name': 'Bob',
                'last_name': 'Professor',
                'role': 'instructor',
                'phone': '555-0003'
            },
            {
                'username': 'admin1',
                'email': 'admin1@lms.com',
                'first_name': 'Carol',
                'last_name': 'Administrator',
                'role': 'admin',
                'phone': '555-0004'
            }
        ]
        
        student_user = None
        for user_data in users_data:
            if User.objects.filter(username=user_data['username']).exists():
                self.stdout.write(f'User "{user_data["username"]}" already exists.')
                if user_data['role'] == 'student':
                    student_user = User.objects.get(username=user_data['username'])
                continue
            
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password='password123',
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            
            UserProfile.objects.create(
                user=user,
                role=user_data['role'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                phone_number=user_data['phone']
            )
            
            if user_data['role'] == 'student':
                student_user = user
            
            self.stdout.write(
                self.style.SUCCESS(f'Created {user_data["role"]}: {user_data["username"]}')
            )
        
        # Return student user for enrollment
        if not student_user:
            student_user = User.objects.filter(userprofile__role='student').first()
        
        return student_user

    def create_sample_course(self):
        """Create sample course"""
        course_code = 'MATH102'
        term = 'Spring 2025'
        
        # Check if course already exists
        if Course.objects.filter(course_code=course_code).exists():
            self.stdout.write(f'Course "{course_code}" already exists.')
            return Course.objects.get(course_code=course_code)
        
        # Get instructor user
        instructor = User.objects.filter(userprofile__role='instructor').first()
        if not instructor:
            # Fallback to superuser if no instructor exists
            instructor = User.objects.filter(is_superuser=True).first()
        
        course = Course.objects.create(
            course_code=course_code,
            course_name='Intermediate Mathematics',
            description='A comprehensive introduction to intermediate mathematical concepts including arithmetic, basic algebra, and problem-solving techniques.',
            credits=3,
            term=term,
            instructor=instructor,
            max_enrollment=30
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Created course: {course}')
        )
        
        return course

    def create_sample_module(self, course):
        """Create sample module for the course"""
        module_name = 'Module 1: Addition'
        
        # Check if module already exists
        if Module.objects.filter(course=course, module_name=module_name).exists():
            self.stdout.write(f'Module "{module_name}" already exists.')
            return Module.objects.get(course=course, module_name=module_name)
        
        module = Module.objects.create(
            course=course,
            module_name=module_name,
            description='Introduction to addition operations and basic arithmetic principles.',
            order_number=1,
            content='''
            # Module 1: Addition

            ## Learning Objectives
            - Understand the concept of addition
            - Perform basic addition operations
            - Apply addition to real-world problems

            ## Content
            Addition is one of the four basic operations of arithmetic. In this module, you will learn:
            1. What addition means
            2. How to add single-digit numbers
            3. How to add multi-digit numbers
            4. Word problems involving addition

            ## Practice Problems
            Complete the assignment to practice what you've learned!
            '''
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Created module: {module}')
        )
        
        return module

    def create_sample_assignment(self, module):
        """Create sample assignment for the module"""
        assignment_name = 'Addition Practice Problems'
        
        # Check if assignment already exists
        if Assignment.objects.filter(module=module, assignment_name=assignment_name).exists():
            self.stdout.write(f'Assignment "{assignment_name}" already exists.')
            return Assignment.objects.get(module=module, assignment_name=assignment_name)
        
        # Set due date to 2 weeks from now
        due_date = timezone.now() + timedelta(days=14)
        
        assignment = Assignment.objects.create(
            module=module,
            assignment_name=assignment_name,
            description='Practice problems to reinforce addition concepts learned in Module 1.',
            due_date=due_date,
            max_points=100,
            assignment_type='homework',
            instructions='''
            Complete the following addition problems:

            1. 25 + 37 = ?
            2. 156 + 289 = ?
            3. 1,247 + 3,856 = ?
            4. Word Problem: Sarah has 45 apples and John gives her 28 more apples. How many apples does Sarah have now?
            5. Word Problem: A school has 234 students in the morning. 67 more students arrive for the afternoon session. What is the total number of students?

            Show your work for each problem. Partial credit will be given for correct methodology even if the final answer is incorrect.
            '''
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Created assignment: {assignment}')
        )
        
        return assignment

    def create_sample_enrollment(self, student_user, course):
        """Create sample enrollment"""
        # Check if enrollment already exists
        if Enrollment.objects.filter(student=student_user, course=course).exists():
            self.stdout.write(f'Enrollment for {student_user.username} in {course.course_code} already exists.')
            return Enrollment.objects.get(student=student_user, course=course)
        
        enrollment = Enrollment.objects.create(
            student=student_user,
            course=course,
            current_grade=None,  # Will be calculated from submissions
            status='active'
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Created enrollment: {enrollment}')
        )
        
        return enrollment

    def create_sample_submission(self, student_user, assignment):
        """Create sample submission"""
        # Check if submission already exists
        if Submission.objects.filter(student=student_user, assignment=assignment).exists():
            self.stdout.write(f'Submission for {student_user.username} on {assignment.assignment_name} already exists.')
            return
        
        submission = Submission.objects.create(
            student=student_user,
            assignment=assignment,
            submission_content='''
            My solutions to the addition problems:

            1. 25 + 37 = 62
            2. 156 + 289 = 445
            3. 1,247 + 3,856 = 5,103
            4. Sarah has 45 + 28 = 73 apples
            5. Total students = 234 + 67 = 301 students

            I showed my work by adding the numbers step by step. For the multi-digit problems, I aligned the numbers by place value and added column by column, carrying over when necessary.
            ''',
            grade=95.0,  # Sample grade
            feedback='Excellent work! All answers are correct and you showed clear methodology. Keep up the good work!',
            graded_by=assignment.module.course.instructor,
            graded_at=timezone.now(),
            status='graded'
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Created submission: {submission}')
        )
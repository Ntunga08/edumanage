# 🎓 EduManage - School Management System

A modern, comprehensive school management system built with Django that helps teachers and administrators manage classes, students, and academic performance efficiently.

## ✨ Features

### 📊 **Dynamic Dashboard**
- Real-time statistics showing total students, classes, teachers, and subjects
- Interactive class overview with student counts
- Performance analytics and insights

### 👨‍🏫 **Teacher Features**
- **Class Management**: View all assigned classes with detailed information
- **Student Tracking**: Monitor student enrollment and performance
- **Exam Results**: Track and analyze student exam performance
- **Performance Analytics**: View class averages and individual student grades

### 👥 **Student Management**
- Complete student profiles with personal information
- Parent contact details
- Enrollment tracking
- Academic performance history

### 📚 **Class & Subject Management**
- Comprehensive class information (grade, section, room, capacity)
- Subject tracking with codes and descriptions
- Teacher assignments and class-subject relationships
- Student enrollment management

### 📝 **Exam & Results System**
- Multiple exam types (Midterm, Final, Quiz, Assignment, Project)
- Detailed result tracking with grades and percentages
- Performance analytics and grade calculations
- Teacher remarks and feedback

### 🔧 **Admin Interface**
- Full Django admin integration for easy data management
- User-friendly forms for adding students, classes, subjects, and exams
- Bulk operations and data import capabilities
- Comprehensive reporting and analytics

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ntunga08/edumanage.git
   cd edumanage
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   cd myproject
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Generate sample data (optional)**
   ```bash
   python manage.py create_sample_data
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main application: http://localhost:8000/
   - Admin interface: http://localhost:8000/admin/

## 📖 Usage Guide

### For Administrators

#### Adding New Data
1. **Login to Admin Interface**: http://localhost:8000/admin/
2. **Add Subjects**: Go to Subjects → Add Subject
3. **Add Teachers**: Go to Users → Add User (check "Is Staff")
4. **Add Classes**: Go to Classes → Add Class
5. **Add Students**: Go to Students → Add Student
6. **Enroll Students**: Go to Student Classes → Add Student Class
7. **Add Exams**: Go to Exams → Add Exam
8. **Add Results**: Go to Results → Add Result

#### Sample Data
Use the management command to quickly populate the system:
```bash
python manage.py create_sample_data
```
This creates:
- 5 subjects (Mathematics, English, Science, History, Geography)
- 1 teacher account (username: `teacher1`, password: `password123`)
- 3 classes with different grade levels
- 6 students with sample data
- Multiple exams and results

### For Teachers

#### Viewing Your Classes
1. Login with your teacher account
2. Navigate to "Classes" in the sidebar
3. View all your assigned classes with student counts and recent performance

#### Analyzing Student Performance
1. Click "View Class Details & Results" on any class
2. See comprehensive student information
3. Review exam results and performance analytics
4. Track individual student progress

#### Dashboard Overview
- View real-time statistics
- Monitor class performance trends
- Access quick navigation to all features

## 🏗️ Project Structure

```
edumanage/
├── myproject/
│   ├── edumanage/
│   │   ├── models.py          # Database models
│   │   ├── views.py           # Application views
│   │   ├── urls.py            # URL routing
│   │   ├── admin.py           # Admin interface
│   │   ├── forms.py           # Form definitions
│   │   ├── templates/         # HTML templates
│   │   ├── static/            # Static files (CSS, JS, images)
│   │   ├── migrations/        # Database migrations
│   │   ├── management/        # Custom management commands
│   │   └── templatetags/      # Custom template filters
│   ├── manage.py              # Django management script
│   └── requirements.txt       # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🗄️ Database Models

### Core Models
- **User**: Teachers and administrators
- **Student**: Student information and profiles
- **Class**: Class details and assignments
- **Subject**: Academic subjects
- **StudentClass**: Student enrollment in classes
- **Exam**: Exam definitions and details
- **Result**: Student exam results and grades

### Key Features
- **Automatic Grade Calculation**: A+ to F based on percentage
- **Performance Analytics**: Class averages and trends
- **Data Validation**: Ensures data integrity
- **Relationship Management**: Proper foreign key relationships

## 🎨 User Interface

### Design Features
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Clean, professional interface using Tailwind CSS
- **Intuitive Navigation**: Easy-to-use sidebar navigation
- **Visual Feedback**: Color-coded performance indicators
- **Interactive Elements**: Hover effects and smooth transitions

### Color Scheme
- **Primary**: Blue (#0369a1) - Professional and trustworthy
- **Success**: Green - Good performance indicators
- **Warning**: Yellow - Average performance
- **Danger**: Red - Poor performance
- **Info**: Blue - General information

## 🔒 Security Features

### Data Protection
- **Database Security**: SQLite with proper access controls
- **User Authentication**: Django's built-in authentication system
- **Admin Access**: Restricted admin interface
- **Input Validation**: Form validation and sanitization

### Git Security
- **Sensitive Files Excluded**: Database files, environment variables, secrets
- **Virtual Environment Ignored**: Prevents dependency conflicts
- **Cache Files Excluded**: Keeps repository clean

## 🛠️ Development

### Adding New Features
1. Create new models in `models.py`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Add views in `views.py`
5. Update URLs in `urls.py`
6. Create templates in `templates/`
7. Update admin interface in `admin.py`

### Custom Management Commands
Create new commands in `management/commands/`:
```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Description of your command'
    
    def handle(self, *args, **options):
        # Your command logic here
        pass
```

## 📊 Performance

### Optimizations
- **Database Queries**: Optimized with select_related and prefetch_related
- **Template Caching**: Efficient template rendering
- **Static Files**: Properly served and cached
- **Database Indexing**: Optimized for common queries

### Scalability
- **Modular Design**: Easy to extend and modify
- **Database Agnostic**: Can switch to PostgreSQL, MySQL, etc.
- **API Ready**: Structure supports REST API development
- **Multi-tenant Ready**: Can be adapted for multiple schools

## 🤝 Contributing

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add comments for complex logic
- Write docstrings for functions and classes

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Django Framework**: For the robust web framework
- **Tailwind CSS**: For the beautiful UI components
- **Django Admin**: For the powerful admin interface
- **Open Source Community**: For inspiration and best practices

## 📞 Support

### Getting Help
- **Documentation**: Check this README and Django documentation
- **Issues**: Report bugs and feature requests on GitHub
- **Community**: Join Django community forums and discussions

### Common Issues
- **Database Errors**: Run `python manage.py migrate`
- **Static Files**: Ensure `python manage.py collectstatic` is run
- **Permission Errors**: Check file permissions and virtual environment

---

**Made with ❤️ for better education management**

*EduManage - Empowering educators with modern tools for student success* 
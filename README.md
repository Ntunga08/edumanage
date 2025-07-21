# 🎓 EduManage - School Management System

A modern, comprehensive school management system built with Django that helps teachers and administrators manage classes, students, and academic performance efficiently. Features responsive design optimized for both mobile and desktop use, with a complete reports and documentation system.

## ✨ Features

### 📱 **Mobile-First Responsive Design**
- **Mobile-Optimized Authentication**: Beautiful login and registration forms with floating borders
- **Responsive Breakpoints**: Automatic adaptation between mobile and desktop views
- **Touch-Friendly Interface**: Optimized for smartphone and tablet use
- **Glass-Morphism Design**: Modern UI with backdrop blur and rounded corners
- **Cross-Device Compatibility**: Seamless experience across all screen sizes
- **Mobile-Specific Optimizations**: Reduced form heights and spacing for mobile screens

### 📊 **Dynamic Dashboard**
- Real-time statistics showing total students, classes, teachers, and subjects
- Interactive class overview with student counts
- Performance analytics and insights
- Responsive layout that works on mobile and desktop
- Live data from admin interface

### 📝 **Comprehensive Reports System**
- **Teacher Logbooks**: Daily, weekly, and monthly teaching reports
- **Teacher Workplans**: Beginning and end of term planning documents
- **Academic Master Review**: Admin review and approval system
- **Status Tracking**: Draft, submitted, reviewed, approved, rejected statuses
- **Detailed Analysis**: Success, challenges, and solutions documentation
- **Performance Analytics**: Student performance analysis and recommendations

#### Logbook Features
- **Daily Reports**: Detailed lesson coverage and student engagement
- **Weekly Reports**: Weekly progress and activity summaries
- **Monthly Reports**: Comprehensive monthly analysis
- **Challenge Documentation**: Problems encountered and solutions implemented
- **Next Lesson Planning**: Forward-looking lesson preparation
- **Student Participation Tracking**: Engagement and participation analysis

#### Workplan Features
- **Beginning of Term**: Learning objectives and teaching strategies
- **End of Term**: Achievement analysis and performance review
- **Mid Term**: Progress assessment and adjustment planning
- **Resource Planning**: Materials and resources needed
- **Timeline Management**: Schedule and timeline for topics
- **Performance Analysis**: Student performance evaluation and recommendations

### 👨‍🏫 **Teacher Features**
- **Class Management**: View all assigned classes with detailed information
- **Student Tracking**: Monitor student enrollment and performance
- **Exam Results**: Track and analyze student exam performance
- **Performance Analytics**: View class averages and individual student grades
- **Mobile Access**: Full functionality on smartphones and tablets
- **Reports Creation**: Create and submit logbooks and workplans
- **Documentation System**: Comprehensive teaching documentation
- **Profile View**: Teachers can view their own profile (name, classes, subjects taught, total students) by clicking the "Teacher" bar in the sidebar. Headmasters/admins can view all teachers' profiles and their classes.

### 👥 **Student Management**
- Complete student profiles with personal information
- Parent contact details
- Enrollment tracking
- Academic performance history
- Responsive student listing and details
- Gender-based statistics and analytics

### 📚 **Class & Subject Management**
- Comprehensive class information (grade, section, room, capacity)
- Subject tracking with codes and descriptions
- Teacher assignments and class-subject relationships
- Student enrollment management
- Mobile-friendly class overview
- Available seats tracking
- Student count by gender

### 📝 **Exam & Results System**
- Multiple exam types (Midterm, Final, Quiz, Assignment, Project)
- Detailed result tracking with grades and percentages
- Performance analytics and grade calculations
- Teacher remarks and feedback
- Responsive result display
- Automatic grade calculation (A+ to F)
- Class performance averages

### 🔧 **Admin Interface**
- Full Django admin integration for easy data management
- User-friendly forms for adding students, classes, subjects, and exams
- Bulk operations and data import capabilities
- Comprehensive reporting and analytics
- Mobile-responsive admin interface
- Reports review and approval system
- Teacher logbook and workplan management

### 🔐 **Enhanced Authentication**
- **Modern Login Form**: Responsive design with glass-morphism effect
- **Registration System**: User-friendly account creation
- **Secure Logout**: Proper session management
- **Mobile Optimization**: Touch-friendly authentication forms
- **Error Handling**: Clear validation messages with icons
- **Floating Borders**: Modern design that doesn't touch screen edges
- **Rounded Corners**: Soft, contemporary appearance

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
   python manage.py runserver 0.0.0.0:8000
   ```

8. **Access the application**
   - Main application: http://localhost:8000/
   - Admin interface: http://localhost:8000/admin/
   - **Mobile access**: Use your local IP (e.g., http://192.168.1.246:8000/)

## 📱 Mobile Access

### Smartphone & Tablet Usage
- **Direct Access**: Visit the app URL on your mobile browser
- **Responsive Forms**: Authentication forms automatically adapt to screen size
- **Touch Navigation**: Optimized for finger navigation
- **Fast Loading**: Optimized for mobile networks
- **Offline Capability**: Works with intermittent connectivity
- **Floating Design**: Forms don't touch screen edges for modern look

### Mobile Features
- **Compact Mobile View**: Optimized spacing for small screens
- **Desktop Spacious View**: Comfortable layout for larger screens
- **Floating Borders**: Modern glass-morphism design
- **Rounded Corners**: Soft, modern appearance
- **Smooth Animations**: Enhanced user experience
- **Reduced Form Heights**: Optimized for mobile screen constraints

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

#### Reports Management
1. **Review Logbooks**: Go to Teacher Logbooks → Review submissions
2. **Review Workplans**: Go to Teacher Workplans → Evaluate term plans
3. **Approve/Reject**: Provide feedback and change status
4. **Track Progress**: Monitor submission and review statuses

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

#### Viewing Your Profile
1. Login with your teacher account
2. Click the "Teacher" bar in the sidebar
3. View your profile, including your name, assigned classes, subjects, and total students

#### Viewing Your Classes
1. Login with your teacher account
2. Navigate to "Classes" in the sidebar
3. View all your assigned classes with student counts and recent performance

#### Creating Reports
1. **Logbooks**: Go to Reports → Teacher Logbooks → Create New Logbook
   - Choose report type (daily, weekly, monthly)
   - Fill in detailed lesson information
   - Document challenges and solutions
   - Submit for review

2. **Workplans**: Go to Reports → Teacher Workplans → Create New Workplan
   - Select plan type (beginning, mid, end of term)
   - Define learning objectives
   - Plan teaching methods and timeline
   - Submit for academic master review

#### Analyzing Student Performance
1. Click "View Class Details & Results" on any class
2. See comprehensive student information
3. Review exam results and performance analytics
4. Track individual student progress

#### Dashboard Overview
- View real-time statistics
- Monitor class performance trends
- Access quick navigation to all features
- Track reports status and submissions

### Mobile Usage
- **Login**: Use the responsive login form optimized for mobile
- **Navigation**: Touch-friendly sidebar navigation
- **Data Entry**: Responsive forms that work on all screen sizes
- **Viewing**: Optimized layouts for mobile reading
- **Reports**: Create and submit reports directly from mobile

## 🏗️ Project Structure

```
edumanage/
├── myproject/
│   ├── edumanage/
│   │   ├── models.py          # Database models (including reports)
│   │   ├── views.py           # Application views (including reports)
│   │   ├── urls.py            # URL routing (including reports)
│   │   ├── admin.py           # Admin interface (including reports)
│   │   ├── forms.py           # Form definitions (responsive + reports)
│   │   ├── templates/         # HTML templates (mobile-responsive)
│   │   │   ├── account/       # Authentication templates
│   │   │   │   ├── login.html     # Responsive login form
│   │   │   │   ├── register.html  # Responsive registration form
│   │   │   │   ├── success.html   # Success pages
│   │   │   │   └── login_success.html
│   │   │   ├── reports/       # Reports system templates
│   │   │   │   ├── dashboard.html # Reports dashboard
│   │   │   │   ├── logbook_list.html # Logbook listing
│   │   │   │   ├── logbook_form.html # Logbook creation/editing
│   │   │   │   ├── logbook_detail.html # Logbook details
│   │   │   │   ├── logbook_review.html # Admin review
│   │   │   │   ├── workplan_list.html # Workplan listing
│   │   │   │   ├── workplan_form.html # Workplan creation/editing
│   │   │   │   ├── workplan_detail.html # Workplan details
│   │   │   │   └── workplan_review.html # Admin review
│   │   │   ├── dashboard.html # Dashboard template
│   │   │   ├── class.html     # Class management
│   │   │   ├── student.html   # Student listing
│   │   │   └── home.html      # Home page
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

### Reports System Models
- **TeacherLogbook**: Daily, weekly, and monthly teaching reports
- **TeacherWorkplan**: Beginning, mid, and end of term plans

### Key Features
- **Automatic Grade Calculation**: A+ to F based on percentage
- **Performance Analytics**: Class averages and trends
- **Data Validation**: Ensures data integrity
- **Relationship Management**: Proper foreign key relationships
- **Status Tracking**: Comprehensive workflow management
- **Review System**: Academic master approval process

## 🎨 User Interface

### Design Features
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Clean, professional interface using Tailwind CSS
- **Intuitive Navigation**: Easy-to-use sidebar navigation
- **Visual Feedback**: Color-coded performance indicators
- **Interactive Elements**: Hover effects and smooth transitions
- **Glass-Morphism**: Modern floating design with backdrop blur
- **Mobile-First**: Optimized for smartphone use
- **Consistent Blue Theme**: Professional color scheme throughout

### Color Scheme
- **Primary**: Blue (#0369a1) - Professional and trustworthy
- **Success**: Green - Good performance indicators
- **Warning**: Yellow - Average performance
- **Danger**: Red - Poor performance
- **Info**: Blue - General information
- **Consistent Branding**: Blue gradients throughout the application

### Responsive Breakpoints
- **Mobile**: < 1024px - Compact, space-efficient design
- **Desktop**: ≥ 1024px - Spacious, comfortable design
- **Automatic Adaptation**: Seamless transition between screen sizes
- **Mobile Optimizations**: Reduced padding and spacing for small screens

## 🔄 Recent Updates

### Latest Features Added
- **Complete Reports System**: Teacher logbooks and workplans with review workflow
- **Mobile Responsiveness**: Enhanced mobile experience with floating forms
- **Color Consistency**: Unified blue theme throughout the application
- **Admin Integration**: Full admin interface for reports management
- **Status Tracking**: Comprehensive workflow for report submission and review
- **Performance Analytics**: Enhanced student and class performance tracking
- **Teacher Profile View**: Teachers now have a dedicated profile page showing their name, assigned classes, subjects, and total students. Headmasters/admins can view all teachers' profiles and their classes. Teachers only see their own information for privacy and security.

### Mobile Improvements
- **Floating Form Design**: Modern glass-morphism authentication forms
- **Optimized Spacing**: Reduced gaps and padding for mobile screens
- **Touch-Friendly Interface**: Enhanced mobile navigation and interaction
- **Responsive Breakpoints**: Automatic adaptation between mobile and desktop
- **Form Height Optimization**: Reduced registration form height for mobile

### Technical Enhancements
- **Database Models**: New models for comprehensive reporting system
- **Form Validation**: Enhanced form handling with responsive styling
- **URL Routing**: Complete URL structure for reports system
- **Admin Customization**: Full admin interface for new models
- **Template System**: Responsive templates for all new features

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team
- Check the documentation for common solutions

---

**EduManage** - Empowering education through modern technology and responsive design. 
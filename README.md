**📝 Blog Application**
Live Demo: [https://abhinavsahoo.pythonanywhere.com/]
Currently deployed on PythonAnywhere (free plan, temporary).  
If the link is inactive, please run locally using the setup instructions below.


A Django-based blog application that allows users to create, manage, and search blog posts. It includes authentication, categories, dashboards, and role-based restrictions (e.g., managers cannot modify superuser accounts).


**🚀 Features**
User registration, login, and logout
Create, edit, and delete blog posts
Categorization of blogs
Search functionality across titles, descriptions, and content
Dashboard for managing users and posts
Role-based access control (superuser vs manager vs normal user)
Static and media file handling

**⚙️ Tech Stack**
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap (or your chosen framework)
Database: SQLite (default) or PostgreSQL/MySQL (production-ready)
Deployment: PythonAnywhere

**PROJECT STRUCTURE**
core/               # Main project settings
blogs/              # Blog app (models, views, templates)
dashboard/          # Dashboard app for user management
templates/          # Shared HTML templates
static/             # Static files (CSS, JS, images)
media/              # Uploaded media files

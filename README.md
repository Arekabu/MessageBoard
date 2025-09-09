# MessageBoard - Django Forum Application
A forum platform built with Django, Docker, Celery, and Redis.
## 🚀 Features

- User registration and authentication
- Forum posts and comments
- Email notifications
- Periodic tasks with Celery Beat
- Docker containerization
- Nginx reverse proxy
- Redis task queue

## 🛠️ Tech Stack

- **Backend:** Django 5.1.6, Python 3.10
- **Task Queue:** Celery 5.5.3, Redis
- **Web Server:** Gunicorn, Nginx
- **Database:** SQLite (development), PostgreSQL ready
- **Containerization:** Docker, Docker Compose

## 📦 Installation

### Prerequisites
- Docker
- Docker Compose
- Python 3.10+ (for local development)

### Docker Setup (Recommended)

**1. Clone the repository**
   
   ```bash
   git clone https://github.com/yourusername/MessageBoard.git
   cd MessageBoard
   ```

**2. Configure environment variables**

   ```
   cp .env.example .env
   # Edit .env with your settings
   ```

**3. Build and start containers**

   ```
   docker-compose up -d --build   
   ```

**4. Create superuser**

   ```
   docker-compose exec web python manage.py createsuperuser
   ```
 
**5. Access the application**

   - Web: http://localhost:8000
   - Admin: http://localhost:8000/admin
 

## Off-Campus Smart Auto Job Application & Recommendation System

This is a full-stack Django-based web application that:

- Automatically fetches off-campus job postings from external APIs
- Matches jobs with user skills and preferences
- Recommends relevant jobs to students
- Tracks job applications and statuses
- Provides admin tools for managing users, jobs, and basic analytics

### Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite (development), PostgreSQL (production)
- **Background Tasks**: Celery or cron jobs

### Local Setup (Quick Start)

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

More detailed deployment and configuration notes will be added as the project evolves.


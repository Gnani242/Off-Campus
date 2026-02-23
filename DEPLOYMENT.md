## Deployment Guide – Off-Campus Smart Job Portal

This project uses:

- **Backend**: Django (`ICET/jobportal`) – deploy to Render or Railway
- **Frontend**: Static HTML/JS (`ICET/frontend`) – deploy to Vercel
- **Database**: PostgreSQL

---

### 1. Backend (Render/Railway)

1. **Prepare repository**
   - Ensure `ICET/jobportal` contains:
     - `manage.py`
     - `jobportal/settings.py`
     - `requirements.txt` (one level up at `ICET/requirements.txt`)

2. **Create service**
   - Connect your GitHub repo.
   - **Root/Working directory**: `ICET/jobportal`
   - **Build command**:

     ```bash
     pip install -r ../requirements.txt
     python manage.py migrate
     python manage.py collectstatic --noinput
     ```

   - **Start command**:

     ```bash
     gunicorn jobportal.wsgi:application --bind 0.0.0.0:$PORT
     ```

3. **Environment variables**

   - `DJANGO_SECRET_KEY=your-strong-secret`
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS=your-backend-hostname`
   - `DEFAULT_FROM_EMAIL=noreply@yourdomain.com`
   - `DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DB_NAME`

4. **Post‑deploy steps**

   - Run `python manage.py createsuperuser` once (via shell on the host).
   - Visit `/admin/` to log in.

---

### 2. Frontend (Vercel)

1. **Create Vercel project**
   - Import the same GitHub repo.
   - In **Project Settings → General**:
     - **Root Directory**: `ICET/frontend`
   - In **Build & Output Settings**:
     - **Framework preset**: `Other`
     - **Build Command**: empty
     - **Output Directory**: `.`

2. **Configure API base URL**

   In `ICET/frontend/js/api.js`:

   ```js
   const API_BASE_URL = "https://your-backend.onrender.com";
   ```

3. **Deploy**

   - Trigger a deploy from Vercel.
   - Use the generated URL, e.g. `https://offcampus-jobportal.vercel.app/`.

---

### 3. CORS / Cookies (optional)

If you later protect APIs with strict auth from the frontend, you may need:

- Django CORS settings (`django-cors-headers`) to allow Vercel origin.
- HTTPS in production for secure cookies.


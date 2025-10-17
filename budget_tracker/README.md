# Personal Budget Tracker

A web app for tracking personal income and expenses with a Django backend and simple frontend.

## Features
- User authentication (register, login, logout).
- Manage transactions (add, edit, delete) with categories.
- View financial summary (income, expenses, balance).
- Filter transactions by date or category.
- Pie chart visualization of spending by category.
- Optional: Export transactions as CSV.

## Setup
1. Clone: `git clone https://github.com/YOUR_USERNAME/personal-budget-tracker.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up PostgreSQL:
   - Create database: `createdb budget_tracker_db`
   - Update `.env` with credentials (see `.env.example`).
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`

## API Endpoints
- POST /api/users/register/: Register a new user.
- POST /api/users/login/: Login and get JWT token.
- GET/PUT /api/users/profile/: View/update user profile.
- GET/POST /api/transactions/: List or create transactions.
- GET/PUT/DELETE /api/transactions/<id>/: Manage specific transaction.
- GET/POST /api/categories/: List or create categories.
- GET /api/reports/summary/: View income, expenses, balance.
- GET /api/reports/filter/: Filter transactions by date/category.
- GET /api/transactions/export/: Export transactions as CSV.

## Tech Stack
- Backend: Django, Django REST Framework
- Database: PostgreSQL
- Frontend: Django templates, Bootstrap, Chart.js
- Authentication: SimpleJWT

## Known Issues
- Pie chart requires page refresh to update.
- Limited error handling on frontend forms.
# finance_and_budget_tracker
A Django-based app for tracking personal income and expenses.

# Personal Budget Tracker

A Django REST API for tracking personal finances.

## Setup
1. Clone: `git clone https://github.com/YOUR_USERNAME/personal-budget-tracker.git`
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`

## API Docs
- Register: POST /api/users/register/
- ... (add more as implemented)

## Tech Stack
- Backend: Django, DRF
- DB: SQLite (dev), PostgreSQL (prod)

# Personal Budget Tracker

A Django REST API for tracking personal finances.

## Setup
1. Clone: `git clone https://github.com/YOUR_USERNAME/personal-budget-tracker.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up PostgreSQL database: Update `.env` with DB credentials.
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`

## API Endpoints
- **POST /api/users/register/**: Register a new user.
- **POST /api/users/login/**: Login and get JWT token.
- **GET/PUT /api/users/profile/**: View/update user profile.
- **GET/POST /api/transactions/**: List or create transactions.
- **GET/PUT/DELETE /api/transactions/<id>/**: Manage specific transaction.
- **GET/POST /api/categories/**: List or create categories.
- **GET /api/reports/summary/**: View income, expenses, balance.
- **GET /api/reports/filter/**: Filter transactions by date/category.

## Tech Stack
- Backend: Django, Django REST Framework
- Database: PostgreSQL
- Authentication: SimpleJWT
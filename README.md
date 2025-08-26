# Inventory Management API

A Django REST Framework (DRF) project that provides APIs for managing products, locations, stock moves, vendors, and inventory snapshots.
Authentication is handled with **JWT (SimpleJWT)**, and **Swagger/OpenAPI** is enabled for API documentation.

---

## Features

* Product, Location, Vendor, Address, StockMove, and InventorySnapshot models
* CRUD APIs using DRF `ModelViewSet`
* JWT Authentication with access & refresh tokens
* Automatic inventory snapshot updates after stock moves
* Swagger UI & ReDoc for interactive API docs
* PostgreSQL (production) / SQLite (local dev)

---

## Prerequisites

* Python **3.10+**
* pip (Python package manager)
* PostgreSQL (for production) or SQLite (default for dev)
* (Optional) Docker & Docker Compose

---

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/inventory-api.git
cd inventory-api
```

### Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

### Setup Environment Variables

Create a `.env` file in the root directory:

```ini
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=dima
DATABASE_USER=dima
DATABASE_PASSWORD=dima
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

API will be available at:
 `http://127.0.0.1:8000/api/`

---

##  Authentication (JWT)

* **Get Token Pair**
  `POST /api/token/`

  ```json
  {
    "username": "your-username",
    "password": "your-password"
  }
  ```
* **Refresh Token**
  `POST /api/token/refresh/`

Add the token to requests:

```
Authorization: Bearer <your_access_token>
```

---

## API Documentation

* Swagger UI:  `http://127.0.0.1:8000/swagger/`
* ReDoc:  `http://127.0.0.1:8000/redoc/`

---

## Run with Docker (Optional)

```bash
docker-compose up --build
```

---

## Project Structure

```
MSInventory/
│── inventory/          # Main app (models, views, serializers, urls)
│── MSInvetory/            # Django project config
│── requirements.txt    # Dependencies
│── manage.py
│── README.md
│── .env.example
```


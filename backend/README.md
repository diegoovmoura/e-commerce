# Backend E-commerce Platform

This is the backend part of the e-commerce platform built using FastAPI, following Clean Architecture principles. It provides a RESTful API for managing products, users, vendors, carts, wishlists, and authentication.

## Project Structure

```
backend/
├── app/
│   ├── api/                # Routers/controllers (HTTP endpoints)
│   │   └── routes.py
│   ├── auth/               # Authentication logic (JWT, password hashing)
│   │   ├── controller.py
│   │   ├── dependencies.py
│   │   ├── service.py
│   │   ├── utils.py
│   │   ├── model.py
│   │   └── schemas.py
│   ├── entities/           # SQLAlchemy models (User, Product, Cart, Wishlist, etc.)
│   ├── repositories/       # Database access logic (CRUD)
│   ├── schemas/            # Pydantic schemas for validation/serialization
│   ├── services/           # Business logic (product_service.py, etc.)
│   ├── utils/              # Shared utilities (db.py, etc.)
│   └── main.py             # FastAPI entry point
├── requirements.txt
└── README.md
```

## Key Features

- **Clean Architecture:** Separation of concerns with routers, services, repositories, models, and schemas.
- **Authentication:** JWT-based authentication with secure password hashing.
- **Product Management:** CRUD operations for products.
- **Vendor Support:** Products are linked to vendors; only existing vendors can have products.
- **User Cart & Wishlist:** Each user has a cart and can have a wishlist, both as separate entities.
- **Extensible:** Easily add new features (orders, payments, etc.) by following the established structure.

## Setup

1. **Clone the repository and navigate to the backend folder:**
    ```sh
    cd ecommerce-platform
    cd backend
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file with your `DATABASE_URL`, `SECRET_KEY`, etc.

5. **Run the backend server:**
    ```sh
    uvicorn app.main:app --reload
    ```

## API Endpoints

- `POST /api/products/` — Create a new product
- `GET /api/products/` — List products
- `GET /api/products/{product_id}` — Get product by ID
- `POST /auth/login` — User login (returns JWT token)
- (Add more endpoints for users, vendors, carts, wishlists, etc.)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

**This backend is designed for scalability, maintainability, and professional development.**
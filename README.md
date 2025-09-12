# Backend E-commerce Platform

This is the backend part of the e-commerce platform built using FastAPI. It provides a RESTful API for managing products and handling requests from the frontend application.

## Project Structure

```
backend/
├── app/
│   ├── main.py               # Entry point for the FastAPI application
│   ├── api/
│   │   └── routes.py         # API routes for product management
│   ├── models/
│   │   └── product.py         # Product model definition
│   ├── schemas/
│   │   └── product_schema.py   # Pydantic schemas for product validation
│   └── utils/
│       └── db.py             # Database utility functions
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation for the backend
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ecommerce-platform/backend
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

## API Usage

### Products

- **Get all products**
  - **Endpoint:** `GET /api/products`
  - **Description:** Retrieve a list of all products.

- **Get a product by ID**
  - **Endpoint:** `GET /api/products/{id}`
  - **Description:** Retrieve a specific product by its ID.

- **Create a new product**
  - **Endpoint:** `POST /api/products`
  - **Description:** Add a new product to the database.

- **Update a product**
  - **Endpoint:** `PUT /api/products/{id}`
  - **Description:** Update an existing product by its ID.

- **Delete a product**
  - **Endpoint:** `DELETE /api/products/{id}`
  - **Description:** Remove a product from the database.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
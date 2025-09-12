# E-commerce Platform

This is a full-stack e-commerce platform built using FastAPI for the backend and Next.js for the frontend. 

## Project Structure

```
ecommerce-platform
├── backend
│   ├── app
│   │   ├── main.py          # Entry point for the FastAPI application
│   │   ├── api
│   │   │   └── routes.py    # API routes for product management
│   │   ├── models
│   │   │   └── product.py    # Product model definition
│   │   ├── schemas
│   │   │   └── product_schema.py # Pydantic schemas for product validation
│   │   └── utils
│   │       └── db.py        # Database utility functions
│   ├── requirements.txt      # Backend dependencies
│   └── README.md             # Documentation for the backend
├── frontend
│   ├── pages
│   │   ├── index.tsx        # Homepage component
│   │   └── products.tsx     # Products listing component
│   ├── components
│   │   └── ProductCard.tsx   # Product card component
│   ├── public                # Static assets
│   ├── package.json          # Frontend dependencies and scripts
│   ├── tsconfig.json         # TypeScript configuration
│   └── README.md             # Documentation for the frontend
└── README.md                 # Overall project documentation
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required dependencies:
   ```
   npm install
   ```
3. Run the Next.js application:
   ```
   npm run dev
   ```

## Usage

- The backend API will be available at `http://localhost:8000`.
- The frontend application will be available at `http://localhost:3000`.

This project is designed to be a starting point for building a more comprehensive e-commerce platform. You can extend the functionality by adding more features such as user authentication, payment processing, and more.
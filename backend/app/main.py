from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as product_router
from app.api.product_controller import router as new_product_router  # add this
from app.auth.controller import router as auth_router

# Import all models to ensure they are registered with SQLAlchemy
from app.entities import product, user, business, cart, cart_item
from app.utils.db import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce API", description="A FastAPI e-commerce platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router, prefix="/api/products", tags=["products"])
app.include_router(new_product_router, prefix="/api/v2/products", tags=["products-v2"]) 
app.include_router(auth_router, prefix="/auth", tags=["authentication"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
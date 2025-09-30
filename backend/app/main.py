from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as product_router
from app.api.product_controller import router as new_product_router
from app.api.cart_controller import router as cart_router
from app.api.business_controller import router as business_router
from app.auth.controller import router as auth_router
from app.entities import product, user, business, cart, cart_item
from app.utils.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-commerce API", 
    description="A FastAPI e-commerce platform",
    swagger_ui_parameters={
        "persistAuthorization": True,
    }
)

# Configure JWT authentication for Swagger UI
app.openapi_schema = None

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    from fastapi.openapi.utils import get_openapi
    
    openapi_schema = get_openapi(
        title="E-commerce API",
        version="1.0.0",
        description="A FastAPI e-commerce platform with JWT authentication",
        routes=app.routes,
    )
    
    # Add JWT Bearer authentication scheme
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Enter JWT token (without 'Bearer' prefix)"
        }
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router, prefix="/api/products", tags=["products"])
app.include_router(new_product_router, prefix="/api/v2/products", tags=["products-v2"]) 
app.include_router(cart_router, prefix="/api", tags=["cart"])
app.include_router(business_router, prefix="/api", tags=["business"])
app.include_router(auth_router, prefix="/auth", tags=["authentication"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
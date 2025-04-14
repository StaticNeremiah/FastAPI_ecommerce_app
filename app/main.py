from fastapi import FastAPI
from app.routers import category, products, auth

app = FastAPI(title='FastAPI e-commerce test application')


@app.get("/")
async def welcome() -> dict:
    return {'message': 'Welcome to the FastAPI application!'}

app.include_router(category.router)
app.include_router(products.router)
app.include_router(auth.router)

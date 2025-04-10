from fastapi import FastAPI
from app.routers import category, products

app = FastAPI(title='FastAPI e-commerce test application')


@app.get("/")
async def welcome() -> dict:
    return {'message': 'Welcome to the FastAPI application!'}

app.include_router(category.router)
app.include_router(products.router)

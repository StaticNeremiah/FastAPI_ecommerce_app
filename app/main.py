from fastapi import FastAPI
import uvicorn
from app.routers import category, products, auth, permission

app = FastAPI(title='FastAPI e-commerce test application')


@app.get("/")
async def welcome() -> dict:
    return {'message': 'Welcome to the FastAPI application!'}

app.include_router(category.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(permission.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

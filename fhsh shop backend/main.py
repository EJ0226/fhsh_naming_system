from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.user import router as user
from router.cart import router as cart
from router.admin import router as admin
from router.products import router as products
from router.item import router as item

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(cart)
app.include_router(admin)
app.include_router(products)
app.include_router(item)
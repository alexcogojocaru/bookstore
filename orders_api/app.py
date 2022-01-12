from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

import pydantic
import uvicorn


class Order(pydantic.BaseModel):
    isbn: str = None
    title: str = None
    price: Optional[float] = None
    quantity: Optional[int] = 1
    status: str = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class OrdersAPI:
    @app.put('/api/orders')
    async def place_order(orderinfo: Order):
        return orderinfo

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8001)
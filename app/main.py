from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="PCBVision API",
    version="0.1.0",
    description="API for detecting defects in printed circuit board images.",
)

app.include_router(router)
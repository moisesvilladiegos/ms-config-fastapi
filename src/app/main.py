from fastapi.applications import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.parking_space.infraestructure.router import parking_space_router
from src.app.rate.infraestructure.router import rate_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(parking_space_router.router, prefix="/api")
app.include_router(rate_router.router, prefix="/api")

@app.get("/api/config/status")
async def root():
    return {"message": "Hello Bigger Applications!"}
from fastapi import APIRouter

from api.v1.endpoints import frase

api_router = APIRouter()
api_router.include_router(frase.router, prefix="/frase", tags=["frases"])
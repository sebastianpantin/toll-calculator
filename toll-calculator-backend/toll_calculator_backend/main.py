from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from toll_calculator_backend.config.settings import get_settings

settings = get_settings()

app = FastAPI(
    debug=bool(settings.DEBUG),
    title=settings.NAME,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

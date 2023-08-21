from fastapi import FastAPI
from src.api.users_api import user_roouter

app = FastAPI()
app.include_router(user_roouter)
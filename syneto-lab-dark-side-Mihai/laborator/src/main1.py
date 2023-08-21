from fastapi import FastAPI
from src.api.users_api import user_roouter
from src.api.cocktails import cocktail_router
from src.api.finance import finance_router

app = FastAPI()
app.include_router(user_roouter)
app.include_router(cocktail_router)
app.include_router(finance_router)
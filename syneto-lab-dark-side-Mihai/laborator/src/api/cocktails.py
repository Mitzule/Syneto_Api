from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import src.call_apis as call_apis
import requests
import json

cocktail_router = APIRouter(prefix="/cocktail")

url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"

@cocktail_router.get("/GetCocktails")
async def getCocktails():
    pass

@cocktail_router.get("/(search)")
async def getImage():
    return FileResponse("margarita.jpg")
    
    
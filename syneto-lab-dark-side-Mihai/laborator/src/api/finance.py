import json
import logging
import random
import sys
from datetime import datetime
from typing import Iterator

import asyncio
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.requests import Request

import plotly.graph_objs as go
import yfinance as yf
from fastapi.responses import FileResponse

random.seed()  

finance_router = APIRouter(prefix="/finance")
app = FastAPI()

# @finance_router.get("/", response_class=HTMLResponse)
# async def index(request: Request) -> templates.TemplateResponse:
#     return templates.TemplateResponse("index.html", {"request": request})

async def generate_random_data(request: Request):
    """
    Generates random value between 0 and 100

    :return: String containing current timestamp (YYYY-mm-dd HH:MM:SS) and randomly generated data.
    """
    client_ip = request.client.host
    ok = 0
    while ok:
        json_data = json.dumps(
            {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "value": random.random() * 100,
            }
        )
        print(json_data)
        yield f"data:{json_data}\n\n"
        await asyncio.sleep(1)

#modifici pentru perioada sa fie days, weeks,years etc

@finance_router.get("/generate_chart")
async def generate_chart(tickers : str, period : str, interval : str):
    data = yf.download(tickers = tickers, period = period, interval = interval, rounding= True)
    # print(data)
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index, open = data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name = 'market data'))
    fig.update_layout(title = 'Google share price', yaxis_title = 'Stock Price (USD)')
    fig.write_image('stock.jpg')
    # fig.show()
    return FileResponse("stock.jpg")
    


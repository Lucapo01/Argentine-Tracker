from unicodedata import name
from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy import JSON
import core.schemas.schemas as _schemas
import core.services.services as _services
import sqlalchemy.orm as _orm
from typing import Dict, List
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# FIX Security Breach
@app.post("/createTicker", response_model=_schemas.Ticker)
async def createTicker(ticker: _schemas.createTicker, db: _orm.Session = Depends(_services.get_db)):
    db_ticker = _services.get_ticker_by_name(db=db, name=ticker.name)
    if db_ticker:
        raise HTTPException(
            status_code=400, detail="Ticker already in Database."
        )
    return _services.create_ticker(db=db, ticker=ticker)


@app.get("/tickers/")
def read_users(
    db: _orm.Session = Depends(_services.get_db),
):
    tickers = _services.get_tickers(db=db)
    response = {}
    for ticker in tickers:
        response[ticker.id] = ticker.name
    return response


@app.get("/tickers/{ticker_id}", response_model=_schemas.Ticker)
def read_user(ticker_id: int, db: _orm.Session = Depends(_services.get_db)):
    db_ticker = _services.get_ticker(db=db, id=ticker_id)
    if db_ticker is None:
        raise HTTPException(
            status_code=404, detail="This Ticker does not exist."
        )
    return db_ticker

@app.post("/engineUpdate/{password}")
async def update_engine(password: str, request: Request, db: _orm.Session = Depends(_services.get_db)):
    print(password)
    payload = await request.json()
    _services.update_ticker(db=db, ticker=_schemas.createTicker(name="test_ticker", funds= payload, price=2, type="1"))

# -------------------------------------------------------------------
# PLAYGROUND
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# RUN
# -------------------------------------------------------------------

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, loop="asyncio")
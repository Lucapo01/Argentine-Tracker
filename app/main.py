from fastapi import FastAPI, Depends, HTTPException
import core.schemas.schemas as _schemas
import core.services.services as _services
import sqlalchemy.orm as _orm
from typing import List

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


@app.get("/tickers/", response_model=List[_schemas.Ticker])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: _orm.Session = Depends(_services.get_db),
):
    tickers = _services.get_tickers(db=db, skip=skip, limit=limit)
    return tickers


@app.get("/tickers/{ticker_id}", response_model=_schemas.Ticker)
def read_user(ticker_id: int, db: _orm.Session = Depends(_services.get_db)):
    db_ticker = _services.get_ticker(db=db, id=ticker_id)
    if db_ticker is None:
        raise HTTPException(
            status_code=404, detail="This Ticker does not exist."
        )
    return db_ticker


# -------------------------------------------------------------------
# PLAYGROUND
# -------------------------------------------------------------------
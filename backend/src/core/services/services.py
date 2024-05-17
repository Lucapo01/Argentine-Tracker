from ..schemas import schemas as _schemas
from typing import List
from ..database.mongo.tickers import TickersDatabase
# from ..database import database as _database
# from ..models import models as _models
# import sqlalchemy.orm as _orm


def get_db():
    db = TickersDatabase()
    return db

# def get_old_db():
#     db = _database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# def get_old_tickers(db: _orm.Session) -> List[_models.Ticker]:
#     return db.query(_models.Ticker).all()

async def get_ticker(db: TickersDatabase, id: int):
    return await db.get(id)


async def get_ticker_by_name(db: TickersDatabase, name: str):
    return await db.get_by_name(name)


async def get_tickers(db: TickersDatabase) -> List[_schemas.Ticker]:
    return await db.get_all()


async def create_ticker(db: TickersDatabase, ticker: _schemas.Ticker):
    return await db.create(ticker)

async def update_ticker(db: TickersDatabase, ticker: _schemas.Ticker):
    return await db.update(ticker)

async def delete_ticker_by_name(db: TickersDatabase, name: str):
    return await db.delete_by_name(name)

from typing import List
import sqlalchemy.orm as _orm

from ..schemas.schemas import HotColdItem
from ..services import services as db_services

def get_hot_cold_items(db: _orm.Session) -> List[HotColdItem]:
    tickers = db_services.get_tickers(db=db)
    items = []
    for ticker in tickers:
        if len(ticker.funds["total"]["qty"]) > 2:
            prev_week_qty = ticker.funds["total"]["qty"][-2]
            this_week_qty = ticker.funds["total"]["qty"][-1]
            delta = (this_week_qty - prev_week_qty) / (prev_week_qty) if prev_week_qty else 0
            items.append(
                HotColdItem(
                    id=ticker.id,
                    name=ticker.name,
                    delta=delta,
                )
            )
    return items

def get_hots(db: _orm.Session, limit: int = 5) -> List[HotColdItem]:
    items = get_hot_cold_items(db)
    sorted_items = sorted(items, key=lambda x: x.delta, reverse=True)
    return sorted_items[:limit]

def get_colds(db: _orm.Session, limit: int = 5) -> List[HotColdItem]:
    items = get_hot_cold_items(db)
    sorted_items = sorted(items, key=lambda x: x.delta)
    return sorted_items[:limit]
    

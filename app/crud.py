from typing import List
from fastapi import HTTPException


from app.database import items_db
from app.models import Item, ItemCreate, ItemUpdate

from bisect import bisect_left


def get_items(min_price: float = 0.0) -> List[Item]:
    return [Item(**item) for item in items_db if item["price"] >= min_price] # change <= for >=


def create_item(item: ItemCreate) -> Item:
    new_id = max(item["id"] for item in items_db) + 1
    new_item = {"id": new_id, **item.dict()}
    items_db.append(new_item)
    return Item(**new_item)


def update_item_by_id(item_id: int, update: ItemUpdate) -> Item | None:

 # check if duplication happened
    if update.name:
        if any(
            i["name"].lower() == update.name.lower() and i["id"] != item_id
            for i in items_db
        ):
            raise HTTPException(status_code=400, detail="Duplicate item name")

    # apply changes

    for item in items_db:
        if item["id"] == item_id:
            if update.name:
                item["name"] = update.name
            if update.price:
                item["price"] = update.price
            return Item(**item)
    return None





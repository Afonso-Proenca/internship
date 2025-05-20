from typing import List
from fastapi import HTTPException


from app.database import items_db
from app.models import Item, ItemCreate, ItemUpdate

from bisect import bisect_left

 # task 2 - The /items endpoint does not behave correctly when filtering by min_price. Investigate and fix the logic.

def get_items(min_price: float = 0.0) -> List[Item]:
    return [Item(**item) for item in items_db if item["price"] >= min_price] # change <= for >=   


def create_item(item: ItemCreate) -> Item:
    new_id = max(item["id"] for item in items_db) + 1
    new_item = {"id": new_id, **item.model_dump()}
    items_db.append(new_item)
    return Item(**new_item)


# task 5 done There is an edge case involving duplicate item names when updating an item. This case is not properly handled and could cause inconsistencies.

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





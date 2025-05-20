from typing import List
from fastapi import HTTPException


from app.database import (
    items_db,
    items_by_price,
    prices_sorted,
    insert_sorted,
    remove_sorted,
)

from app.models import Item, ItemCreate, ItemUpdate

from bisect import bisect_left

 # task 2 - The /items endpoint does not behave correctly when filtering by min_price. Investigate and fix the logic.

#def get_items(min_price: float = 0.0) -> List[Item]:
 #   return [Item(**item) for item in items_db if item["price"] >= min_price] # change <= for >=   

def get_items(min_price: float = 0.0) -> List[Item]:
    idx = bisect_left(prices_sorted, min_price)
    return [Item(**it) for it in items_by_price[idx:]]


def create_item(item: ItemCreate) -> Item:
    # duplicate‐name guard
    if any(i["name"].lower() == item.name.lower() for i in items_db):
        raise HTTPException(400, "Duplicate item name")

    new_id = max(i["id"] for i in items_db) + 1
    new_item = {"id": new_id, **item.model_dump()}

    # add to both structures
    items_db.append(new_item)
    insert_sorted(new_item)

    return Item(**new_item)



# task 5 done There is an edge case involving duplicate item names when updating an item. This case is not properly handled and could cause inconsistencies.

def update_item_by_id(item_id: int, update: ItemUpdate) -> Item | None:
    # duplicate name preventoion (Task 5)
    if update.name and any(
        i["name"].lower() == update.name.lower() and i["id"] != item_id
        for i in items_db
    ):
        raise HTTPException(400, "Duplicate item name")

    for item in items_db:
        if item["id"] == item_id:
            # if price is changing, keep index in sync
            if update.price is not None:
                remove_sorted(item)

            if update.name is not None:
                item["name"] = update.name
            if update.price is not None:
                item["price"] = update.price

            # re-insert into index if price changed
            if update.price is not None:
                insert_sorted(item)

            return Item(**item)

    return None




import json
from pathlib import Path
from bisect import bisect_left, insort


path = Path(__file__).parent / "items_db.json"
with path.open("r") as f:
    items_db = json.load(f)


# task 4 - The /items endpoint exhibits performance issues as the item list grows. Consider the current implementation and propose improvements.


# Build a secondary in-memory index ordered by price


# items_by_price holds the same dicts as items_db, but sorted by price.

items_by_price: list[dict] = sorted(items_db, key=lambda x: x["price"])

# prices_sorted is just the list of their prices – used for bisect.

prices_sorted: list[float] = [it["price"] for it in items_by_price]


def insert_sorted(item: dict) -> None:
    """
    Insert `item` into both `items_by_price` and `prices_sorted`, preserving order.
    Should be called any time i append or update an entry in items_db.
    """
    # Find insertion index in the price list
    idx = bisect_left(prices_sorted, item["price"])

    # Insert price and item at the same position

    prices_sorted.insert(idx, item["price"])
    items_by_price.insert(idx, item)


def remove_sorted(item: dict) -> None:
    """
    Remove `item` from both `items_by_price` and `prices_sorted`.
    Useful when you know an item's price has changed and i need to
    re-insert it (see update flow).
    """
    # Locate by matching both price and identity
    # if prices repeat, this ensures the correct dict is removed

    for idx, existing in enumerate(items_by_price):
        if existing["id"] == item["id"]:
            prices_sorted.pop(idx)
            items_by_price.pop(idx)
            return
        
    # If we didn't find it, the operation does not proceed (shouldn't normally happen)
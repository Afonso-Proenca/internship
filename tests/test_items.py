# testing command : pytest -q 


from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_min_price_filter() -> None:
    response = client.get("/items?min_price=4")
    assert all(item["price"] >= 4 for item in response.json())


def test_short_name() -> None:
    response = client.post("/items", json={"name": "ab", "price": 5})
    assert response.status_code == 422


def test_update_to_duplicate_name() -> None:
    client.post("/items", json={"name": "Grape", "price": 6})
    resp = client.put("/items/1", json={"name": "Grape"})
    assert resp.status_code == 400 or resp.status_code == 422


def test_item_name_consistency() -> None:
    # Call the /items endpoint
    response = client.get("/items")
    assert response.status_code == 200

    # Extract just the names
    names = [item["name"] for item in response.json()]

    # Ensure the list is not empty
    assert names, "The items list should not be empty"

    # Check that at least one name ends with "500000"
    assert any(n.endswith("500000") for n in names), (
        "There should be at least one item whose name ends with '500000'"
    )
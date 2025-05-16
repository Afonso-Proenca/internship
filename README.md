# Internship Technical Assignment

## Overview
This is a small FastAPI application that provides a basic REST API for managing items. The codebase contains several bugs of varying difficulty. Your task is to fix the identified issues, ensure tests pass, and submit a pull request with your changes.

We're looking for clean code, clear thinking, and effective communication of your solution.

---

## Setup Instructions
-create venv: python -m venv .venv
              .venv\Scripts\Activate.ps1

### Requirements
- Python 3.11+
- `pip` or `poetry` (we recommend `pip` for simplicity)

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the app
```bash
uvicorn app.main:app --reload
```

### Run tests
```bash
pytest
```

---

## Project Structure
```
.
├── app
│   ├── main.py
│   ├── models.py
│   ├── crud.py
│   └── database.py
├── tests
│   └── test_items.py
├── requirements.txt
└── README.md
```

---

## Tasks Summary
There are six issues embedded in this codebase. Some are obvious, while others are subtle or hinted at via failing tests or unexpected behavior. Your job is to investigate, identify the root causes, and fix them. We encourage you to think critically and communicate your reasoning in the pull request.

**Task 1:** There is a typo in one of the route paths. Find and correct it.

**Task 2:** The `/items` endpoint does not behave correctly when filtering by `min_price`. Investigate and fix the logic.

**Task 3:** Item creation currently allows names that are too short. Review the expected behavior, minimum of three characters, and add appropriate validation.

**Task 4:** The `/items` endpoint exhibits performance issues as the item list grows. Consider the current implementation and propose improvements.

**Task 5:** There is an edge case involving duplicate item names when updating an item. This case is not properly handled and could cause inconsistencies.

**Task 6:** One test assumes a specific item exists in the large dataset. This creates fragility and reflects poor test design. Improve the test to ensure robustness without relying on hardcoded assumptions.

---

## Submission Instructions
1. Fork this repository.
2. Create a new branch from `main` for your changes.
3. Fix the issues mentioned.
4. Commit frequently with descriptive messages.
5. Push your branch and open a pull request.
6. Ensure all tests pass and any added tests cover edge cases.

We look forward to discussing your solution in the interview!

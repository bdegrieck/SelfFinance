from fastapi import FastAPI, HTTPException
import datetime as dt
from src.managers.source_manager.entrypoint import create_sourcedata_service
from src.managers.source_manager.domain import GroceriesExpense

app = FastAPI()
service = create_sourcedata_service()

@app.get("/")
def read_root():
    return {"message": "SelfFinance API"}

@app.post("/groceries")
def add_groceries(expense: GroceriesExpense):
    service.insert_groceries(groceries=expense)
    return {"status": "ok"}

@app.get("/groceries/{date}")
def get_groceries(date: str):
    try:
        dt_date = dt.datetime.fromisoformat(date)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="Invalid date format") from exc
    groceries = service.get_groceries_by_date(date=dt_date)
    if not groceries:
        raise HTTPException(status_code=404, detail="Groceries not found")
    return groceries

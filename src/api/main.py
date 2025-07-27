from fastapi import FastAPI, HTTPException
import datetime as dt
from src.managers.source_manager.entrypoint import create_sourcedata_service
from src.managers.source_manager.domain import GroceriesExpense, Login

app = FastAPI()
service = create_sourcedata_service()

@app.get("/")
def read_root():
    return {"message": "SelfFinance API"}

@app.post("/login")
def login(login_data: Login):
    """Handle user login authentication."""
    try:
        # Get the stored login record for this username
        stored_login = service.get_login_by_username(username=login_data.username)
        
        if not stored_login:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        
        # Check if password matches (assuming passwords are hashed)
        if stored_login.password != login_data.password:  # In production, use proper password hashing
            raise HTTPException(status_code=401, detail="Invalid username or password")
        
        return {
            "status": "success",
            "message": "Login successful",
            "username": login_data.username
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login failed: {str(e)}")

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

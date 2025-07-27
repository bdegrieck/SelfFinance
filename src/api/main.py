from fastapi import FastAPI, HTTPException
import datetime as dt
from src.managers.source_manager.entrypoint import create_selfFinance_service
from src.managers.source_manager.domain import GroceriesExpense, Login

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SelfFinance API"}

@app.post("/create-user")
def login(login_data: Login):
    """Handle user login authentication."""
    try:
        # Get the stored login record for this username
        finance_service = create_selfFinance_service()
        
        return {
            "status": "success",
            "message": "Login successful",
            "username": login_data.username
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login failed: {str(e)}")


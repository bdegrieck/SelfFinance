from fastapi import FastAPI, HTTPException
import datetime as dt
from src.managers.source_manager.entrypoint import create_selfFinance_service
from src.managers.source_manager.domain import CreateUser, GroceriesExpense, Login
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "SelfFinance API"}

@app.post("/create-user")
def login(new_user_info: CreateUser):
    """Handle user login authentication."""
    try:
        # Get the stored login record for this username
        finance_service = create_selfFinance_service()
        
        return {
            "status": "success",
            "message": "Login successful",
            "username": "ben"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login failed: {str(e)}")


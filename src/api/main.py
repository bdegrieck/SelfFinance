from fastapi import FastAPI, HTTPException
import datetime as dt
from src.managers.source_manager.entrypoint import create_selfFinance_service
from src.managers.source_manager.domain import User, GroceriesExpense, Login
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
def UserResourcePost(new_user_info: User):
    """Handle user login authentication."""
    try:
        # Get the stored login record for this username
        finance_service = create_selfFinance_service()
        finance_service.insert_new_user(new_user_info)
        
        return {
            "status": "success",
            "data": None,
            "message": "Login successful",
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login failed: {str(e)}")



app.post("/login")
def UserResourcePost(login_info: Login):
    """Handle user login authentication."""
    finance_service = create_selfFinance_service()
    login_user_info = finance_service.get_login_by_username(username=login_info.username)

    if login_user_info is None:
        raise HTTPException(
            status_code=404,
            detail=f"No user found for username: {login_info.username}."
        )

    if login_user_info.password != login_info.password:
        raise HTTPException(
            status_code=401,
            detail=f"Could not authenticate user {login_info.username} with invalid password."
        )

    return {
        "status": "success",
        "data": None,
        "message": "Login successful",
    }
from fastapi import FastAPI, HTTPException
import datetime as dt
from src.api.constants import HttpStatus
from src.managers.source_manager.entrypoint import create_selfFinance_service
from src.managers.source_manager.domain import User, GroceriesExpense, Login, CreateUser
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
def UserResourcePost(new_user_info: CreateUser):
    """Handle user login authentication."""
    try:
        # Get the stored login record for this username
        finance_service = create_selfFinance_service()
        finance_service.insert_new_user(new_user_info)
        
        return {
            "status": "success",
            "data": None,
            "message": "User created successfully",
            "status_code": HttpStatus.created
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login failed: {str(e)}")



@app.post("/login-user")
def UserResourcePost(login_info: Login):
    """Handle user login authentication."""
    finance_service = create_selfFinance_service()
    login_user_info: User = finance_service.get_login_by_username(username=login_info.username)

    if login_user_info is None:
        raise HTTPException(
            status_code=HttpStatus.not_found,
            detail=f"User not found for: {login_info.username}."
        )

    if login_user_info.password != login_info.password:
        raise HTTPException(
            status_code=HttpStatus.unauthorized,
            detail=f"Could not authenticate user: {login_info.username} with invalid password."
        )

    return {
        "status": "success",
        "data": {
            "username": login_user_info.username,
            # Add other safe user fields here if needed
            # "email": login_user_info.email,
            "first_name": login_user_info.first_name,
        },
        "message": "Login successful",
        "status_code": HttpStatus.ok
    }


@app.get("/get-monthly-expenses")
def get_monthly_expenses(date: dt.datetime):
    finance_service = create_selfFinance_service()
    monthly_expenses = finance_service.get_monthly_expenses(date)
    return monthly_expenses


from fastapi import FastAPI

from app.database import engine, Base
from app.models import User, Expense

from app.routes.user import router as user_router
from app.routes.auth import router as auth_router
from app.routes.expense import router as expense_router
from app.routes.report import router as report_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(expense_router)
app.include_router(report_router)


@app.get("/")
def home():
    return {"message": "Expense tracker Api"}

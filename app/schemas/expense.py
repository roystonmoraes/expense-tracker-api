from pydantic import BaseModel
from datetime import date


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    expense_date: date


class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    expense_date: date
    user_id: int

    class Config:
        from_attributes = True

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from sqlalchemy import extract, func


from app.database import get_db

from app.models.expense import Expense
from app.models.user import User

from app.auth.oauth2 import get_current_user

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/monthly-summary")
def monthly_summary(
    month: int,
    year: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    total = (
        db.query(func.sum(Expense.amount))
        .filter(
            Expense.user_id == current_user.id,
            extract("month", Expense.expense_date) == month,
            extract("year", Expense.expense_date) == year,
        )
        .scalar()
    )

    return {"month": month, "year": year, "total_expenses": total or 0}

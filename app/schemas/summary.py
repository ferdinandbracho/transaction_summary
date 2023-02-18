from pydantic import BaseModel
from typing import Dict

class SummaryItem(BaseModel):
    total_balance: float
    avg_debit: float
    avg_credit: float
    month_transactions: Dict

    class Config:
        orm_mode = True
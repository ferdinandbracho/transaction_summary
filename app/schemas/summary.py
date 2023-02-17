from pydantic import BaseModel
from typing import List

class Summary(BaseModel):
    total_balance: float
    avg_debit: float
    avg_credit: float
    transactions_month: List
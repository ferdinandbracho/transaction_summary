from pydantic import BaseModel
from typing import Dict

class Summary(BaseModel):
    total_balance: float
    avg_debit: float
    avg_credit: float
    month_transactions: Dict
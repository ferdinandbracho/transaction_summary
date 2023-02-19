from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime

class SummaryItem(BaseModel):
    id: int
    user_email: Optional[str]
    total_balance: float
    avg_debit: float
    avg_credit: float
    month_transactions: Dict
    created_at: datetime

    class Config:
        orm_mode = True
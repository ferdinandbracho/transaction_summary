from sqlalchemy import Column, Float, Integer
from typing import List
from app.db.session import Base

class Summary(Base):
    __tablename__ = 'summary'

    id = Column(Integer, primary_key=True, index=True)

    total_balance = Column(Float, nullable=False)

    avg_debit = Column(Float, nullable=False)

    avg_credit = Column(Float, nullable=False)

    transactions_month = Column(List, nullable=False)
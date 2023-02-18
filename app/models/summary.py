from sqlalchemy import Column, Float, Integer, PickleType
from app.db.session import Base

class Summary(Base):
    __tablename__ = 'summary'

    id = Column(Integer, primary_key=True, index=True)

    total_balance = Column(Float, nullable=False)

    avg_debit = Column(Float, nullable=False)

    avg_credit = Column(Float, nullable=False)

    month_transactions = Column(PickleType, nullable=False)

    def __repr__(self) -> str:
        return f'''Summary(
            id={self.id},
            total_balance={self.total_balance},
            avg_debit={self.avg_debit},
            avg_credit={self.avg_credit},
            month_transactions={self.month_transactions},
        )'''
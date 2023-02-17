from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import app.config as config

# Init Engine
engine = create_engine(
    config.DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create Session
SessionLocal = sessionmaker(autocommit=False, bind=engine)

# Init base
Base = declarative_base()

# Database dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
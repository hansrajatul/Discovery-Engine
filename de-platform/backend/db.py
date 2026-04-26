from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://kde:kde@postgres:5432/kde"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

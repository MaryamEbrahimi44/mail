from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create a dependency function that can return a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_engine("postgresql://maryamebrahimi44:18520241@localhost:5432/db")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
Base.metadata.create_all(engine)
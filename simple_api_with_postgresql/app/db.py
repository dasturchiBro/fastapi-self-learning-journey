from sqlmodel import Session, create_engine

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/fastapi_new"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
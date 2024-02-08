from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
from sqlalchemy import create_engine, text


with open("db_config.config", "r") as f:
    db_config = json.load(f)
# Database engine
engine = create_engine(
    f"mysql+mysqlconnector://{db_config['db_user']}:{db_config['db_password']}@{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def execute(query):
    try:
        db = SessionLocal()
        db.execute(text(query))
        db.commit()
        return True
    except Exception as e:
        print(e,'--->')
        db.rollback()

def show_table(query):
        db = SessionLocal()
        result = db.execute(text(query))
        tables = [row[0] for row in result]
        db.commit()
        return tables

def read_data(query):
    db = SessionLocal()
    result=db.execute(text(query))
    rows = result.fetchall()
    columns = result.keys()

    return [dict(zip(columns, row)) for row in rows]

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
session = scoped_session(sessionmaker())


def setup_db(db_url):
    engine = create_engine(db_url)
    session.configure(bind=engine)
    return engine


def init_db(engine):
    import muse_writer.models
    Base.metadata.create_all(bind=engine)

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.sql import func

engine = create_engine("mysql+pymysql://root:root@localhost/ButGitizi_05?charset=utf8mb4")

Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

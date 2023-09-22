from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#change this line with your db credentials 
engine=create_engine("postgresql://root:root@localhost/tasks",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
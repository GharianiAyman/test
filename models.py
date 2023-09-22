from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Integer,Column,Text


class Task(Base):
    __tablename__='tasks'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    description=Column(Text)



    def __repr__(self):
        return f"<Tasks name={self.name}>"
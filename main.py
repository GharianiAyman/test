from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app=FastAPI()

#class for Tasks modelisation 
class Task(BaseModel): 
    id:int
    name:str
    description:str
    class Config:
        orm_mode=True

#class for added Tasks modelisation 
class CreatedTask(BaseModel): 
    name:str
    description:str
    class Config:
        orm_mode=True

#connect to DB 
db=SessionLocal()

#display all Tasks
@app.get('/tasks',response_model=List[Task],status_code=200)

def get_all_tasks():
    tasks=db.query(models.Task).all()

    return tasks

#display specified Task
@app.get('/task/{task_id}',response_model=Task,status_code=status.HTTP_200_OK)

def get_an_task(task_id:int):
    task=db.query(models.Task).filter(models.Task.id==task_id).first()
    return task

#add new Task
@app.post('/tasks',response_model=CreatedTask,status_code=status.HTTP_201_CREATED)

def create_an_task(task:CreatedTask):
    db_task=db.query(models.Task).filter(models.Task.name==task.name).first()

    if db_task is not None:
        raise HTTPException(status_code=400,detail="task already exists")
    new_task=models.Task(
        name=task.name,
        description=task.description,
    )
    db.add(new_task)
    db.commit()
    return new_task

#update Task
@app.put('/task/{task_id}',response_model=Task,status_code=status.HTTP_200_OK)

def update_an_task(task_id:int,task:Task):
    task_to_update=db.query(models.Task).filter(models.Task.id==task_id).first()
    task_to_update.name=task.name
    task_to_update.description=task.description
    db.commit()
    return task_to_update

#delete Task
@app.delete('/task/{task_id}')

def delete_task(task_id:int):
    task_to_delete=db.query(models.Task).filter(models.Task.id==task_id).first()
    if task_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    db.delete(task_to_delete)
    db.commit()
    return task_to_delete
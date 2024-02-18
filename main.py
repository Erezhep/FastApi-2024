from fastapi import FastAPI, Depends
from datetime import datetime
from pydantic import BaseModel
from typing import Annotated, Optional


class Task(BaseModel):
    name: str
    description: Optional[str] = None

tasks = []

app = FastAPI()

@app.get("/")
def home():
    return {"date": datetime.now()}


@app.get("/tasks")
def get_tasks():
    task = Task(name="Hello", description="World! My name is Bekarys")
    return {"data": task}


@app.post("/add_task")
async def add_task(task: Annotated[Task, Depends()]):
    tasks.append(task)
    print(tasks)
    return {"ok": True}
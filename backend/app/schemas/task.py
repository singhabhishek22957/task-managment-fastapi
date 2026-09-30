from pydantic import BaseModel  , Field
from enum import Enum
from datetime import datetime

class TaskStatus(str,Enum):
    pending= "pending"
    in_progress="in_progress"
    completed="completed"

class TaskPriority(str,Enum):
    low="low"
    medium="medium"
    high="high"


class TaskCreate(BaseModel):
    title:str = Field(min_length=2 , max_length=200)
    description:str |None = Field(default=None, max_length=2000)
    priority:TaskPriority = TaskPriority.medium
    due_date:datetime | None = None
    status : TaskStatus = TaskStatus.pending

class TaskResponse(BaseModel):
    id:str
    user_id:str
    title:str
    slug:str
    description:str
    status:TaskStatus
    priority:TaskPriority
    due_date : datetime|None
    created_at:datetime
    updated_at:datetime
    completed_at:datetime |None


class TaskUpdateStatus(BaseModel):
    status: TaskStatus

class TaskUpdatePriority(BaseModel):
    priority: TaskPriority


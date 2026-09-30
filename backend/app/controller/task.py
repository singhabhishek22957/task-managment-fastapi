
from app.models.task import task_document
from app.schemas.task import TaskCreate , TaskUpdatePriority , TaskUpdateStatus
from app.core import exceptions
from app.core.utiles import serialize_document , generate_slug
from app.services.task import (
    create_task,
    get_all_task,
    get_task_by_slug,
    get_all_deleted_task,
    updated_task_priority,
    updated_task_status,
    delete_task
)

async def create_task_controller(user_id:str,data:TaskCreate):

    task = task_document(
        title=data.title,
        slug=generate_slug(data.title),
        user_id=user_id,
        description=data.description,
    )

    result = await create_task(task)
    return serialize_document(result)


async def get_all_task_controller(user_id:str):
    tasks = await get_all_task(user_id)
    return [
        serialize_document(task)
        for task in tasks
    ]

async def get_task_by_slug_controller(user_id:str, slug:str):
    data = {
        "user_id":user_id,
        "slug":slug,
    }

    result = await get_task_by_slug(data)
    return serialize_document(result)

async def get_all_deleted_task_controller(user_id:str):
    result = await get_all_deleted_task(user_id)
    return [
        serialize_document(r)
        for r in result
    ]

async def update_task_status_controller(user_id:str,data:TaskUpdateStatus):
    data = {
        "slug" :data["slug"],
        "status": data['status'],
        "user_id":user_id
    }

    result = await updated_task_status(data)
    return None


async def update_task_priority_controller(user_id:str,data:TaskUpdatePriority):
    data = {
        "slug" :data['slug'],
        "priority": data["priority"],
        "user_id":user_id
    }

    result = await updated_task_priority(data)
    return None

async def delete_task_controller(user_id:str,slug:str):
    data={
        "user_id":user_id,
        "slug":slug
    }

    await delete_task(data)
    return None




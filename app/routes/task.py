from fastapi import APIRouter , status, Request
from app.core.success_res import success_response
from app.schemas.common import APIResponse
from app.schemas.task import (
    TaskUpdatePriority,
    TaskUpdateStatus,
    TaskCreate,
    TaskResponse
)

from app.controller.task import (
    create_task_controller,
    get_all_deleted_task_controller,
    get_all_task_controller,
    get_task_by_slug_controller,
    update_task_priority_controller,
    update_task_status_controller,
    delete_task_controller
)


router = APIRouter(
    prefix="/task",
    tags=["Tasks"]
)

@router.post("/",response_model=APIResponse[TaskResponse], status_code=201)
async def create_task(req:Request , data:TaskCreate):
    user_id = req.state.user["id"]

    await create_task_controller(user_id,data)

    return success_response(None,"Task Created successfully")

@router.get("/all", response_model=APIResponse[list[TaskResponse]],status_code=200)
async def get_all_task(req:Request):
    user_id = req.state.user['id']
    tasks = await get_all_task_controller(user_id)
    return success_response(tasks,"Tasks Fetched Successfully")


@router.get("/all-deleted", response_model=APIResponse[list[TaskResponse]],status_code=200)
async def get_all_deleted_task(req:Request):
    user_id = req.state.user['id']
    tasks = await get_all_deleted_task_controller(user_id)
    return success_response(tasks,"Tasks Fetched Successfully")


@router.get("/{slug}", response_model=APIResponse[TaskResponse],status_code=200)
async def get_task_by_slug(req:Request,slug:str):
    task = await get_task_by_slug_controller(user_id=req.state.user['id'],slug=slug)
    return success_response(task , "Task Fetched Successfully")


@router.delete("/{slug}", response_model=APIResponse[TaskResponse],status_code=200)
async def delete_task(req:Request,slug:str):
    await delete_task_controller(user_id=req.state.user['id'],slug=slug)
    return success_response(None , "Task Fetched Successfully")

@router.put("/status/{slug}", response_model=APIResponse[TaskResponse],status_code=201)
async def update_task_status(req:Request,data:TaskUpdateStatus,slug:str):
    data = {
        "slug":slug,
        "status":data.status
    }

    await update_task_status_controller(user_id=req.state.user['id'],data=data)
    return success_response(None , "Task Status Updated Successfully")


@router.put("/priority/{slug}", response_model=APIResponse[TaskResponse],status_code=201)
async def update_task_status(req:Request,data:TaskUpdatePriority,slug:str):
    data = {
        "slug":slug,
        "priority":data.priority
    }

    await update_task_priority_controller(user_id=req.state.user['id'],data=data)
    return success_response(None , "Task Priority Updated Successfully")





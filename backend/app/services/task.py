from bson import ObjectId
from app.core import exceptions
from app.core.db import task_collection
from pymongo.errors import DuplicateKeyError


async def  create_task(data:dict):

    try:
        await task_collection.insert_one(data)
    except DuplicateKeyError:
        raise exceptions.TaskAlreadyExistsError()

    return {
        "msg":"Task Inserted Successfully"
    }

async def get_task_by_slug(data:dict):
    task = await task_collection.find_one({
        "slug":data["slug"],
        "user_id":data["user_id"],
        "is_deleted":False
    })

    if not task:
        raise exceptions.TaskNotFoundError()
    return task


async def get_all_task(user_id:str):
    cursor =  task_collection.find({
        "user_id":user_id,
        "is_deleted":False,
    })
    tasks = await cursor.to_list(length=100)

    if not tasks:
        raise exceptions.TaskNotFoundError()
    
    return tasks

    
async def get_all_deleted_task(user_id:str):
    cursor =  task_collection.find({
        "user_id":user_id,
        "is_deleted":True
    })

    tasks = await cursor.to_list(length=100)
    
    if not tasks:
        raise exceptions.TaskNotFoundError()

    return tasks

async def updated_task_status(data:dict):
    task = await task_collection.update_one({
        "slug":data["slug"],
        "user_id":data["user_id"],
        "is_deleted":False,
    },{
        "$set":{
            "status":data["status"],
        }
    })
    
    if task.matched_count==0:
        raise exceptions.TaskNotFoundError()
    

    return {
        "msg":"Task Updated SuccessFully"
    }


async def updated_task_priority(data:dict):
    task = await task_collection.update_one({
        "slug":data["slug"],
        "user_id":data["user_id"],
        "is_deleted":False,
    },{
        "$set":{
            "priority":data["priority"],
        }
    })
    
    if task.matched_count==0:
        raise exceptions.TaskNotFoundError()
    

    return {
        "msg":"Task Updated SuccessFully"
    }


async def delete_task(data:dict):
    task = await task_collection.update_one({
        "slug":data["slug"],
        "user_id":data["user_id"],
        "is_deleted":False,
    },{
        "$set":{
            "is_deleted":True,
        }
    })
    
    if task.matched_count==0:
        raise exceptions.TaskNotFoundError()
    

    return {
        "msg":"Task Updated SuccessFully"
    }






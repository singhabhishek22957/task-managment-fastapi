from bson import ObjectId
from app.core.db import user_collection
from app.core import exceptions
from app.core.security import hash_password

async def create_user(user_data:dict):


    is_user = await user_collection.find_one({
        "email":user_data['email']
    })

    if is_user :
        raise exceptions.UserAlreadyExistsError() 
    user_data['password'] = hash_password(user_data['password'])
    result = await user_collection.insert_one(user_data)

    return await user_collection.find_one(
        {
            "_id":result.inserted_id
        }
    )


async def get_users():
    cursor =  user_collection.find(
        {},
        {
            "password":0
        }
    )

    return await cursor.to_list(length=100)

async def get_user_by_id(user_id:str):
    if not ObjectId.is_valid(user_id):
        raise exceptions.UserNotFoundError()

    return await user_collection.find_one(
        {
            "_id":ObjectId(user_id)
        },
        {
            "password":0
        }
    )


async def update_user(
        user_id:str,
        update_data: dict
):
    if not ObjectId.is_valid(user_id):
        return exceptions.InvalidCredentialsError()
    await user_collection.update_one(
        {
            "_id":ObjectId(user_id)
        },{
            "$set":update_data
        }
    )

    return await get_user_by_id(user_id)

async def delete_user(user_id:str):
    if not ObjectId.is_valid(user_id):
        return exceptions.InvalidCredentialsError()
    result = await user_collection.delete_one(
        {
            "_id":ObjectId(user_id)
        }
    )

    return result.deleted_count>0



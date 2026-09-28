
from app.models.user import user_document 
from app.schemas.user import UserCreate , UserUpdate
from app.core import exceptions
from app.core.utiles import serialize_document
from app.services.user import (
    create_user, get_users , get_user_by_id , update_user , delete_user
)

async def create_user_controller(data: UserCreate):
    user = user_document(
        name=data.name,
        email=data.email,
        password=data.password
    )

    result = await create_user(user)


    return serialize_document(result)


async def get_users_controller():

    users = await get_users()

    if not users:
        raise exceptions.UserNotFoundError()

    return [
        serialize_document(user)
        for user in users
    ]


async def get_user_controller(user_id:str):
    user = await get_user_by_id(user_id)

    if not user:
        raise exceptions.UserNotFoundError()

    return serialize_document(user)


async def update_user_controller(
        user_id:str,
        data:UserUpdate,
):
    update_data = data.model_dump(
        exclude_unset=True
    )

    user = await update_user(
        user_id,
        update_data
    )

    if not user:
        raise exceptions.UserNotFoundError()
    return serialize_document(user)


async  def delete_user_controller(user_id:str):
    deleted = await delete_user(user_id)

    if not deleted:
        raise  exceptions.UserNotFoundError()

    return None
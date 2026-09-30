from fastapi import APIRouter  , status, Request
from app.controller.user import (
    create_user_controller,
    get_user_controller, 
    get_users_controller,
    update_user_controller,
    delete_user_controller
)
from app.schemas.user import UserCreate , UserUpdate
from app.core.success_res import success_response
from app.schemas.common import APIResponse 
from app.schemas.user import UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# @router.post("/", response_model=APIResponse[UserResponse], status_code=status.HTTP_201_CREATED )
# async def create_user(req:Request, data:UserCreate):
#     print("Req",req)
#     print(req.state.user)
#     print( await req.json())
#     print("Data", data) 
#     # user = await create_user_controller(data)
#     return success_response(None, "User Created Successfully")

@router.get("/", response_model=APIResponse[list[UserResponse]], status_code=status.HTTP_200_OK)
async def get_users():
    users= await get_users_controller()
    return success_response(users, "User Fetched Successfully")


@router.get("/me", response_model=APIResponse[UserResponse], status_code=status.HTTP_200_OK)
async def get_user(req:Request):
    user_id = req.state.user['id']
    user =  await get_user_controller(user_id)
    return success_response(user, "User Fetched Successfully")


@router.put("/", response_model=APIResponse[UserResponse], status_code= status.HTTP_201_CREATED)
async def update_user(
    req:Request,
    data:UserUpdate
):
    user_id=req.state.user['id']
    user =  await update_user_controller(
        user_id,
        data
    )
    return success_response(user , "User Updated Successfully")


@router.delete("/", response_model=APIResponse[UserResponse], status_code=status.HTTP_200_OK)

async def delete_user(req:Request):
    print(req.state.user["id"])
    await delete_user_controller(
        req.state.user["id"]
    )
    return success_response(
        None,"User Deleted Successfully"
    )


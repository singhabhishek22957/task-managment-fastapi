from fastapi import APIRouter , status 

from app.controller.auth import login_controller, register_controller

from app.core.success_res import success_response
from app.schemas.auth import LoginRequest , TokenResponse
from app.schemas.user import UserResponse, UserCreate
from app.schemas.common import APIResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=APIResponse[TokenResponse],
    status_code=status.HTTP_200_OK

)
async def login (data:LoginRequest):
    token = await login_controller(data)
    return success_response(
        token,
        "Login successful"
    )

@router.post(
    "/register",
    response_model=APIResponse[UserResponse],
    status_code=status.HTTP_201_CREATED
)
async def register(data:UserCreate):
    await register_controller(data)
    return success_response(
        None,
        "User created Successfully"
    )
from fastapi import APIRouter , status , Response

from app.controller.auth import login_controller, register_controller

from app.core.success_res import success_response
from app.schemas.auth import LoginRequest , TokenResponse
from app.schemas.user import UserResponse, UserCreate
from app.schemas.common import APIResponse
from app.core.config import settings

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    
    response_model=APIResponse[TokenResponse],
    status_code=status.HTTP_200_OK

)
async def login (res:Response,data:LoginRequest):
    token = await login_controller(data)
    print("token",token.access_token)
    res.set_cookie(
        key="access_token" ,
        value=token.access_token,
        httponly=True,
        samesite="lax",
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES*60
    )
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


@router.post("/logout")
def logout(response: Response):

    response.delete_cookie(
        key="access_token",
        httponly=True,
        secure=True,
        samesite="lax",
    )

    return {
        "message": "Logout successful",
    }
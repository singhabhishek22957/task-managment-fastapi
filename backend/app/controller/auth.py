from app.schemas.auth import LoginRequest , TokenResponse
from app.schemas.user import UserCreate
from  app.services.auth import login_user, register_user
from app.models.user import user_document

async def login_controller(
        data:LoginRequest
)-> TokenResponse:
    return await login_user(data)

async def register_controller(
        data:UserCreate
):
    user_data = user_document(
        name=data.name,
        email=data.email,
        password = data.password
    )
    return await register_user(user_data)
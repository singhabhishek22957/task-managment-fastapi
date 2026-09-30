from app.core.db import user_collection
from app.core.security import (
    verify_password , create_access_token,
    hash_password
)


from app.schemas.auth import LoginRequest , TokenResponse
from app.core import exceptions

async def login_user(data:LoginRequest)->TokenResponse:
    # 1. Find User 
    user = await user_collection.find_one(
        {
            "email":data.email.lower().strip()
        }
    )

    # 2. User doesn't exist 
    if not user:
        raise exceptions.InvalidCredentialsError()
    # 3. verify Password 
    is_password_valid = verify_password(data.password , user["password"])

    if not is_password_valid:
        raise exceptions.InvalidCredentialsError()

    # 4. Check account status
    if not user['is_active']:
        raise exceptions.UserInactiveError()

    # 5. create jwt token 
    access_token = create_access_token(
        str(user['_id'])

    )

    # 6. return token 
    return TokenResponse(
        access_token=access_token,
    )


async def register_user(data:dict):
    is_user = await user_collection.find_one({
        "email":data['email']
    })

    if is_user :
        raise exceptions.UserAlreadyExistsError()
    data['password'] = hash_password(data['password'])

    user = await user_collection.insert_one(data)

    print("user", user)
    return {
        "msg": "User Created Successfully"
    }

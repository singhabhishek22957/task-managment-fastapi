from fastapi import Depends
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials

from app.core.security import decode_access_token
from app.core.db import user_collection
from app.core import exceptions
from app.core.utiles import serialize_document

from bson import ObjectId

security = HTTPBearer()

async def get_current_user(
        credentials:HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    try:
        payload=decode_access_token(token)
    except ValueError:
        raise exceptions.InvalidCredentialsError()

    user_id = payload.get("sub")

    if not user_id:
        raise exceptions.InvalidCredentialsError()

    object_id = ObjectId(user_id)
    user = await user_collection.find_one({
        "_id":object_id
    })

    if not user:
        raise exceptions.InvalidCredentialsError()

    if not user['is_active']:
        raise exceptions.UserInactiveError()
    
    return serialize_document(user)
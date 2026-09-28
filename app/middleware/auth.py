from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse

from bson import ObjectId

from app.core.db import user_collection
from app.core.security import decode_access_token


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request:Request, call_next):

        # public routes 
        public_paths = [
            "/docs",
            "/openapi.json",
            "/auth/login",
            "/auth/register",
        ]

        if request.url.path in public_paths:
            return await call_next(request)

        # get authorization header 
        authorization = request.headers.get("Authorization")

        if not authorization:
            return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message": "Authentication required",
                    "error": {
                        "code": "UNAUTHORIZED",
                    },
                },
            )

        try:
            scheme , token = authorization.split(" ",1)

            if scheme.lower() != "bearer":
                raise ValueError()

            payload = decode_access_token(token)

            user_id = payload.get("sub")

            if not user_id:
                return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message": "Authentication required",
                    "error": {
                        "code": "UNAUTHORIZED",
                    },
                },
            )
            user = await user_collection.find_one({
                "_id":ObjectId(user_id)
            })

            if not user:
                return JSONResponse(
                    status_code=401,
                    content={
                        "success": False,
                        "message": "Invalid or expired token",
                        "error": {
                            "code": "INVALID_TOKEN",
                        },
                    },
                )

            if not user['is_active']:
                return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message": "Authentication required",
                    "error": {
                        "code": "UNAUTHORIZED",
                    },
                },
            )

            request.state.user = {
                "id":str(user['_id']),
                "email":user['email'],
                "name":user['name'],
                "is_active":user['is_active'],
                "is_email_verified":user['is_email_verified']
            }

        except Exception:
            return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message": "Invalid or expired token",
                    "error": {
                        "code": "INVALID_TOKEN",
                    },
                },
            )

        return await call_next(request)
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.db import client , create_indexes

from app.routes.user import router as user_router
from app.routes.auth import router as auth_router 
from app.routes.task import router as task_router


from app.core.exceptions import AppException
from app.handlers.exceptions import app_exception_handler

from app.middleware.auth import AuthMiddleware
from fastapi.openapi.utils import get_openapi
@asynccontextmanager 
async def lifespan(app:FastAPI):
    await client.admin.command("ping")
    await create_indexes()
    yield
    await client.close()

app = FastAPI(lifespan=lifespan)

# custom open api 

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version="1.0.0",
        description="Task Management API",
        routes = app.routes,
    )

    openapi_schema["components"]["securitySchemes"]={
        "BearerAuth":{
            "type":"http",
            "scheme":"bearer",
            "bearerFormat":"JWT"
        }
    }

    openapi_schema["security"]=[
        {
            "BearerAuth":[]
        }
    ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# add middleware 
app.add_middleware(AuthMiddleware)

# handle exceptions 
app.add_exception_handler(
    AppException,
    app_exception_handler,
)

# user route
app.include_router(user_router)

# auth route 
app.include_router(auth_router)

# task route

app.include_router(task_router)

# root

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/db-test")
async def db_test():
    await client.admin.command("ping")
    return {
        "message": " MongoDB Connected SuccessFully"
    }
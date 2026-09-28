from pymongo import AsyncMongoClient, ASCENDING
from app.core.config import settings

client = AsyncMongoClient(settings.MONGODB_URL)
database = client[settings.DATABASE_NAME]

user_collection = database['users']
task_collection = database['tasks']

async def create_indexes():
    await user_collection.create_index(
        [("email",ASCENDING)],
        unique = True,
        name= "unique_user_email"
    )

    await task_collection.create_index(
        [("user_id",ASCENDING)],
        name="tasks_by_user",
    )

    await task_collection.create_index(
        [("user_id", ASCENDING)],
        name="tasks_by_user",
    )

    await task_collection.create_index(
        [("user_id",ASCENDING), ("status",ASCENDING)],
        name="tasks_by_user_status",
    )

    await task_collection.create_index(
        [("slug",ASCENDING)],
        unique=True,
        name="tasks_unique_slug",
    )

from datetime import datetime , timezone
from typing import Any 

def task_document(*,
                    user_id,
                    title:str,
                    slug:str,
                    description:str |None = None,
                    ) -> dict[str,Any]:
    now = datetime.now(timezone.utc)

    return {
        "user_id":user_id,
        "title":title,
        "slug":slug,
        "description":description,
        "status":"pending",
        "priority":"medium",
        "is_deleted":False,
        "due_date":None,
        "created_at":now,
        "updated_at":now,
        "completed_at":None,

    }
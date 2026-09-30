from datetime import datetime , timezone
from typing import Any

def user_document(*,
                  name:str,
                  email:str,
                  password:str,
                  )-> dict[str,Any]:
    now = datetime.now(timezone.utc)

    return {
        "name":name,
        "email":email.lower().strip(),
        "password":password,
        "is_active":True,
        "is_email_verified":False,
        "created_at":now,
        "updated_at":now,
    }
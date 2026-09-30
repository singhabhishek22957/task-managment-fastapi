from services.api_client import api_client


def create_task(data: dict):
    response = api_client.post(
        "/task/",
        json=data,
    )

    response.raise_for_status()

    return response.json()


def get_all_tasks():
    response = api_client.get(
        "/task/all",
    )

    response.raise_for_status()

    return response.json()


def get_all_deleted_tasks():
    response = api_client.get(
        "/task/all-deleted",
    )

    response.raise_for_status()

    return response.json()


def get_task_by_slug(slug: str):
    response = api_client.get(
        f"/task/{slug}",
    )

    response.raise_for_status()

    return response.json()


def delete_task(slug: str):
    response = api_client.delete(
        f"/task/{slug}",
    )

    response.raise_for_status()

    return response.json()


def update_task_status(slug: str, status: str):
    response = api_client.put(
        f"/task/status/{slug}",
        json={
            "status": status,
        },
    )

    response.raise_for_status()

    return response.json()


def update_task_priority(slug: str, priority: str):
    response = api_client.put(
        f"/task/priority/{slug}",
        json={
            "priority": priority,
        },
    )

    response.raise_for_status()

    return response.json()



def update_task(slug: str, data: dict):
    response = api_client.put(
        f"/task/{slug}",
        json=data,
    )
    response.raise_for_status()
    return response.json()
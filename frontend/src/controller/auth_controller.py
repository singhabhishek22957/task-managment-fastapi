import streamlit as st
from services.api_client import api_client

def login(email: str, password: str):
    response = api_client.post(
        "/auth/login",
        json={
            "email": email,
            "password": password,
        },
    )

    response.raise_for_status()
    return response.json()


def logout():
    response = api_client.post(
        "/auth/logout"
    )

    response.raise_for_status()
   
    st.session_state.pop("access_token", None)
    st.session_state.pop("user", None)

    return response.json()

def register(name:str, email:str, password:str):
    response = api_client.post(
        "/auth/register",
        json={
            "name": name,
            "email": email,
            "password": password,
        },
    )

    response.raise_for_status()

    return response.json()


def get_current_user():
    response = api_client.get(
        "/users/me"
    )

    response.raise_for_status()

    data = response.json()
    print(data)
    user = data["data"]

    st.session_state["user"] = {
        "name": user["name"],
        "email": user["email"],
    }

    return st.session_state["user"]




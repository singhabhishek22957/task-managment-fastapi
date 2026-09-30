import re

import streamlit as st

from controller.auth_controller import login
from controller.auth_controller import get_current_user
from services.api_client import api_client


st.set_page_config(
    page_title="Login | TaskFlow",
    page_icon="🔐",
    layout="centered",
)


st.title("🔐 Login")
st.caption("Sign in to your Task Management account")

st.divider()


def validate_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email))


def validate_password(password: str) -> bool:
    # Minimum 8 characters, at least:
    # 1 uppercase, 1 lowercase, 1 number, 1 special character
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$"
    return bool(re.fullmatch(pattern, password))


with st.form("login_form"):

    email = st.text_input(
        "Email",
        placeholder="Enter your email",
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password",
    )

    submitted = st.form_submit_button(
        "Login",
        type="primary",
        width="stretch",
    )


if submitted:

    email = email.strip()

    # Validate email
    if not email:
        st.error("Email is required.")

    elif not validate_email(email):
        st.error("Please enter a valid email address.")

    # Validate password
    elif not password:
        st.error("Password is required.")

    elif not validate_password(password):
        st.error(
            "Password must be at least 8 characters and contain "
            "uppercase, lowercase, number, and special character."
        )

    # Call API only after validation
    else:
        try:
            response = login(
                email=email,
                password=password,
            )

           
            # print("STATUS:", response.status_code)
            
            get_current_user()
            st.success("Login successful!")

            st.switch_page("app.py")

        except Exception as e:
            st.error(str(e))


st.divider()

st.write("Don't have an account?")

if st.button("Create Account", width="stretch"):
    st.switch_page("pages/register.py")
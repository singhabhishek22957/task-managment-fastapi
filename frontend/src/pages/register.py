import re

import streamlit as st

from controller.auth_controller import register


st.set_page_config(
    page_title="Signup | TaskFlow",
    page_icon="📝",
    layout="centered",
)


st.title("📝 Create Account")
st.caption("Create your Task Management account")

st.divider()


def validate_name(name: str) -> bool:
    pattern = r"^[A-Za-z ]{2,50}$"
    return bool(re.fullmatch(pattern, name))


def validate_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email))


def validate_password(password: str) -> bool:
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$"
    return bool(re.fullmatch(pattern, password))


with st.form("signup_form"):

    name = st.text_input(
        "Name",
        placeholder="Enter your name",
    )

    email = st.text_input(
        "Email",
        placeholder="Enter your email",
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password",
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        placeholder="Confirm your password",
    )

    submitted = st.form_submit_button(
        "Create Account",
        type="primary",
        width="stretch",
    )


if submitted:

    name = name.strip()
    email = email.strip()

    # Name validation
    if not name:
        st.error("Name is required.")

    elif not validate_name(name):
        st.error("Name must contain only letters and spaces.")

    # Email validation
    elif not email:
        st.error("Email is required.")

    elif not validate_email(email):
        st.error("Please enter a valid email address.")

    # Password validation
    elif not password:
        st.error("Password is required.")

    elif not validate_password(password):
        st.error(
            "Password must be at least 8 characters and contain "
            "uppercase, lowercase, number, and special character."
        )

    # Confirm password
    elif password != confirm_password:
        st.error("Passwords do not match.")

    # Call API
    else:
        try:
            response = register(
                name=name,
                email=email,
                password=password,
            )

            st.success("Account created successfully!")

            st.switch_page("pages/login.py")

        except Exception as e:
            st.error(str(e))


st.divider()

st.write("Already have an account?")

if st.button("Login", width="stretch"):
    st.switch_page("pages/login.py")
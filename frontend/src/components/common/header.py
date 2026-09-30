import streamlit as st

from controller.auth_controller import get_current_user, logout


PAGE_CONFIG = {
    "dashboard": {
        "title": "Dashboard",
        "icon": "⌂",
    },
    "tasks": {
        "title": "Tasks",
        "icon": "✓",
    },
    "users": {
        "title": "Users",
        "icon": "♙",
    },
    "settings": {
        "title": "Settings",
        "icon": "⚙",
    },
}


def get_page_info(page_name: str):
    page = PAGE_CONFIG.get(
        page_name.lower(),
        {
            "title": page_name.title(),
            "icon": "•",
        },
    )

    return page["title"], page["icon"]


def render_header(page_name: str = "dashboard"):

    page_title, page_icon = get_page_info(page_name)

    # --------------------------------------------------
    # Check authentication
    # --------------------------------------------------

    # access_token = st.session_state.get("access_token")
    user = st.session_state.get("user")

    # Token exists but user is not loaded
    if  not user:
        try:
            user = get_current_user()
        except Exception:
            # st.session_state.pop("access_token", None)
            st.session_state.pop("user", None)
            user = None

    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    left, center, right = st.columns(
        [2.5, 3, 2.5],
        vertical_alignment="center",
    )

    # --------------------------------------------------
    # LEFT
    # --------------------------------------------------

    with left:
        st.header("◈ TaskFlow")

    # --------------------------------------------------
    # CENTER
    # --------------------------------------------------

    with center:
        st.write(
            f"### {page_icon} {page_title}"
        )

    # --------------------------------------------------
    # RIGHT
    # --------------------------------------------------

    with right:

        if  user:

            user_col, logout_col = st.columns(
                [2, 1],
                vertical_alignment="center",
            )

            with user_col:
                st.write(
                    f"👤 **{user['name']}**"
                )

                st.caption(
                    user["email"]
                )

            with logout_col:

                if st.button(
                    "Logout",
                    key="header_logout",
                    width="stretch",
                ):
                    try:
                        logout()
                    except Exception:
                        # Clear local session even if API logout fails
                        st.session_state.pop(
                            "access_token",
                            None,
                        )
                        st.session_state.pop(
                            "user",
                            None,
                        )

                    st.switch_page(
                        "pages/login.py"
                    )

        else:

            login_col, signup_col = st.columns(
                2,
                vertical_alignment="center",
            )

            with login_col:

                if st.button(
                    "Login",
                    key="header_login",
                    width="stretch",
                ):
                    st.switch_page(
                        "pages/login.py"
                    )

            with signup_col:

                if st.button(
                    "Signup",
                    key="header_signup",
                    width="stretch",
                ):
                    st.switch_page(
                        "pages/register.py"
                    )
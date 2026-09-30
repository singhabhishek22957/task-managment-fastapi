
import streamlit as st


def render_sidebar():
    """Render task navigation sidebar."""

    st.sidebar.title("◈ TaskFlow")
    st.sidebar.caption("Task Management")

    st.sidebar.divider()

    # -----------------------------
    # Task Navigation
    # -----------------------------

    st.sidebar.subheader("Tasks")

    if st.sidebar.button(
        "✓  All Tasks",
        key="sidebar_all_tasks",
        width="stretch",
    ):
        st.switch_page(
            "pages/all_tasks.py"
        )

    if st.sidebar.button(
        "🗑️  Deleted Tasks",
        key="sidebar_deleted_tasks",
        width="stretch",
    ):
        st.switch_page(
            "pages/deleted_tasks.py"
        )

    if st.sidebar.button(
        "＋  Create Task",
        key="sidebar_create_task",
        width="stretch",
    ):
        st.switch_page(
            "pages/create_task.py"
        )

    if st.sidebar.button(
        "✎  Update Task",
        key="sidebar_update_task",
        width="stretch",
    ):
        st.switch_page(
            "pages/update_task.py"
        )


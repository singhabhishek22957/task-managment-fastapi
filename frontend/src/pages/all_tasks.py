import streamlit as st

from controller.task_controller import (
    get_all_tasks,
    delete_task,
    update_task_status,
    update_task_priority,
)

st.set_page_config(
    page_title="Tasks | TaskFlow",
    page_icon="✓",
    layout="wide",
)

st.title("✓ All Tasks")
st.caption("Manage all your tasks")
st.divider()


# --------------------------------------------------
# Fetch Tasks
# --------------------------------------------------

try:
    response = get_all_tasks()
    tasks = response.get("data", [])

except Exception as e:
    st.error(str(e))
    st.stop()


# --------------------------------------------------
# Header
# --------------------------------------------------

if not tasks:
    st.info("No tasks found.")
    st.stop()

st.subheader(f"Tasks ({len(tasks)})")


# --------------------------------------------------
# Task Table
# --------------------------------------------------

for task in tasks:

    with st.container(border=True):

        col1, col2, col3, col4, col5, col6 = st.columns(
            [2.5, 3, 1.2, 1.2, 1.5, 2]
        )

        # Title
        with col1:
            st.write("**Title**")
            st.write(task["title"])

        # Description
        with col2:
            st.write("**Description**")
            st.write(task["description"])

        # Status
        with col3:
            st.write("**Status**")
            st.write(task["status"].title())

        # Priority
        with col4:
            st.write("**Priority**")
            st.write(task["priority"].title())

        # Due date
        with col5:
            st.write("**Due Date**")

            if task["due_date"]:
                st.write(task["due_date"][:10])
            else:
                st.write("No deadline")

        # Actions
        with col6:
            st.write("**Actions**")

            edit_col, status_col, priority_col, delete_col = st.columns(4)

            with edit_col:
                if st.button(
                    "✏️",
                    key=f"edit_{task['slug']}",
                    help="Edit task",
                ):
                    st.session_state["edit_task"] = task
                    st.switch_page("pages/edit_task.py")

            with status_col:
                if st.button(
                    "🔄",
                    key=f"status_{task['slug']}",
                    help="Change status",
                ):
                    st.session_state["status_task"] = task
                    st.rerun()

            with priority_col:
                if st.button(
                    "⚡",
                    key=f"priority_{task['slug']}",
                    help="Change priority",
                ):
                    st.session_state["priority_task"] = task
                    st.rerun()

            with delete_col:
                if st.button(
                    "🗑️",
                    key=f"delete_{task['slug']}",
                    help="Delete task",
                ):
                    try:
                        delete_task(task["slug"])
                        st.success("Task deleted successfully.")
                        st.rerun()

                    except Exception as e:
                        st.error(str(e))


# --------------------------------------------------
# Status Editor
# --------------------------------------------------

if "status_task" in st.session_state:

    task = st.session_state["status_task"]

    st.divider()
    st.subheader(f"🔄 Change Status — {task['title']}")

    status = st.selectbox(
        "Status",
        ["pending", "in_progress", "completed"],
        index=[
            "pending",
            "in_progress",
            "completed",
        ].index(task["status"]),
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Update Status", type="primary"):
            try:
                update_task_status(
                    task["slug"],
                    status,
                )

                del st.session_state["status_task"]

                st.success("Status updated successfully.")
                st.rerun()

            except Exception as e:
                st.error(str(e))

    with col2:
        if st.button("Cancel Status"):
            del st.session_state["status_task"]
            st.rerun()


# --------------------------------------------------
# Priority Editor
# --------------------------------------------------

if "priority_task" in st.session_state:

    task = st.session_state["priority_task"]

    st.divider()
    st.subheader(f"⚡ Change Priority — {task['title']}")

    priority = st.selectbox(
        "Priority",
        ["low", "medium", "high"],
        index=[
            "low",
            "medium",
            "high",
        ].index(task["priority"]),
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Update Priority", type="primary"):
            try:
                update_task_priority(
                    task["slug"],
                    priority,
                )

                del st.session_state["priority_task"]

                st.success("Priority updated successfully.")
                st.rerun()

            except Exception as e:
                st.error(str(e))

    with col2:
        if st.button("Cancel Priority"):
            del st.session_state["priority_task"]
            st.rerun()
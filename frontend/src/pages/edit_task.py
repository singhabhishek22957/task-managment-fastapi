import streamlit as st

from controller.task_controller import update_task


st.set_page_config(
    page_title="Edit Task | TaskFlow",
    page_icon="✏️",
    layout="centered",
)


# --------------------------------------------------
# Get selected task
# --------------------------------------------------

task = st.session_state.get("edit_task")

if not task:
    st.warning("No task selected.")
    
    if st.button("← Back to Tasks"):
        st.switch_page("pages/tasks.py")

    st.stop()


# --------------------------------------------------
# Page Header
# --------------------------------------------------

st.title("✏️ Edit Task")
st.caption("Update your task details")
st.divider()


# --------------------------------------------------
# Edit Form
# --------------------------------------------------

with st.form("edit_task_form"):

    title = st.text_input(
        "Title",
        value=task.get("title", ""),
        placeholder="Enter task title",
    )

    description = st.text_area(
        "Description",
        value=task.get("description", ""),
        placeholder="Enter task description",
        height=150,
    )

    col1, col2 = st.columns(2)

    with col1:
        priority_options = [
            "low",
            "medium",
            "high",
        ]

        current_priority = task.get(
            "priority",
            "medium",
        )

        priority = st.selectbox(
            "Priority",
            priority_options,
            index=priority_options.index(current_priority),
        )

    with col2:
        status_options = [
            "pending",
            "in_progress",
            "completed",
        ]

        current_status = task.get(
            "status",
            "pending",
        )

        status = st.selectbox(
            "Status",
            status_options,
            index=status_options.index(current_status),
        )

    due_date = st.date_input(
        "Due Date",
        value=None,
    )

    st.divider()

    save, cancel = st.columns(2)

    with save:
        submitted = st.form_submit_button(
            "💾 Save Changes",
            type="primary",
            width="stretch",
        )

    with cancel:
        cancelled = st.form_submit_button(
            "Cancel",
            width="stretch",
        )


# --------------------------------------------------
# Cancel
# --------------------------------------------------

if cancelled:
    st.session_state.pop("edit_task", None)
    st.switch_page("pages/tasks.py")


# --------------------------------------------------
# Update Task
# --------------------------------------------------

if submitted:

    title = title.strip()
    description = description.strip()

    if not title:
        st.error("Title is required.")

    elif not description:
        st.error("Description is required.")

    else:

        data = {
            "title": title,
            "description": description,
            "priority": priority,
            "status": status,
            "due_date": (
                due_date.isoformat()
                if due_date
                else None
            ),
        }

        try:

            update_task(
                task["slug"],
                data,
            )

            st.session_state.pop(
                "edit_task",
                None,
            )

            st.success(
                "Task updated successfully!"
            )

            st.switch_page("pages/tasks.py")

        except Exception as e:
            st.error(str(e))
import streamlit as st

from controller.task_controller import create_task


st.set_page_config(
    page_title="Create Task | TaskFlow",
    page_icon="➕",
    layout="centered",
)


st.title("➕ Create Task")
st.caption("Create a new task")

st.divider()


with st.form("create_task_form"):

    title = st.text_input(
        "Title",
        placeholder="Enter task title",
    )

    description = st.text_area(
        "Description",
        placeholder="Enter task description",
        height=150,
    )

    submitted = st.form_submit_button(
        "Create Task",
        type="primary",
        width="stretch",
    )


if submitted:

    title = title.strip()
    description = description.strip()

    if not title:
        st.error("Title is required.")

    elif not description:
        st.error("Description is required.")

    else:
        try:
            response = create_task({
                "title": title,
                "description": description,
            })

            st.success("Task created successfully!")

            st.session_state["task_created"] = True

        except Exception as e:
            st.error(str(e))
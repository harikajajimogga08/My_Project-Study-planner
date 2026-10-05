import streamlit as st
from planner import get_today_tasks, mark_task_completed


st.title("📚 Study Planner")

student_id = st.session_state.get(
    "student_id"
)

if not student_id:

    st.warning(
        "Please create your profile from the Home page."
    )

    st.stop()


tasks = get_today_tasks(
    student_id
)


st.subheader("Today's Tasks")


if not tasks:

    st.info(
        "No tasks available for today."
    )

else:

    for task in tasks:

        col1, col2, col3 = st.columns(
            [2, 4, 1]
        )

        with col1:

            st.write(
                f"⏰ {task.start_time.strftime('%I:%M %p')}"
            )

        with col2:

            status = (
                "✅ Completed"
                if task.completed
                else "📌 Pending"
            )

            st.write(
                f"**{task.task}**  \n"
                f"{task.category} | {status}"
            )

        with col3:

            if not task.completed:

                if st.button(
                    "Done",
                    key=f"done_{task.id}"
                ):

                    mark_task_completed(
                        task.id
                    )

                    st.rerun()
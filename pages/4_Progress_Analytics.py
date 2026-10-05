import streamlit as st
import matplotlib.pyplot as plt

from analytics import (
    get_task_statistics,
    get_skill_data,
    calculate_skill_average
)


st.title("📊 Progress Analytics")


student_id = st.session_state.get(
    "student_id"
)


if not student_id:

    st.warning(
        "Please create your profile first."
    )

    st.stop()


stats = get_task_statistics(
    student_id
)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Tasks",
        stats["total"]
    )


with col2:

    st.metric(
        "Completed",
        stats["completed"]
    )


with col3:

    st.metric(
        "Completion",
        f"{stats['percentage']}%"
    )


st.divider()


skill_data = get_skill_data(
    student_id
)


if skill_data.empty:

    st.info(
        "Update your skills from the Skill Development page."
    )

else:

    average = calculate_skill_average(
        skill_data
    )

    st.metric(
        "Average Skill Level",
        f"{average}%"
    )

    st.subheader(
        "📈 Skill Progress"
    )

    chart_data = skill_data.set_index(
        "Skill"
    )["Current"]

    st.bar_chart(
        chart_data
    )


st.divider()


st.subheader(
    "🎯 Improvement Strategy"
)


st.write(
    """
    **If your progress is low:**

    • Spend 30–60 minutes daily on technical skills.

    • Complete one coding problem every day.

    • Practice communication for 15–30 minutes.

    • Participate actively in team projects.

    • Maintain a GitHub portfolio.

    • Revise college subjects regularly.

    • Take mock coding tests before placements.
    """
)
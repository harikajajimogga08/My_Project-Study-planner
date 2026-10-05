import streamlit as st
from datetime import date

from database import (
    initialize_database,
    get_session,
    Student,
    SkillProgress
)

from planner import create_daily_plan
from reminders import create_default_reminders
from ai_assistant import ask_ai
from utils import get_recommended_schedule


st.set_page_config(
    page_title="AI Student Study Planner",
    page_icon="🎓",
    layout="wide"
)


initialize_database()


# -----------------------------
# SESSION STATE
# -----------------------------

if "student_id" not in st.session_state:

    st.session_state.student_id = None


if "profile_created" not in st.session_state:

    st.session_state.profile_created = False


# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("🎓 AI Study Planner")

    st.markdown(
        """
        ### Student Dashboard

        🏫 College: **9:00 AM - 4:00 PM**

        💻 Coding Test: **8:00 PM - 10:00 PM**

        ⏱️ Test Duration: **45 minutes**
        """
    )

    st.divider()

    st.info(
        "The planner helps you balance academics, "
        "technical skills, communication and career preparation."
    )


# -----------------------------
# PROFILE
# -----------------------------

st.title("🎓 AI Student Study Planner")

st.subheader("Create Your Student Profile")


if not st.session_state.profile_created:

    name = st.text_input(
        "Student Name"
    )

    career_goal = st.text_input(
        "What is your future career goal?",
        placeholder="Example: Software Developer / AI Engineer / Data Analyst"
    )

    study_hours = st.slider(
        "Preferred daily study hours",
        min_value=1.0,
        max_value=5.0,
        value=2.0,
        step=0.5
    )

    if st.button(
        "🚀 Create My Study Plan",
        type="primary"
    ):

        if not name:

            st.warning(
                "Please enter your name."
            )

        else:

            session = get_session()

            student = Student(
                name=name,
                branch="CSE",
                year=2,
                career_goal=career_goal,
                daily_study_hours=study_hours
            )

            session.add(student)

            session.commit()

            student_id = student.id

            session.close()

            st.session_state.student_id = student_id

            create_daily_plan(student_id)

            create_default_reminders(student_id)

            st.session_state.profile_created = True

            st.success(
                "🎉 Your personalized study planner has been created!"
            )

            st.rerun()


# -----------------------------
# MAIN DASHBOARD
# -----------------------------

else:

    session = get_session()

    student = session.query(Student).filter(
        Student.id == st.session_state.student_id
    ).first()

    session.close()

    st.success(
        f"Welcome {student.name}! 👋"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Year",
            "2nd Year"
        )

    with col2:

        st.metric(
            "Department",
            "CSE"
        )

    with col3:

        st.metric(
            "College",
            "9 AM - 4 PM"
        )

    with col4:

        st.metric(
            "Coding",
            "45 min/day"
        )

    st.divider()

    # -------------------------
    # TODAY'S PLAN
    # -------------------------

    st.subheader("📅 Today's Recommended Schedule")

    schedule = get_recommended_schedule()

    for item in schedule:

        if item["category"] == "College":

            st.info(
                f"🏫 **{item['time']}** — {item['activity']}"
            )

        elif item["category"] == "Coding":

            st.warning(
                f"💻 **{item['time']}** — {item['activity']}"
            )

        else:

            st.write(
                f"⏰ **{item['time']}** — "
                f"{item['activity']}"
            )

    st.divider()

    # -------------------------
    # AI ASSISTANT
    # -------------------------

    st.subheader("🤖 AI Study Assistant")

    user_question = st.text_area(
        "Ask your AI assistant",
        placeholder=(
            "Example: I have a coding test tomorrow. "
            "How should I prepare?"
        )
    )

    if st.button("Ask AI"):

        if user_question:

            with st.spinner("AI is thinking..."):

                answer = ask_ai(
                    user_question
                )

            st.markdown(answer)

        else:

            st.warning(
                "Enter your question first."
            )

    st.divider()

    st.subheader("🎯 Your Career Goal")

    st.write(
        student.career_goal
        if student.career_goal
        else "Not specified"
    )

    st.subheader("💡 Daily Motivation")

    st.success(
        "Small consistent improvements every day "
        "can make a big difference in your technical career. 🚀"
    )
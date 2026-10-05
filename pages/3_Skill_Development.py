import streamlit as st

from database import (
    get_session,
    SkillProgress
)

from utils import (
    get_skill_recommendations
)


st.title("🚀 Skill Development")


student_id = st.session_state.get(
    "student_id"
)


if not student_id:

    st.warning(
        "Please create your profile first."
    )

    st.stop()


session = get_session()

student = session.query(
    __import__("database").Student
).filter(
    __import__("database").Student.id == student_id
).first()

session.close()


skills = get_skill_recommendations(
    student.career_goal
)


st.subheader(
    "🎯 Recommended Skills For Your Career"
)


for skill in skills:

    st.write(
        f"🔹 {skill}"
    )


st.divider()


st.subheader(
    "📊 Update Your Skill Level"
)


selected_skill = st.selectbox(
    "Select Skill",
    skills
)


score = st.slider(
    "Current Skill Level",
    min_value=0,
    max_value=100,
    value=50
)


if st.button(
    "Save Skill Progress"
):

    session = get_session()

    existing = session.query(
        SkillProgress
    ).filter(
        SkillProgress.student_id == student_id,
        SkillProgress.skill == selected_skill
    ).first()

    if existing:

        existing.score = score

    else:

        new_skill = SkillProgress(
            student_id=student_id,
            skill=selected_skill,
            score=score,
            target=100
        )

        session.add(new_skill)

    session.commit()

    session.close()

    st.success(
        f"✅ {selected_skill} progress updated!"
    )


st.divider()


st.subheader(
    "💼 Important Career Skills"
)


career_skills = {

    "Technical": [
        "Programming",
        "DSA",
        "Database",
        "Git & GitHub",
        "AI / ML"
    ],

    "Communication": [
        "English speaking",
        "Presentation",
        "Interview communication"
    ],

    "Team Skills": [
        "Teamwork",
        "Leadership",
        "Problem solving",
        "Time management"
    ]
}


for category, items in career_skills.items():

    st.markdown(
        f"### {category}"
    )

    for item in items:

        st.write(
            f"• {item}"
        )
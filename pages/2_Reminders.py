import streamlit as st
from datetime import datetime

from reminders import (
    get_current_reminders,
    complete_reminder
)


st.title("🔔 Smart Reminders")


student_id = st.session_state.get(
    "student_id"
)


if not student_id:

    st.warning(
        "Please create your profile first."
    )

    st.stop()


st.subheader(
    "Today's Study Reminders"
)


reminders = get_current_reminders(
    student_id
)


if not reminders:

    st.success(
        "🎉 No pending reminders right now!"
    )

else:

    for reminder in reminders:

        st.warning(
            f"🔔 {reminder.message}"
        )

        if st.button(
            "Mark as Done",
            key=f"reminder_{reminder.id}"
        ):

            complete_reminder(
                reminder.id
            )

            st.rerun()


st.divider()


st.subheader("⏰ Fixed Daily Routine")


routine = [

    ("05:30 AM", "Core subject study"),

    ("04:30 PM", "Technical skill development"),

    ("05:30 PM", "Communication / Team skills"),

    ("06:15 PM", "Revision / assignments"),

    ("08:00 PM", "45-minute coding test"),

    ("09:00 PM", "Coding practice"),

    ("10:15 PM", "Daily revision")
]


for time, activity in routine:

    st.write(
        f"⏰ **{time}** → {activity}"
    )
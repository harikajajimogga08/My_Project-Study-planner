from datetime import date, datetime, time

from database import Reminder, get_session


def create_default_reminders(student_id):

    session = get_session()

    reminders = [

        Reminder(
            student_id=student_id,
            message="🌅 Good morning! Start your core subject study.",
            reminder_date=date.today(),
            reminder_time=time(5, 30)
        ),

        Reminder(
            student_id=student_id,
            message="💻 Time to improve your technical skills.",
            reminder_date=date.today(),
            reminder_time=time(16, 30)
        ),

        Reminder(
            student_id=student_id,
            message="🗣️ Practice communication and teamwork skills.",
            reminder_date=date.today(),
            reminder_time=time(17, 30)
        ),

        Reminder(
            student_id=student_id,
            message="🔥 Your 45-minute coding test starts now!",
            reminder_date=date.today(),
            reminder_time=time(20, 0)
        ),

        Reminder(
            student_id=student_id,
            message="🧠 Complete your coding practice.",
            reminder_date=date.today(),
            reminder_time=time(21, 0)
        ),

        Reminder(
            student_id=student_id,
            message="📚 Revise today's learning before sleeping.",
            reminder_date=date.today(),
            reminder_time=time(22, 15)
        )
    ]

    session.add_all(reminders)

    session.commit()

    session.close()


def get_current_reminders(student_id):

    session = get_session()

    now = datetime.now()

    reminders = (
        session.query(Reminder)
        .filter(
            Reminder.student_id == student_id,
            Reminder.reminder_date == date.today(),
            Reminder.reminder_time <= now.time(),
            Reminder.completed == False
        )
        .all()
    )

    session.close()

    return reminders


def complete_reminder(reminder_id):

    session = get_session()

    reminder = session.query(Reminder).filter(
        Reminder.id == reminder_id
    ).first()

    if reminder:

        reminder.completed = True

        session.commit()

    session.close()
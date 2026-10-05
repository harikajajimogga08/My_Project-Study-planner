from datetime import date, time

from database import StudyTask, get_session


def create_daily_plan(student_id):

    session = get_session()

    tasks = [

        StudyTask(
            student_id=student_id,
            task="Study one core B.Tech subject",
            category="Academic",
            task_date=date.today(),
            start_time=time(5, 30),
            end_time=time(6, 30)
        ),

        StudyTask(
            student_id=student_id,
            task="Technical skill practice",
            category="Technical",
            task_date=date.today(),
            start_time=time(16, 30),
            end_time=time(17, 30)
        ),

        StudyTask(
            student_id=student_id,
            task="Communication and speaking practice",
            category="Communication",
            task_date=date.today(),
            start_time=time(17, 30),
            end_time=time(18, 15)
        ),

        StudyTask(
            student_id=student_id,
            task="Assignment / revision",
            category="Revision",
            task_date=date.today(),
            start_time=time(18, 15),
            end_time=time(19, 0)
        ),

        StudyTask(
            student_id=student_id,
            task="Daily coding test",
            category="Coding Test",
            task_date=date.today(),
            start_time=time(20, 0),
            end_time=time(20, 45)
        ),

        StudyTask(
            student_id=student_id,
            task="Coding problem practice",
            category="Coding",
            task_date=date.today(),
            start_time=time(21, 0),
            end_time=time(21, 45)
        ),

        StudyTask(
            student_id=student_id,
            task="Daily revision and tomorrow preparation",
            category="Revision",
            task_date=date.today(),
            start_time=time(22, 15),
            end_time=time(22, 45)
        )
    ]

    session.add_all(tasks)
    session.commit()

    session.close()


def get_today_tasks(student_id):

    session = get_session()

    tasks = (
        session.query(StudyTask)
        .filter(
            StudyTask.student_id == student_id,
            StudyTask.task_date == date.today()
        )
        .all()
    )

    session.close()

    return tasks


def mark_task_completed(task_id):

    session = get_session()

    task = session.query(StudyTask).filter(
        StudyTask.id == task_id
    ).first()

    if task:
        task.completed = True
        session.commit()

    session.close()
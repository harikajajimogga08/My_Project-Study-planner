import pandas as pd
import numpy as np

from database import StudyTask, SkillProgress, get_session


def get_task_statistics(student_id):

    session = get_session()

    tasks = (
        session.query(StudyTask)
        .filter(
            StudyTask.student_id == student_id
        )
        .all()
    )

    session.close()

    if not tasks:

        return {
            "total": 0,
            "completed": 0,
            "percentage": 0
        }

    total = len(tasks)

    completed = sum(
        1 for task in tasks
        if task.completed
    )

    percentage = (
        completed / total * 100
    )

    return {
        "total": total,
        "completed": completed,
        "percentage": round(percentage, 2)
    }


def get_skill_data(student_id):

    session = get_session()

    skills = (
        session.query(SkillProgress)
        .filter(
            SkillProgress.student_id == student_id
        )
        .all()
    )

    session.close()

    data = []

    for skill in skills:

        data.append({
            "Skill": skill.skill,
            "Current": skill.score,
            "Target": skill.target,
            "Gap": max(skill.target - skill.score, 0)
        })

    return pd.DataFrame(data)


def calculate_skill_average(dataframe):

    if dataframe.empty:

        return 0

    scores = dataframe["Current"].to_numpy()

    return round(
        np.mean(scores),
        2
    )
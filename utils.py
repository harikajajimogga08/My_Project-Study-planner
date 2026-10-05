from datetime import time, datetime, timedelta


COLLEGE_START = time(9, 0)
COLLEGE_END = time(16, 0)

CODING_WINDOW_START = time(20, 0)
CODING_WINDOW_END = time(22, 0)

CODING_TEST_DURATION = 45


def is_college_time(current_time):

    return COLLEGE_START <= current_time <= COLLEGE_END


def is_coding_window(current_time):

    return CODING_WINDOW_START <= current_time <= CODING_WINDOW_END


def get_available_study_slots():

    slots = [

        ("05:30", "06:30", "Morning Study"),

        ("16:30", "17:30", "Technical Skills"),

        ("17:30", "18:15", "Communication / Team Skills"),

        ("18:15", "19:00", "Revision"),

        ("20:00", "20:45", "Daily Coding Test"),

        ("21:00", "21:45", "Coding Practice"),

        ("22:15", "22:45", "Daily Revision"),

    ]

    return slots


def get_recommended_schedule():

    return [

        {
            "time": "5:30 AM - 6:30 AM",
            "activity": "Core Subject Study",
            "category": "Academic"
        },

        {
            "time": "9:00 AM - 4:00 PM",
            "activity": "College Hours",
            "category": "College"
        },

        {
            "time": "4:30 PM - 5:30 PM",
            "activity": "Technical Skill Development",
            "category": "Technical"
        },

        {
            "time": "5:30 PM - 6:15 PM",
            "activity": "Communication / Team Skills",
            "category": "Soft Skills"
        },

        {
            "time": "6:15 PM - 7:00 PM",
            "activity": "Revision / Assignment Work",
            "category": "Revision"
        },

        {
            "time": "8:00 PM - 8:45 PM",
            "activity": "Daily Coding Test",
            "category": "Coding"
        },

        {
            "time": "9:00 PM - 9:45 PM",
            "activity": "Coding Practice",
            "category": "Coding"
        },

        {
            "time": "10:15 PM - 10:45 PM",
            "activity": "Daily Revision",
            "category": "Revision"
        }
    ]


def get_skill_recommendations(career_goal):

    goal = career_goal.lower()

    recommendations = []

    if "software" in goal or "developer" in goal:

        recommendations = [
            "Python / Java",
            "Data Structures and Algorithms",
            "SQL",
            "Git and GitHub",
            "Problem Solving",
            "Communication",
            "Teamwork"
        ]

    elif "data" in goal:

        recommendations = [
            "Python",
            "Pandas",
            "NumPy",
            "Statistics",
            "Machine Learning",
            "SQL",
            "Communication"
        ]

    elif "ai" in goal or "machine learning" in goal:

        recommendations = [
            "Python",
            "NumPy",
            "Pandas",
            "Machine Learning",
            "Generative AI",
            "Problem Solving",
            "Communication"
        ]

    elif "web" in goal:

        recommendations = [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git and GitHub",
            "Problem Solving",
            "Teamwork"
        ]

    else:

        recommendations = [
            "Programming",
            "Data Structures",
            "Problem Solving",
            "Communication",
            "Teamwork",
            "Git and GitHub",
            "Interview Preparation"
        ]

    return recommendations
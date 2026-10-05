from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Date,
    Time
)

from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date


DATABASE_URL = "sqlite:///data/student_planner.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    branch = Column(String, default="CSE")
    year = Column(Integer, default=2)
    career_goal = Column(String, default="")
    daily_study_hours = Column(Float, default=2.0)


class StudyTask(Base):
    __tablename__ = "study_tasks"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    task = Column(String, nullable=False)
    category = Column(String)
    task_date = Column(Date, default=date.today)
    start_time = Column(Time)
    end_time = Column(Time)
    completed = Column(Boolean, default=False)


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    message = Column(String)
    reminder_date = Column(Date)
    reminder_time = Column(Time)
    completed = Column(Boolean, default=False)


class SkillProgress(Base):
    __tablename__ = "skill_progress"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    skill = Column(String)
    score = Column(Float, default=0)
    target = Column(Float, default=100)
    updated_date = Column(Date, default=date.today)


def initialize_database():

    import os

    os.makedirs("data", exist_ok=True)

    Base.metadata.create_all(engine)


def get_session():
    return SessionLocal()
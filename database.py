from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import enum

class UserRole(enum.Enum):
    TRAINEE = "trainee"
    ADMIN = "admin"

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    name = Column(String)
    position = Column(String)
    start_date = Column(DateTime)
    role = Column(Enum(UserRole), default=UserRole.TRAINEE)
    last_activity = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Отношения
    test_results = relationship("TestResult", back_populates="user")
    questions = relationship("Question", back_populates="user")

class TestResult(Base):
    __tablename__ = 'test_results'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    test_id = Column(Integer)
    score = Column(Integer)
    completed_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="test_results")

class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(Text)
    answer = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="questions")

# Создание базы данных
engine = create_engine('sqlite:///hotel_bot.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

async def get_user_role(telegram_id: int) -> UserRole:
    """Получает роль пользователя из базы данных"""
    session = Session()
    try:
        user = session.query(User).filter(User.telegram_id == telegram_id).first()
        if user:
            return user.role
        return UserRole.TRAINEE  # Возвращаем роль стажера по умолчанию
    finally:
        session.close() 
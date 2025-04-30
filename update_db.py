from database import Base, engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy import text

# Определяем новую структуру таблицы users
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    name = Column(String)
    phone = Column(String)  # Добавляем колонку phone
    position = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    created_at = Column(DateTime, default=datetime.now)
    last_activity = Column(DateTime, nullable=True)

def add_phone_column():
    with engine.connect() as conn:
        try:
            conn.execute(text("ALTER TABLE users ADD COLUMN phone TEXT"))
            conn.commit()
            print("Колонка phone успешно добавлена!")
        except Exception as e:
            print(f"Ошибка при добавлении колонки: {e}")

# Создаем все таблицы
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_phone_column()
    print("База данных успешно обновлена!") 
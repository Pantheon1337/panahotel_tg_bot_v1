from database import engine
from sqlalchemy import text

def migrate():
    with engine.connect() as conn:
        try:
            # Добавляем колонку phone
            conn.execute(text("ALTER TABLE users ADD COLUMN phone TEXT"))
            conn.commit()
            print("Миграция успешно выполнена!")
        except Exception as e:
            print(f"Ошибка при выполнении миграции: {e}")

if __name__ == "__main__":
    migrate() 
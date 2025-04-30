from database import Session, User

def check_users():
    session = Session()
    try:
        users = session.query(User).all()
        print("\nСписок пользователей в базе данных:")
        print("-" * 50)
        for user in users:
            print(f"ID: {user.id}")
            print(f"Telegram ID: {user.telegram_id}")
            print(f"Имя: {user.name}")
            print(f"Должность: {user.position}")
            print(f"Роль: {user.role}")
            print("-" * 50)
    finally:
        session.close()

if __name__ == "__main__":
    check_users() 
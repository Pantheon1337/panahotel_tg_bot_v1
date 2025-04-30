from database import Session, User, UserRole

def make_admin(telegram_id: int):
    session = Session()
    try:
        user = session.query(User).filter_by(telegram_id=telegram_id).first()
        
        if user:
            # Устанавливаем роль администратора напрямую
            user.role = UserRole.ADMIN
            session.commit()
            print(f"Пользователь {user.name} (ID: {telegram_id}) получил права администратора. Должность: {user.position}")
        else:
            print(f"Пользователь с ID {telegram_id} не найден")
    finally:
        session.close()

if __name__ == "__main__":
    # Введите ID пользователя, которого хотите сделать администратором
    telegram_id = int(input("Введите ID пользователя: "))
    make_admin(telegram_id) 
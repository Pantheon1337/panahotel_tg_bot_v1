from database import Base, engine

def recreate_database():
    # Удаляем все существующие таблицы
    Base.metadata.drop_all(engine)
    
    # Создаем все таблицы заново
    Base.metadata.create_all(engine)
    
    print("База данных успешно пересоздана!")

if __name__ == "__main__":
    recreate_database() 
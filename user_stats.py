from database import Session, User
from datetime import datetime
import csv
import os

def get_users_data():
    """
    Получает данные о всех пользователях из базы данных
    """
    session = Session()
    users = session.query(User).all()
    
    # Формируем список с данными пользователей
    users_data = []
    for user in users:
        users_data.append({
            'name': user.name,
            'phone': user.phone,  # Используем поле phone вместо position
            'position': user.position,  # Добавляем поле position
            'role': 'Администратор' if user.role.name == 'ADMIN' else 'Стажер',
            'registration_date': user.created_at.strftime('%d.%m.%Y %H:%M')
        })
    
    return users_data

def save_users_to_csv():
    """
    Сохраняет данные пользователей в CSV файл
    """
    users_data = get_users_data()
    
    # Создаем директорию для отчетов, если её нет
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Формируем имя файла с текущей датой
    filename = f'reports/users_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    
    # Записываем данные в CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'phone', 'position', 'role', 'registration_date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for user in users_data:
            writer.writerow(user)
    
    return filename

def format_users_data():
    """
    Форматирует данные пользователей для отображения в текстовом виде
    """
    users_data = get_users_data()
    
    if not users_data:
        return "В базе данных пока нет зарегистрированных пользователей."
    
    result = "📊 *Список зарегистрированных пользователей:*\n\n"
    
    for i, user in enumerate(users_data, 1):
        result += f"{i}. *{user['name']}*\n"
        result += f"   📱 Телефон: {user['phone']}\n"
        result += f"   👔 Должность: {user['position']}\n"
        result += f"   👤 Роль: {user['role']}\n"
        result += f"   📅 Дата регистрации: {user['registration_date']}\n\n"
    
    return result

if __name__ == "__main__":
    # Пример использования
    print(format_users_data())
    csv_file = save_users_to_csv()
    print(f"\nДанные сохранены в файл: {csv_file}") 
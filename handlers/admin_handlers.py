from aiogram import types
from aiogram.fsm.context import FSMContext
from database import Session, User, UserRole
from keyboards.menu_keyboards import get_admin_menu_keyboard, get_admin_panel_keyboard
from datetime import datetime, timedelta
from user_stats import format_users_data, save_users_to_csv

async def handle_admin_statistics(message: types.Message):
    session = Session()
    
    # Получаем статистику
    total_users = session.query(User).count()
    active_users = session.query(User).filter(User.last_activity != None).count()
    new_users = session.query(User).filter(User.created_at >= datetime.now() - timedelta(days=7)).count()
    
    text = (
        "📊 *Статистика*\n\n"
        f"• Всего пользователей: {total_users}\n"
        f"• Активных пользователей: {active_users}\n"
        f"• Новых пользователей за неделю: {new_users}\n\n"
        "Для экспорта данных в CSV используйте команду /export"
    )
    await message.answer(text, parse_mode="Markdown")

async def handle_admin_users(message: types.Message):
    """
    Обработчик для просмотра списка пользователей
    """
    session = Session()
    try:
        # Получаем всех пользователей
        users = session.query(User).all()
        
        # Форматируем список пользователей
        users_list = "👥 *Список пользователей*\n\n"
        for user in users:
            users_list += (
                f"• ID: {user.id}\n"
                f"  Имя: {user.full_name}\n"
                f"  Телефон: {user.phone}\n"
                f"  Должность: {user.position}\n"
                f"  Роль: {user.role}\n"
                f"  Дата регистрации: {user.created_at.strftime('%d.%m.%Y')}\n\n"
            )
        
        # Отправляем список пользователей
        await message.answer(users_list, parse_mode="Markdown")
        
        # Сохраняем данные в CSV и отправляем файл
        csv_file = save_users_to_csv()
        with open(csv_file, 'rb') as file:
            await message.answer_document(
                file,
                caption="📊 Список пользователей в формате CSV"
            )
    except Exception as e:
        await message.answer(f"Произошла ошибка при получении списка пользователей: {str(e)}")
    finally:
        session.close()

async def handle_admin_edit_content(message: types.Message):
    edit_keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📝 Редактировать текст")],
            [types.KeyboardButton(text="🖼️ Добавить изображение")],
            [types.KeyboardButton(text="📄 Добавить документ")],
            [types.KeyboardButton(text="🔙 В админ-панель")]
        ],
        resize_keyboard=True
    )
    
    await message.answer(
        "📝 *Редактирование контента*\n\n"
        "Выберите тип контента для редактирования:",
        reply_markup=edit_keyboard,
        parse_mode="Markdown"
    )

async def handle_admin_back(message: types.Message):
    await message.answer(
        "👨‍💼 *Панель администратора*\n\n"
        "Выберите действие:",
        reply_markup=get_admin_panel_keyboard(),
        parse_mode="Markdown"
    )

async def handle_admin_to_main_menu(message: types.Message):
    await message.answer(
        "Выберите раздел:",
        reply_markup=get_admin_menu_keyboard()
    ) 
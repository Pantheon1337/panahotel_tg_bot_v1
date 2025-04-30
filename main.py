from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
import asyncio
import logging
from datetime import datetime
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import BOT_TOKEN, ADMIN_ROLE
from database import Session, User, UserRole
from keyboards.menu_keyboards import (
    get_role_keyboard,
    get_main_keyboard,
    get_admin_panel_keyboard,
    get_learning_menu_keyboard,
    get_admin_room_fund_keyboard,
    get_admin_menu_keyboard,
    get_trainee_menu_keyboard,
    get_admin_keyboard,
    get_trainee_keyboard,
    get_about_hotel_keyboard,
    get_opera_keyboard
)
from handlers.menu_handlers import (
    handle_standards,
    handle_about_company,
    handle_food,
    handle_halls,
    handle_contacts,
    handle_accessible_room,
    handle_back_to_menu,
    handle_back_to_main_menu,
    handle_tary_cafe,
    handle_halal,
    handle_banquet_hall,
    handle_conference_hall,
    handle_standard_room,
    handle_family_room,
    handle_studio_with_kitchen,
    handle_studio,
    handle_learning,
    handle_faq,
    handle_introduction,
    handle_service_standards,
    handle_managers,
    handle_general_manager,
    handle_operations_manager,
    handle_food_service_director,
    handle_sales_director,
    handle_technical_director,
    handle_chef,
    handle_navigation,
    handle_minus_first_floor,
    handle_first_floor,
    handle_second_floor,
    handle_offices,
    handle_tary_menu,
    handle_main_dishes,
    handle_appetizers,
    handle_soups,
    handle_desserts,
    handle_drinks,
    handle_currency_exchange,
    handle_parking,
    handle_location,
    handle_stay_conditions,
    handle_extra_bed,
    handle_pets,
    handle_late_checkout,
    handle_early_checkin,
    handle_main_conditions,
    handle_opera,
    handle_new,
    handle_checkin,
    handle_learning_back,
    handle_room_fund_info,
    handle_sport_hall,
    handle_checkout,
    handle_salary,
    handle_vacation,
    handle_sick_leave
)
from handlers.admin_handlers import (
    handle_admin_statistics,
    handle_admin_users,
    handle_admin_edit_content,
    handle_admin_back,
    handle_admin_to_main_menu
)

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Состояния для авторизации
class AuthStates(StatesGroup):
    waiting_for_role = State()

# Удаляем состояния авторизации
class RegistrationState(StatesGroup):
    full_name = State()
    phone = State()
    role = State()

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Получение роли пользователя
async def get_user_role(user_id: int) -> UserRole:
    session = Session()
    try:
        user = session.query(User).filter_by(telegram_id=user_id).first()
        return user.role if user else None
    finally:
        session.close()

# Получение пользователя
async def get_user(user_id: int) -> User:
    session = Session()
    try:
        user = session.query(User).filter_by(telegram_id=user_id).first()
        return user
    finally:
        session.close()

# Проверка прав администратора
async def is_admin(user_id: int) -> bool:
    role = await get_user_role(user_id)
    return role == UserRole.ADMIN if role else False

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    user = await get_user(user_id)
    
    if user:
        if user.role == UserRole.ADMIN:
            await message.answer(
                "Добро пожаловать в бот отеля! Выберите раздел:",
                reply_markup=get_admin_menu_keyboard()
            )
        else:
            await message.answer(
                "Добро пожаловать в бот отеля! Выберите раздел:",
                reply_markup=get_trainee_menu_keyboard()
            )
    else:
        await message.answer(
            "Добро пожаловать! Пожалуйста, выберите вашу роль:",
            reply_markup=get_role_keyboard()
        )
        await state.set_state(AuthStates.waiting_for_role)

@dp.message(AuthStates.waiting_for_role)
async def process_role(message: types.Message, state: FSMContext):
    """Обработчик выбора роли"""
    role_text = message.text.lower()
    
    if role_text not in ["администратор", "стажер"]:
        await message.answer("Пожалуйста, выберите роль из предложенных вариантов:",
                           reply_markup=get_role_keyboard())
        return
    
    # Обновляем роль существующего пользователя или создаем нового
    session = Session()
    user = session.query(User).filter(User.telegram_id == message.from_user.id).first()
    
    if user:
        # Обновляем роль существующего пользователя
        user.role = UserRole.ADMIN if role_text == "администратор" else UserRole.TRAINEE
        user.last_activity = datetime.now()
    else:
        # Создаем нового пользователя
        new_user = User(
            telegram_id=message.from_user.id,
            role=UserRole.ADMIN if role_text == "администратор" else UserRole.TRAINEE
        )
        session.add(new_user)
    
    session.commit()
    session.close()
    
    # Показываем соответствующее меню
    if role_text == "администратор":
        await message.answer("Вы выбрали роль администратора. Добро пожаловать!",
                           reply_markup=get_admin_menu_keyboard())
    else:
        await message.answer("Вы выбрали роль стажера. Добро пожаловать!",
                           reply_markup=get_trainee_menu_keyboard())
    
    await state.clear()

# Обработчик команды /admin
@dp.message(Command("admin"))
async def cmd_admin(message: types.Message):
    if not await is_admin(message.from_user.id):
        await message.answer("❌ У вас нет прав администратора")
        return

    await message.answer(
        "👨‍💼 *Панель администратора*\n\n"
        "Выберите действие:",
        reply_markup=get_admin_panel_keyboard(),
        parse_mode="Markdown"
    )

# Обработчик команды /moder
@dp.message(Command("moder"))
async def cmd_moder(message: types.Message):
    if not await is_admin(message.from_user.id):
        await message.answer("❌ У вас нет прав модератора")
        return

    await message.answer(
        "👨‍💼 *Панель модератора*\n\n"
        "Выберите действие:",
        reply_markup=get_admin_panel_keyboard(),
        parse_mode="Markdown"
    )

# Обработчик команды /role
@dp.message(Command("role"))
async def cmd_role(message: types.Message, state: FSMContext):
    """Обработчик команды /role для перевыбора роли"""
    # Предлагаем выбрать новую роль
    await message.answer("Пожалуйста, выберите новую роль:",
                       reply_markup=get_role_keyboard())
    await state.set_state(AuthStates.waiting_for_role)

# Удаляем обработчики состояний авторизации
@dp.message(RegistrationState.full_name)
async def process_full_name(message: types.Message, state: FSMContext):
    pass

@dp.message(RegistrationState.phone)
async def process_phone(message: types.Message, state: FSMContext):
    pass

@dp.message(RegistrationState.role)
async def process_role(message: types.Message, state: FSMContext):
    pass

# Обработчик кнопки обучения
@dp.message(F.text == "📚 Обучение")
async def handle_learning(message: types.Message, state: FSMContext):
    await state.update_data(previous_menu="main")
    await message.answer(
        "Выберите раздел:",
        reply_markup=get_learning_menu_keyboard(await get_user_role(message.from_user.id))
    )

# Регистрация обработчиков для основных кнопок меню
dp.message.register(handle_standards, F.text == "🏠 Номерной фонд")
dp.message.register(handle_about_company, F.text == "ℹ️ Об отеле")
dp.message.register(handle_contacts, F.text == "📞 Контакты")
dp.message.register(handle_learning, F.text == "📚 Обучение")

# Регистрация обработчиков для номерного фонда
dp.message.register(handle_accessible_room, F.text == "Для людей с ограниченными возможностями")
dp.message.register(handle_standard_room, F.text == "Стандарт")
dp.message.register(handle_family_room, F.text == "Семейный")
dp.message.register(handle_studio_with_kitchen, F.text == "Студия с кухней")
dp.message.register(handle_studio, F.text == "Студия")

# Регистрация обработчиков для раздела "Об отеле"
dp.message.register(handle_food, F.text == "🍽️ Питание")
dp.message.register(handle_halls, F.text == "🎪 Залы")
dp.message.register(handle_tary_cafe, F.text == "🍽️ Кафе Tary")
dp.message.register(handle_halal, F.text == "🕌 Халяль")
dp.message.register(handle_banquet_hall, F.text == "Банкетный зал")
dp.message.register(handle_conference_hall, F.text == "Конференц-зал")
dp.message.register(handle_opera, F.text == "🖥️ Opera")
dp.message.register(handle_location, F.text == "📍 Расположение")
dp.message.register(handle_currency_exchange, F.text == "💰 Обмен валют")
dp.message.register(handle_parking, F.text == "🅿️ Парковка")
dp.message.register(handle_stay_conditions, F.text == "📋 Условия проживания")
dp.message.register(handle_extra_bed, F.text == "🛏️ Дополнительная кровать")
dp.message.register(handle_pets, F.text == "🐾 Проживание с животными")
dp.message.register(handle_late_checkout, F.text == "⌛ Поздний выезд")
dp.message.register(handle_early_checkin, F.text == "⏰ Ранний заезд")
dp.message.register(handle_main_conditions, F.text == "📜 Основные условия")

# Регистрация обработчиков для меню обучения
dp.message.register(handle_introduction, F.text == "👨‍💼 Введение в должность")
dp.message.register(handle_service_standards, F.text == "🤝 Стандарты обслуживания")
dp.message.register(handle_managers, F.text == "👥 Руководители отделов")
dp.message.register(handle_learning_back, F.text == "🔙 Назад")

# Регистрация обработчиков для руководителей
dp.message.register(handle_general_manager, F.text == "Генеральный менеджер")
dp.message.register(handle_operations_manager, F.text == "Операционный менеджер")
dp.message.register(handle_food_service_director, F.text == "Директор службы питания")
dp.message.register(handle_sales_director, F.text == "Руководитель отдела продаж")
dp.message.register(handle_technical_director, F.text == "Руководитель технической службы")
dp.message.register(handle_chef, F.text == "Шеф-повар")

# Регистрация обработчиков для навигации
dp.message.register(handle_navigation, F.text == "🧭 Навигация")
dp.message.register(handle_minus_first_floor, F.text == "-1 этаж")
dp.message.register(handle_first_floor, F.text == "1 этаж")
dp.message.register(handle_second_floor, F.text == "2 этаж")
dp.message.register(handle_offices, F.text == "Офисы")

# Регистрация обработчиков для меню кафе Тары
dp.message.register(handle_tary_menu, F.text == "🍽️ Меню")
dp.message.register(handle_main_dishes, F.text == "🍽️ Основные блюда")
dp.message.register(handle_appetizers, F.text == "🥗 Закуски")
dp.message.register(handle_soups, F.text == "🥣 Супы")
dp.message.register(handle_desserts, F.text == "🍰 Десерты")
dp.message.register(handle_drinks, F.text == "☕ Напитки")

# Регистрация обработчиков для Opera
dp.message.register(handle_new, F.text == "Новое бронирование")
dp.message.register(handle_checkin, F.text == "Заселение")
dp.message.register(handle_checkout, F.text == "Выселение")
dp.message.register(handle_about_company, F.text == "🏢 Об отеле")

# Регистрация обработчиков для навигации по меню
dp.message.register(handle_back_to_menu, F.text == "🔙 Назад в меню")
dp.message.register(handle_back_to_main_menu, F.text == "🔙 В главное меню")

# Регистрация обработчиков админ-панели
dp.message.register(handle_admin_statistics, F.text == "📊 Статистика")
dp.message.register(handle_admin_users, F.text == "👥 Пользователи")
dp.message.register(handle_admin_edit_content, F.text == "📝 Редактировать контент")
dp.message.register(handle_admin_back, F.text == "🔙 В админ-панель")
dp.message.register(handle_admin_to_main_menu, F.text == "🔙 В главное меню")

# Регистрация обработчиков для кнопок "Об отеле" и "Обучение"
@dp.message(F.text == "🏠 Об отеле")
async def handle_about_hotel(message: types.Message, state: FSMContext):
    await state.update_data(previous_menu="main")
    await message.answer(
        "Выберите раздел:",
        reply_markup=get_about_hotel_keyboard()
    )

@dp.message(F.text == "📚 Обучение")
async def handle_learning(message: types.Message, state: FSMContext):
    await state.update_data(previous_menu="main")
    await message.answer(
        "Выберите раздел:",
        reply_markup=get_learning_menu_keyboard(await get_user_role(message.from_user.id))
    )

@dp.message(F.text == "🖥️ Opera")
async def handle_opera(message: types.Message, state: FSMContext):
    await state.update_data(previous_menu="main")
    await message.answer(
        "Выберите раздел:",
        reply_markup=get_opera_keyboard()
    )

@dp.message(F.text == "💰 Обмен валют")
async def handle_currency_exchange(message: types.Message, state: FSMContext):
    await handle_currency_exchange(message, state)

@dp.message(F.text == "📍 Расположение")
async def handle_location(message: types.Message, state: FSMContext):
    await handle_location(message, state)

@dp.message(F.text == "👥 Руководство")
async def handle_managers(message: types.Message, state: FSMContext):
    await handle_managers(message, state)

@dp.message(F.text == "🤝 Стандарты обслуживания")
async def handle_service_standards(message: types.Message, state: FSMContext):
    await handle_service_standards(message, state)

@dp.message(F.text == "🔙 Назад в меню")
async def handle_back_to_menu(message: types.Message, state: FSMContext):
    await handle_back_to_menu(message, state)

@dp.message(F.text == "🔙 В главное меню")
async def handle_back_to_main_menu(message: types.Message, state: FSMContext):
    await handle_back_to_main_menu(message, state)

# Регистрация обработчиков для кнопок
dp.message.register(handle_room_fund_info, F.text == "ℹ️ Информация")
dp.message.register(handle_sport_hall, F.text == "Спорт зал")

@dp.message(F.text == "ℹ️ Информация")
async def handle_room_fund_info(message: types.Message, state: FSMContext):
    """Обработчик кнопки 'Информация' в разделе 'Номерной фонд'"""
    await state.update_data(previous_menu="room_fund")
    await message.answer(
        "ℹ️ *Информация о номерном фонде*\n\n"
        "В нашем отеле представлены следующие типы номеров:\n\n"
        "• Стандарт - 21 кв.м., одна двуспальная кровать\n"
        "• Семейный - 21 кв.m., одна большая кровать и дополнительное кресло-кровать\n"
        "• Студия с кухней - 34 кв.m., полностью оборудованная кухня\n"
        "• Студия - 34 кв.m., просторная планировка\n"
        "• Для людей с ограниченными возможностями - 30 кв.m., специально оборудованный номер\n\n"
        "Все номера оснащены:\n"
        "• Кондиционером\n"
        "• Телевизором\n"
        "• Мини-баром\n"
        "• Сейфом\n"
        "• Бесплатным Wi-Fi\n"
        "• Телефоном\n"
        "• Феном\n"
        "• Набором полотенец\n"
        "• Туалетными принадлежностями",
        reply_markup=get_admin_room_fund_keyboard(),
        parse_mode="Markdown"
    )

# Регистрация обработчиков для кнопок меню
dp.message.register(handle_back_to_main_menu, F.text == "◀️ Назад в главное меню")
dp.message.register(handle_about_hotel, F.text == "🏨 Об отеле")
dp.message.register(handle_stay_conditions, F.text == "📋 Условия проживания")
dp.message.register(handle_learning, F.text == "📚 Обучение")
dp.message.register(handle_salary, F.text == "💰 Заработная плата")
dp.message.register(handle_vacation, F.text == "🏖️ Отпуск")
dp.message.register(handle_sick_leave, F.text == "🏥 Больничный")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 
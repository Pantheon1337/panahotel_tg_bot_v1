from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from database import UserRole

def get_back_to_menu_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру с кнопкой 'Назад в меню'"""
    keyboard = [
        [KeyboardButton(text="🔙 Назад в меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_role_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для выбора роли"""
    keyboard = [
        [KeyboardButton(text="Администратор")],
        [KeyboardButton(text="Стажер")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_main_keyboard(user_role: UserRole = None) -> ReplyKeyboardMarkup:
    """Создает единое главное меню для всех пользователей"""
    keyboard = [
        [KeyboardButton(text="🏠 Номерной фонд"), KeyboardButton(text="ℹ️ Об отеле")],
        [KeyboardButton(text="📚 Обучение"), KeyboardButton(text="📞 Контакты")],
        [KeyboardButton(text="🧭 Навигация"), KeyboardButton(text="📋 Условия проживания")],
        [KeyboardButton(text="🖥️ Opera")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_trainee_menu_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для стажера"""
    keyboard = [
        [KeyboardButton(text="🏠 Номерной фонд"), KeyboardButton(text="ℹ️ Об отеле")],
        [KeyboardButton(text="📚 Обучение"), KeyboardButton(text="📞 Контакты")],
        [KeyboardButton(text="🧭 Навигация"), KeyboardButton(text="📋 Условия проживания")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_admin_menu_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для администратора"""
    return get_main_keyboard()

def get_trainee_learning_menu_keyboard():
    keyboard = [
        [
            KeyboardButton(text="👨‍💼 Введение в должность"),
            KeyboardButton(text="🤝 Стандарты обслуживания")
        ],
        [
            KeyboardButton(text="👥 Руководители отделов"),
            KeyboardButton(text="👨‍💼 Управление персоналом")
        ],
        [
            KeyboardButton(text="💰 Заработная плата"),
            KeyboardButton(text="🏖️ Отпуск")
        ],
        [
            KeyboardButton(text="🏥 Больничный"),
            KeyboardButton(text="📊 Аналитика работы")
        ],
        [KeyboardButton(text="🔙 Назад в главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_admin_learning_menu_keyboard():
    keyboard = [
        [
            KeyboardButton(text="👨‍💼 Введение в должность"),
            KeyboardButton(text="🤝 Стандарты обслуживания")
        ],
        [
            KeyboardButton(text="👥 Руководители отделов"),
            KeyboardButton(text="👨‍💼 Управление персоналом")
        ],
        [
            KeyboardButton(text="💰 Заработная плата"),
            KeyboardButton(text="🏖️ Отпуск")
        ],
        [
            KeyboardButton(text="🏥 Больничный"),
            KeyboardButton(text="📊 Аналитика работы")
        ],
        [KeyboardButton(text="🔙 Назад в главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_learning_menu_keyboard(user_role: UserRole) -> ReplyKeyboardMarkup:
    """Создает клавиатуру для меню обучения"""
    keyboard = [
        [
            KeyboardButton(text="👨‍💼 Введение в должность"),
            KeyboardButton(text="🤝 Стандарты обслуживания")
        ],
        [
            KeyboardButton(text="👥 Руководители отделов"),
            KeyboardButton(text="💰 Заработная плата")
        ],
        [
            KeyboardButton(text="🏖️ Отпуск"),
            KeyboardButton(text="🏥 Больничный")
        ],
        [KeyboardButton(text="🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_trainee_tests_menu_keyboard():
    keyboard = [
        [
            KeyboardButton(text="📋 Тест: Стандарты работы"),
            KeyboardButton(text="🛡️ Тест: Безопасность")
        ],
        [
            KeyboardButton(text="🤝 Тест: Обслуживание"),
            KeyboardButton(text="📊 Мои результаты")
        ],
        [
            KeyboardButton(text="📈 Результаты команды"),
            KeyboardButton(text="📝 Создать тест")
        ],
        [KeyboardButton(text="🔙 Назад в главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_admin_tests_menu_keyboard():
    keyboard = [
        [
            KeyboardButton(text="📋 Тест: Стандарты работы"),
            KeyboardButton(text="🛡️ Тест: Безопасность")
        ],
        [
            KeyboardButton(text="🤝 Тест: Обслуживание"),
            KeyboardButton(text="📊 Мои результаты")
        ],
        [
            KeyboardButton(text="📈 Результаты команды"),
            KeyboardButton(text="📝 Создать тест")
        ],
        [KeyboardButton(text="🔙 Назад в главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_tests_menu_keyboard(user_role: UserRole = None):
    if user_role == UserRole.ADMIN:
        return get_admin_tests_menu_keyboard()
    return get_trainee_tests_menu_keyboard()

def get_admin_panel_keyboard():
    keyboard = [
        [KeyboardButton(text="📊 Статистика")],
        [KeyboardButton(text="👥 Пользователи")],
        [KeyboardButton(text="📝 Редактировать контент")],
        [KeyboardButton(text="🔙 В главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_room_types_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Стандарт"), KeyboardButton(text="Семейный")],
        [KeyboardButton(text="Студия с кухней"), KeyboardButton(text="Студия")],
        [KeyboardButton(text="🦽 Для людей с ограниченными возможностями")],
        [KeyboardButton(text="🔙 Назад в меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_managers_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Генеральный менеджер"), KeyboardButton(text="Операционный менеджер")],
        [KeyboardButton(text="Директор службы питания"), KeyboardButton(text="Руководитель отдела продаж")],
        [KeyboardButton(text="Руководитель технической службы"), KeyboardButton(text="Шеф-повар")],
        [KeyboardButton(text="🔙 Назад в меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_room_fund_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Стандарт")],
        [KeyboardButton(text="Стандарт для людей с ограниченными возможностями")],
        [KeyboardButton(text="Люкс")],
        [KeyboardButton(text="Сьюит")],
        [KeyboardButton(text="⬅️ Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_food_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="🍽️ Кафе Tary"), KeyboardButton(text="🕌 Халяль")],
        [KeyboardButton(text="🔙 Назад в меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_halls_menu_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для категории 'Залы'"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Банкетный зал"),
                KeyboardButton(text="Конференц-зал")
            ],
            [
                KeyboardButton(text="Спорт зал")
            ],
            [
                KeyboardButton(text="🔙 Назад в меню")
            ]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_about_hotel_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для раздела 'Об отеле'"""
    keyboard = [
        [KeyboardButton(text="🍽️ Питание"), KeyboardButton(text="🎪 Залы")],
        [KeyboardButton(text="📍 Расположение"), KeyboardButton(text="💰 Обмен валют")],
        [KeyboardButton(text="🅿️ Парковка")],
        [KeyboardButton(text="🔙 Назад в меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_admin_about_hotel_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для раздела 'Об отеле' для администратора"""
    return get_about_hotel_keyboard()

def get_trainee_about_hotel_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для раздела 'Об отеле' для стажера"""
    return get_about_hotel_keyboard()

def get_stay_conditions_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для раздела 'Условия проживания'"""
    keyboard = [
        [KeyboardButton(text="🛏️ Дополнительная кровать"), KeyboardButton(text="🐾 Проживание с животными")],
        [KeyboardButton(text="⌛ Поздний выезд"), KeyboardButton(text="⏰ Ранний заезд")],
        [KeyboardButton(text="📜 Основные условия")],
        [KeyboardButton(text="🔙 Назад в меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_navigation_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="-1 этаж"), KeyboardButton(text="1 этаж")],
        [KeyboardButton(text="2 этаж"), KeyboardButton(text="Офисы")],
        [KeyboardButton(text="🔙 Назад в меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_tary_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="🍽️ Основные блюда"), KeyboardButton(text="🥗 Закуски")],
        [KeyboardButton(text="🥣 Супы"), KeyboardButton(text="🍰 Десерты")],
        [KeyboardButton(text="☕ Напитки")],
        [KeyboardButton(text="🔙 Назад в меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_opera_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для меню Opera"""
    keyboard = [
        [KeyboardButton(text="Новое бронирование"), KeyboardButton(text="Заселение")],
        [KeyboardButton(text="Выселение")],
        [KeyboardButton(text="🔙 Назад в меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_admin_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для администратора"""
    keyboard = [
        [KeyboardButton(text="🏠 Номерной фонд"), KeyboardButton(text="ℹ️ Об отеле")],
        [KeyboardButton(text="📚 Обучение"), KeyboardButton(text="📞 Контакты")],
        [KeyboardButton(text="🧭 Навигация"), KeyboardButton(text="📋 Условия проживания")],
        [KeyboardButton(text="🖥️ Opera")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_trainee_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для стажера"""
    keyboard = [
        [KeyboardButton(text="🏠 Номерной фонд"), KeyboardButton(text="ℹ️ Об отеле")],
        [KeyboardButton(text="📚 Обучение"), KeyboardButton(text="📞 Контакты")],
        [KeyboardButton(text="🧭 Навигация"), KeyboardButton(text="📋 Условия проживания")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_admin_room_fund_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для категории 'Номерной фонд' администратора"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Стандарт"),
                KeyboardButton(text="Семейный")
            ],
            [
                KeyboardButton(text="Студия с кухней"),
                KeyboardButton(text="Студия")
            ],
            [
                KeyboardButton(text="Для людей с ограниченными возможностями"),
                KeyboardButton(text="ℹ️ Информация")
            ],
            [
                KeyboardButton(text="🔙 Назад в меню")
            ]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_trainee_room_fund_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для категории 'Номерной фонд' стажера"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Стандарт"),
                KeyboardButton(text="Семейный")
            ],
            [
                KeyboardButton(text="Студия с кухней"),
                KeyboardButton(text="Студия")
            ],
            [
                KeyboardButton(text="Для людей с ограниченными возможностями"),
                KeyboardButton(text="ℹ️ Информация")
            ],
            [
                KeyboardButton(text="🔙 Назад в меню")
            ]
        ],
        resize_keyboard=True
    )
    return keyboard 
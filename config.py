from dotenv import load_dotenv
import os

load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Роли пользователей
ADMIN_ROLE = "admin"
MODERATOR_ROLE = "moderator"
USER_ROLE = "user"

# Состояния FSM
class States:
    WAITING_FOR_NAME = "waiting_for_name"
    WAITING_FOR_POSITION = "waiting_for_position"
    WAITING_FOR_START_DATE = "waiting_for_start_date"
    WAITING_FOR_TEST_ANSWER = "waiting_for_test_answer"
    WAITING_FOR_QUESTION = "waiting_for_question" 
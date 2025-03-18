import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш бот. Как я могу помочь?')

# Обработчик текстовых сообщений
def echo(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    update.message.reply_text(f'Вы сказали: {user_text}')

def main() -> None:
    # Получаем токен из переменной окружения
    token = os.getenv('BOT_TOKEN')
    
    if not token:
        raise ValueError("Переменная окружения BOT_TOKEN не установлена!")

    # Создаем Updater и передаем ему токен вашего бота
    updater = Updater(token)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()

    # Работаем до тех пор, пока не будет нажата комбинация Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()

from django.core.management.base import BaseCommand
import telebot


bot = telebot.TeleBot("6868586010:AAH3RxUnlwzB3iBJacKdb3-VjpwWVwQ80C0")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Отправьте фотографию картины")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Здесь функция для распознования человека
    bot.reply_to(message, "Спасибо за фотографию!")
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path

    # Download the photo
    downloaded_file = bot.download_file(file_path)

    # Define a path to save the photo
    photo_path = f'/Users/tomiris/Desktop/bot/myproject/images/{file_id}.jpg'

    print(f"Photo downloaded and saved to {photo_path}")


@bot.message_handler(func=lambda message: True)
def handle_other(message):
    bot.reply_to(message, "Пожалуйста, отправьте фотографию.")

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

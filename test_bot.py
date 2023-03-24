

# !pip install pyTelegramBotAPI
# !pip install Faker
# !pip install random
from faker import Faker
# подключение библиотек
import json
import random
from secrets import token_urlsafe
from telebot import TeleBot, types


# TODO: вставить свой токен
TOKEN = '5890687341:AAEMDt-2IawvJdBNTR5RaHXfe6yE1dWCFnY'
bot = TeleBot(TOKEN, parse_mode='html')
# утилита для генерации номеров кредитных карт
# указываем язык - русский
faker = Faker('ru_RU') 

# объект клавиаутры
main_menu_reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# первый ряд кнопок
main_menu_reply_markup.row(
    types.KeyboardButton(text="Издания"), types.KeyboardButton(text="Конференции")
)
# второй ряд кнопок
main_menu_reply_markup.row(
    types.KeyboardButton(text="Статьи"), types.KeyboardButton(text="Экспертиза")
)

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_message_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    # не забываем прикрепить объект клавиатуры к сообщению
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет!\nНужны данные для тестирования заявок? "\
        "Просто выбери тип заявки 👇🏻",
        reply_markup=main_menu_reply_markup
    )


# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # определяем количество тестовых пользователей
    # или отправляем ошибку
    payload_len = 0
    if message.text == "Издания":
        payload_len = 1
        total_payload = []
        for _ in range(payload_len):
          user_phone = f'+7{faker.msisdn()[3:]}'
          user_mail = faker.company_email()
          user_name = faker.name()
          color_info = faker.safe_color_name()
          date_info = faker.date()
          text_info1 = faker.text()
          text_info2 = faker.text()
          text_info3 = faker.text()
          text_info4 = faker.text()
          total_payload.append(user_phone)
          total_payload.append(user_name)
          total_payload.append(user_mail)
          total_payload.append(color_info)
          total_payload.append(date_info)
          total_payload.append(text_info1)
          total_payload.append(text_info2)
          total_payload.append(text_info3)
          total_payload.append(text_info4)
          payload_str = json.dumps(
          obj=total_payload,
          indent=9,
          sort_keys=True,
          ensure_ascii=False,
          default=str
    )
          bot.send_message(
            chat_id=message.chat.id,
            text=f"Данные тестовой заявки:\n<code>"\
            f"{payload_str}</code>"
          )
    elif message.text == "Конференции":
        payload_len = 1
        total_payload = []
        for _ in range(payload_len):
          user_phone = f'+7{faker.msisdn()[3:]}'
          user_mail = faker.company_email()
          user_name = faker.name()
          date_info = faker.date()
          text_info1 = faker.text()
          text_info2 = faker.text()
          text_info3 = faker.text()
          total_payload.append(user_phone)
          total_payload.append(user_name)
          total_payload.append(user_mail)
          total_payload.append(date_info)
          total_payload.append(text_info1)
          total_payload.append(text_info2)
          total_payload.append(text_info3)
          payload_str = json.dumps(
          obj=total_payload,
          indent=7,
          sort_keys=True,
          ensure_ascii=False,
          default=str
    )
          bot.send_message(
            chat_id=message.chat.id,
            text=f"Данные тестовой заявки:\n<code>"\
            f"{payload_str}</code>"
          )
    elif message.text == "Статьи":
        payload_len = 1
        total_payload = []
        for _ in range(payload_len):
          year = faker.year()
          text_info1 = faker.text()
          text_info2 = faker.text()
          text_info3 = faker.text()
          number1= random.randint(0, 200)
          number2= faker.ipv4()
          number3= faker.iana_id()
          link=faker.uri()
          total_payload.append(year)
          total_payload.append(number1)
          total_payload.append(number2)
          total_payload.append(number3)
          total_payload.append(text_info1)
          total_payload.append(text_info2)
          total_payload.append(text_info3)
          total_payload.append(link)
          payload_str = json.dumps(
          obj=total_payload,
          indent=8,
          sort_keys=True,
          ensure_ascii=False,
          default=str
    )
          bot.send_message(
            chat_id=message.chat.id,
            text=f"Данные тестовой заявки:\n<code>"\
            f"{payload_str}</code>"
          )
    elif message.text == "Экспертиза":
        payload_len = 1
        total_payload = []
        for _ in range(payload_len):
          country = faker.country()
          city = faker.city()
          text_info1 = faker.text()
          text_info2 = faker.text()
          text_info3 = faker.text()
          text_info4 = faker.text()
          date_info1 = faker.date()
          date_info2 = faker.date()
          date_info3 = faker.date()
          total_payload.append(country)
          total_payload.append(city)
          total_payload.append(date_info1)
          total_payload.append(date_info2)
          total_payload.append(date_info3)
          total_payload.append(text_info1)
          total_payload.append(text_info2)
          total_payload.append(text_info3)
          total_payload.append(text_info4)
          payload_str = json.dumps(
          obj=total_payload,
          indent=9,
          sort_keys=True,
          ensure_ascii=False,
          default=str
    )
          bot.send_message(
            chat_id=message.chat.id,
            text=f"Данные тестовой заявки:\n<code>"\
            f"{payload_str}</code>"
          )
    else:
        bot.send_message(chat_id=message.chat.id, text="Не знаю что и ответить :(")
        return

   
    bot.send_message(
        chat_id=message.chat.id,
        text="Если нужны еще данные, можешь выбрать еще раз 👇🏻",
        reply_markup=main_menu_reply_markup
    )
    

# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
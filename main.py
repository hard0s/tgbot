import telebot

bot = telebot.TeleBot('6073497379:AAE0Qaq-GyLY1XMKnxGxjxcwXxHkxAAwAUk')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'гей, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_message(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, "ты гей", parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"твой id: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('test.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'мох':
        audio = open('mox.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Авдеева':
        bot.send_message(message.chat.id, 'https://vk.com/away.php?to=https%3A%2F%2Fvas3k.ru%2Fblog%2Fblockchain%2F&cc_key=')
    else :
        bot.send_message(message.chat.id, 'я тебя не понимаю', parse_mode='html')




bot.polling(none_stop=True)

import telebot

bot = telebot.TeleBot('6141289418:AAF3T3gS9gCuXMmVsf7F9NbIhoGA7BNlpkc')

@bot.message_handler(commands=['start'])

def start(message):
    mess = f'OPPYM@LenovoLaptop, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# 

@bot.message_handler()
def get_user_message(message):
    match (message.text):
        case "привет":
            bot.send_message(message.chat.id, "ты гей", parse_mode='html')
        case "id":
            bot.send_message(message.chat.id, f"твой id: {message.from_user.id}", parse_mode='html')
        case "photo":
                photo = open("test.jpg", "rb")
                bot.send_photo(message.chat.id, photo)
        case "rodrigo":
            photo = open("Rodrigo.png", "rb")
            bot.send_photo(message.chat.id, photo)        
        case "мох":
            audio = open('mox.mp3', 'rb')
            bot.send_audio(message.chat.id, audio)
        case "megadeth":
            audio = open("We\'ll Be Back.mp3", 'rb')
            bot.send_audio(message.chat.id, audio)
        case "Авдеева":
            bot.send_message(message.chat.id, 'https://vk.com/away.php?to=https%3A%2F%2Fvas3k.ru%2Fblog%2Fblockchain%2F&cc_key=')
        case _ :
            bot.send_message(message.chat.id, 'я тебя не понимаю', parse_mode='html')

bot.polling(none_stop=True)

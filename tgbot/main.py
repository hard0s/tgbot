import telebot
import config


bot = telebot.TeleBot(config.TOKEN)
 

@bot.message_handler()

def get_user_message(message):
    match (message.text):
        case 'Привет':
            bot.send_message(message.chat.id, "Привет", parse_mode='html')
        case 'Id':
            bot.send_message(message.chat.id, f"твой id: {message.from_user.id}", parse_mode='html')
        case "Понедельник":
            bot.send_message(message.chat.id, config.read1, parse_mode='html')
        case "Вторник":
            bot.send_message(message.chat.id, config.read2, parse_mode='html')
        case "Среда":
            bot.send_message(message.chat.id, config.read3, parse_mode='html')
        case "Четверг":
            bot.send_message(message.chat.id, config.read4, parse_mode='html')
        case "Пятница":
            bot.send_message(message.chat.id, config.read5, parse_mode='html')
        case _ :
            bot.send_animation(message.chat.id, config.unknown)
        
        
'''
@bot.message_handler()
def get_user_message(message) :
    match (message):
        case "привет":
            bot.send_message(message.chat.id, "ты гей", parse_mode='html')
        case "id":
            bot.send_message(message.chat.id, f"твой id: {message.from_user.id}", parse_mode='html')
        case "photo":
            photo = open('test.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        case "мох":
            audio = open('mox.mp3', 'rb')
            bot.send_audio(message.chat.id, audio)
        case "Авдеева":
            bot.send_message(message.chat.id, 'https://vk.com/away.php?to=https%3A%2F%2Fvas3k.ru%2Fblog%2Fblockchain%2F&cc_key=')
        case _ :
            bot.send_message(message.chat.id, 'я тебя не понимаю', parse_mode='html')
elif message.text == "вторник":
        f = open('rasp.txt', 'r') 
        for i in range (4,8):
            bot.send_message(message.chat.id, test)
'''
bot.polling(none_stop=True)

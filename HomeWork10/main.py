import telebot
from telebot import types


bot = telebot.TeleBot("6106582022:AAFGq0UOW-qkE0eEIqm3bCWi8ykySwuPFoU")

typeNums = 0

def log(message):
    file = open("db.csv", "a")
    file.write(f'{message}\n')
    file.close()

@bot.message_handler(commands=["start"])
def button(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("Рациональные")
        but2 = types.KeyboardButton("Комплексные")
        but3 = types.KeyboardButton("Выход")
        markup.add(but1)
        markup.add(but2)
        markup.add(but3)
        bot.send_message(message.chat.id, "Сделай выбор с какими числами работать", reply_markup=markup) 

@bot.message_handler(content_types = ["text"])

def buttons(message):
    log(message)
    global typeNums
    menu = types.ReplyKeyboardMarkup()
    if message.text == "Рациональные":
        bot.send_message(message.chat.id, "Работа с рациональными числами", reply_markup=menu)
        bot.send_message(message.chat.id, "Введите выражение разделяя пробелом")
        bot.register_next_step_handler(message, controller)
        typeNums = 0
    elif message.text == "Комплексные":
         bot.send_message(message.chat.id, "Работа с комплексными числами", reply_markup=menu)
         bot.send_message(message.chat.id, "Введите выражение разделяя пробелом")
         bot.register_next_step_handler(message, controller)
         typeNums = 1
    else:
        bot.send_message(exit)

        
def controller(message):
    line = message.text.split()
    if typeNums == 0:
        a = int(line[0])
        b = int(line[2])
    else:
        a = complex(line[0])
        b = complex(line[2])
    
    if line[1] == '+':
        res = a + b
    elif line[1] == '-':
        res = a - b
    elif line[1] == '*':
        res = a * b
    elif line[1] == '/':
        res = a / b
    elif typeNums == 1 and (line[1] == '//' or line[1] == '%'):
        bot.send_message(message.chat.id, "Данная операция невозможна с комплексными числами")
        bot.register_next_step_handler(message, controller)
    elif line[1] == '//':
        res = a // b
    elif line[1] == '%':
        res = a % b
    bot.send_message(message.chat.id, str(res))
    bot.register_next_step_handler(message, controller)


bot.infinity_polling()
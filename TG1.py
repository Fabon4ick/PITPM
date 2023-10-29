import telebot

bot = telebot.TeleBot('6828573113:AAHEQyBjSzr3runAAr-kn3WZiLhHVeUW2Gk')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, давай я отправлю тебе стикер?")
    elif message.text == "Давай":
        bot.send_message(message.from_user.id, "Напиши Стикер")
    elif message.text == "Стикер":
        bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEKkzNlNHQzwaKaA6CbSkW_CzNRjch58AAChAEAAj0N6ATiTiZoWEw2uTAE")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши 'Привет.'")


bot.polling(none_stop=True, interval=0)
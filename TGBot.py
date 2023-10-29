import telebot
from telebot import types
import random

bot = telebot.TeleBot('6828573113:AAHEQyBjSzr3runAAr-kn3WZiLhHVeUW2Gk')

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1


lives = 9
words = ['пицца', "ангел", "мираж", "носки", "выдра", "петух"]
secret_word = random.choice(words)
clue = list("?????")
heart_symbol = u'\u2764'
guessed_word_correctly = False
pred = '@'


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global pred, guessed_word_correctly, clue, secret_word, words, lives, heart_symbol
    guess = message.text
    if pred != '@':
        if lives > 0:
            if guess == secret_word or ''.join(clue) == secret_word:
                guessed_word_correctly = True
            if guess in secret_word:
                update_clue(guess, secret_word, clue)
            else:
                bot.send_message(message.chat.id, "Неправильно, вы теряете одну жизнь")
                lives -= 1
            if guessed_word_correctly:
                bot.send_message(message.chat.id, "Победа! Было загадано слово " + secret_word)
                lives = 9
                words = ['пицца', "ангел", "мираж", "носки", "выдра", "петух"]
                secret_word = random.choice(words)
                clue = list('?????')
                heart_symbol = u'\u2764'
                guessed_word_correctly = False

                pred = '@'
            mess = ''
            for x in clue:
                mess += str(x) + ''
            bot.send_message(message.chat.id, mess)
            mess = "Осталось жизней: " + heart_symbol * lives
            bot.send_message(message.chat.id, mess)
        else:
            bot.send_message(message.chat.id, 'Вы проиграли(')
            pred = '@'
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row('Играть еще раз')
            bot.send_message(message.chat.id, 'Хотите сыграть еще раз?', reply_markup=keyboard)
    else:
        pred = '1'
        bot.send_message(message.chat.id, 'Это игра "9 жизней". Попробуйте угадать слово!')
        mess = ''
        for x in clue:
            mess += str(x) + ' '
        bot.send_message(message.chat.id, mess)
        mess = "Осталось жизней: " + heart_symbol * lives
        bot.send_message(message.chat.id, mess)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Играть еще раз':
        global pred, guessed_word_correctly, clue, secret_word, words, lives, heart_symbol
        lives = 9
        secret_word = random.choice(words)
        clue = list("?????")
        guessed_word_correctly = False
        pred = '@'
        get_text_messages(message)


bot.polling(none_stop=True, interval=0)
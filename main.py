import sys
import threading
import json
from msilib.schema import Error
import re
import time
import telebot
from scrapper import scrap
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from db import pgdb, pgdbins, pgdbupd
from filtration import filt

#bot_token = "5333091432:AAEE-MtnYqdrHo1N09LRBHIFW_BexsCs2pQ"   #old token
bot_token = "5541786342:AAFy00RVCPHnF_4TNpjFGlucWVVxX7GvJhs"    #new token


# chat_id = ["865161907", "722830299", "735059361"]

 
bot = telebot.TeleBot(bot_token)
parse_mode = 'MARKDOWN'


def notif_markup(text, url):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text, url=url))
    return markup

#! function to test the bot
@bot.message_handler(commands=['new'])
def sendMessage(message):
    print("got message")
    try:
        msg = scrap(1)
        bot.send_message(message.chat.id, "\u2B55 "*10+"\n\n\U0001F4CC  *{0}*\n\n\U0001F4CE  {1}".format(
            msg["title"], msg["description"]), parse_mode, reply_markup=notif_markup("\U0001F4E5 Notification", msg["link"]))
    except Exception as e:
        print(e)

# A new feature :-
# When a use enters a number 'n'
# then the scrapper scrapes the n-th notification


# @bot.message_handler(content_types=['text'])
# def nthNotif(message):
#     print(message.text)
#     msg = scrap(int(message.text) - 1)
#     bot.send_message(message.chat.id, msg, parse_mode)


# This needs any message #########
# def scrapper(message):

#     return True


# @bot.message_handler(func=scrapper)
# def send(message):
#     bot.send_message(message.chat.id,msg,'MARKDOWN')
#     bot.send_message(message.chat.id,'*Notification*',parse_mode,reply_markup=notif_markup())


##################################

# Reply Keyboard
with open('prg_sem_data.json') as json_file:
    prg_sem = json.load(json_file)


def prg_Markup():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    button_list = [
        KeyboardButton(prg) for prg in prg_sem
    ]
    markup.add(*button_list)
    return markup


def sem_Markup(sem):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    button_list = [
        KeyboardButton("S{}".format(sem)) for sem in range(1, sem+1)
    ]
    markup.add(*button_list)
    return markup


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, "*Welcome to\nKTU Personal Updates Bot*",
                     parse_mode)
    bot.send_message(message.chat.id,
                     "Select your *Program*",
                     parse_mode,
                     reply_markup=prg_Markup())


@bot.message_handler(content_types=['text'])
def data_collection(msg):
    if msg.text in prg_sem:

        pgdbins(msg.chat.id,msg.text)

        # print(msg.text+"\t"+str(msg.chat.id))
        try:
            bot.send_message(msg.chat.id,
                             "Select your *Semester*",
                             parse_mode,
                             reply_markup=sem_Markup(prg_sem[msg.text]))
        except Exception as e:
            print(e)

    elif(re.search("S*", msg.text)):
        # print(msg.text+"\t"+str(msg.chat.id))
        pgdbupd(msg.chat.id,msg.text)
        bot.send_message(msg.chat.id,
                         "_Let's start our journey together_",
                         parse_mode)


def send():
    while True:
        # print("running the job...")
        # bot.send_message(int(865161907), "hai")
        # time.sleep(60)
        listnot=scrap()
        # print(len(listnot))
        if(len(listnot)!=0):
            for i in reversed(range(len(listnot))):
                    listabc=filt(listnot[i]["title"])
                    print(listabc)
                    try:
                        chatids=pgdb(listabc)
                    except Exception as e:
                        print(e)
                    # print(chatids)
                    if(len(chatids)!=0):
                        for chat_id in chatids:
                            
                          bot.send_message(chat_id, "\u2B55 "*10+"\n\n\U0001F4CC  *{0}*\n\n\U0001F4CE  {1}".format(
                    listnot[i]["title"], listnot[i]["description"]), parse_mode, reply_markup=notif_markup("\U0001F4E5 Notification",listnot[i]["link"]))
                    else:
                        print("no entry for that combo")
        time.sleep(9000)

def main():

    try:

        print("trying to thread...")
        t = threading.Thread(target=send, daemon=True)
        t.start()
        print("thread started")

        bot.polling(non_stop=True)

        while t.is_alive():
            t.join(1)
    except KeyboardInterrupt:
        print("exiting...")
        sys.exit(1)


if __name__ == '__main__':
    main()

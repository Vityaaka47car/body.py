import re
import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot('Вставляете свой')

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton(text='Понедельник')
    markup.add(keyboard)
    keyboard2 = types.KeyboardButton(text='Вторник')
    markup.add(keyboard2)
    keyboard3 = types.KeyboardButton(text='Среда')
    markup.add(keyboard3)
    keyboard4 = types.KeyboardButton(text='Четверг')
    markup.add(keyboard4)
    keyboard5 = types.KeyboardButton(text='Пятница')
    markup.add(keyboard5)
    keyboard6 = types.KeyboardButton(text='Суббота')
    markup.add(keyboard6)

    bot.send_message(chat_id, f'Привет {first_name}!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Понедельник':
            url = 'https://www.sptkaluga.ru/pon'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            dirty_string = str(soup.find('div', class_="main_content"))
            middle_list = re.split("<|>", dirty_string)
            predfinish_list = []
            for i in middle_list:
                f = i[:2]
                if f == '1)' or f == '2)' or f == '3)' or f == '4)':
                    predfinish_list.append(i)

            finish_list = []
            for i in predfinish_list[1:6]:
                f = i[:2]
                if f == '1)':
                    k = predfinish_list.index(i)
                    l = k + 1
                    h = k + 2
                    finish_list.append(i)
                    for s in predfinish_list[l:h]:
                        r = s[:2]
                        if r == '2)':
                            two = predfinish_list.index(s)
                            two1 = two + 1
                            two2 = two + 2
                            finish_list.append(s)
                            for thre in predfinish_list[two1:two2]:
                                d = thre[:2]
                                if d == '3)':
                                    three = predfinish_list.index(thre)
                                    three1 = three + 1
                                    three2 = three + 2
                                    finish_list.append(thre)
                                    for four in predfinish_list[three1:three2]:
                                        j = four[:2]
                                        if j == '4)':
                                            fourr = predfinish_list.index(four)
                                            fourr1 = fourr + 1
                                            fourr2 = fourr + 2
                                            finish_list.append(four)

            finishListReal = []
            compareNum = int(finish_list[0][0])
            for elem in finish_list:
                currNum = int(elem[0])
                if currNum < compareNum:
                    break;
                finishListReal.append(elem)
                compareNum = currNum

            finish_string = "\n".join(finishListReal)

            bot.send_message(chat_id, f'Расписание на понедельник: \n{finish_string}')



        elif message.text == 'Вторник':
            url = 'https://www.sptkaluga.ru/vtor'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            dirty_string = str(soup.find('div', class_="main_content"))
            middle_list = re.split("<|>", dirty_string)
            predfinish_list = []
            for i in middle_list:
                f = i[:2]
                if f == '1)' or f == '2)' or f == '3)' or f == '4)':
                    predfinish_list.append(i)

            finish_list = []
            for i in predfinish_list[1:7]:
                f = i[:2]
                if f == '1)':
                    k = predfinish_list.index(i)
                    l = k + 1
                    h = k + 2
                    finish_list.append(i)
                    for s in predfinish_list[l:h]:
                        r = s[:2]
                        if r == '2)':
                            two = predfinish_list.index(s)
                            two1 = two + 1
                            two2 = two + 2
                            finish_list.append(s)
                            for thre in predfinish_list[two1:two2]:
                                d = thre[:2]
                                if d == '3)':
                                    three = predfinish_list.index(thre)
                                    three1 = three + 1
                                    three2 = three + 2
                                    finish_list.append(thre)
                                    for four in predfinish_list[three1:three2]:
                                        j = four[:2]
                                        if j == '4)':
                                            fourr = predfinish_list.index(four)
                                            fourr1 = fourr + 1
                                            fourr2 = fourr + 2
                                            finish_list.append(four)

            finishListReal = []
            compareNum = int(finish_list[0][0])
            for elem in finish_list:
                currNum = int(elem[0])
                if currNum < compareNum:
                    break;
                finishListReal.append(elem)
                compareNum = currNum

            finish_string = "\n".join(finishListReal)

            bot.send_message(chat_id, f'Расписание на вторник: \n{finish_string}')



        elif message.text == 'Среда':
            url = 'https://www.sptkaluga.ru/sreda'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            dirty_string = str(soup.find('div', class_="main_content"))
            middle_list = re.split("<|>", dirty_string)
            predfinish_list = []
            for i in middle_list:
                f = i[:2]
                if f == '1)' or f == '2)' or f == '3)' or f == '4)':
                    predfinish_list.append(i)

            finish_list = []
            for i in predfinish_list[1:7]:
                f = i[:2]
                if f == '1)':
                    k = predfinish_list.index(i)
                    l = k + 1
                    h = k + 2
                    finish_list.append(i)
                    for s in predfinish_list[l:h]:
                        r = s[:2]
                        if r == '2)':
                            two = predfinish_list.index(s)
                            two1 = two + 1
                            two2 = two + 2
                            finish_list.append(s)
                            for thre in predfinish_list[two1:two2]:
                                d = thre[:2]
                                if d == '3)':
                                    three = predfinish_list.index(thre)
                                    three1 = three + 1
                                    three2 = three + 2
                                    finish_list.append(thre)
                                    for four in predfinish_list[three1:three2]:
                                        j = four[:2]
                                        if j == '4)':
                                            fourr = predfinish_list.index(four)
                                            fourr1 = fourr + 1
                                            fourr2 = fourr + 2
                                            finish_list.append(four)

            finishListReal = []
            compareNum = int(finish_list[0][0])
            for elem in finish_list:
                currNum = int(elem[0])
                if currNum < compareNum:
                    break;
                finishListReal.append(elem)
                compareNum = currNum

            finish_string = "\n".join(finishListReal)

            bot.send_message(chat_id, f'Расписание на среду: \n{finish_string}')



        elif message.text == 'Четверг':
            url = 'https://www.sptkaluga.ru/chetv'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            dirty_string = str(soup.find('div', class_="main_content"))
            middle_list = re.split("<|>", dirty_string)
            predfinish_list = []
            for i in middle_list:
                f = i[:2]
                if f == '1)' or f == '2)' or f == '3)' or f == '4)':
                    predfinish_list.append(i)

            finish_list = []
            for i in predfinish_list[1:7]:
                f = i[:2]
                if f == '1)':
                    k = predfinish_list.index(i)
                    l = k + 1
                    h = k + 2
                    finish_list.append(i)
                    for s in predfinish_list[l:h]:
                        r = s[:2]
                        if r == '2)':
                            two = predfinish_list.index(s)
                            two1 = two + 1
                            two2 = two + 2
                            finish_list.append(s)
                            for thre in predfinish_list[two1:two2]:
                                d = thre[:2]
                                if d == '3)':
                                    three = predfinish_list.index(thre)
                                    three1 = three + 1
                                    three2 = three + 2
                                    finish_list.append(thre)
                                    for four in predfinish_list[three1:three2]:
                                        j = four[:2]
                                        if j == '4)':
                                            fourr = predfinish_list.index(four)
                                            fourr1 = fourr + 1
                                            fourr2 = fourr + 2
                                            finish_list.append(four)

            finishListReal = []
            compareNum = int(finish_list[0][0])
            for elem in finish_list:
                currNum = int(elem[0])
                if currNum < compareNum:
                    break;
                finishListReal.append(elem)
                compareNum = currNum

            finish_string = "\n".join(finishListReal)

            bot.send_message(chat_id, f'Расписание на четверг: \n{finish_string}')



        elif message.text == 'Пятница':
            url = 'https://www.sptkaluga.ru/patn'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            dirty_string = str(soup.find('div', class_="main_content"))
            middle_list = re.split("<|>", dirty_string)
            predfinish_list = []
            for i in middle_list:
                f = i[:2]
                if f == '1)' or f == '2)' or f == '3)' or f == '4)':
                    predfinish_list.append(i)

            finish_list = []
            for i in predfinish_list[1:7]:
                f = i[:2]
                if f == '1)':
                    k = predfinish_list.index(i)
                    l = k + 1
                    h = k + 2
                    finish_list.append(i)
                    for s in predfinish_list[l:h]:
                        r = s[:2]
                        if r == '2)':
                            two = predfinish_list.index(s)
                            two1 = two + 1
                            two2 = two + 2
                            finish_list.append(s)
                            for thre in predfinish_list[two1:two2]:
                                d = thre[:2]
                                if d == '3)':
                                    three = predfinish_list.index(thre)
                                    three1 = three + 1
                                    three2 = three + 2
                                    finish_list.append(thre)
                                    for four in predfinish_list[three1:three2]:
                                        j = four[:2]
                                        if j == '4)':
                                            fourr = predfinish_list.index(four)
                                            fourr1 = fourr + 1
                                            fourr2 = fourr + 2
                                            finish_list.append(four)

            finishListReal = []
            compareNum = int(finish_list[0][0])
            for elem in finish_list:
                currNum = int(elem[0])
                if currNum < compareNum:
                    break;
                finishListReal.append(elem)
                compareNum = currNum

            finish_string = "\n".join(finishListReal)

            bot.send_message(chat_id, f'Расписание на пятницу: \n{finish_string}')



        elif message.text == 'Суббота':
            url = 'https://www.sptkaluga.ru/syb'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            dirty_string = str(soup.find('div', class_="main_content"))
            middle_list = re.split("<|>", dirty_string)
            predfinish_list = []
            for i in middle_list:
                f = i[:2]
                if f == '1)' or f == '2)' or f == '3)' or f == '4)':
                    predfinish_list.append(i)

            finish_list = []
            for i in predfinish_list[1:7]:
                f = i[:2]
                if f == '1)':
                    k = predfinish_list.index(i)
                    l = k + 1
                    h = k + 2
                    finish_list.append(i)
                    for s in predfinish_list[l:h]:
                        r = s[:2]
                        if r == '2)':
                            two = predfinish_list.index(s)
                            two1 = two + 1
                            two2 = two + 2
                            finish_list.append(s)
                            for thre in predfinish_list[two1:two2]:
                                d = thre[:2]
                                if d == '3)':
                                    three = predfinish_list.index(thre)
                                    three1 = three + 1
                                    three2 = three + 2
                                    finish_list.append(thre)
                                    for four in predfinish_list[three1:three2]:
                                        j = four[:2]
                                        if j == '4)':
                                            fourr = predfinish_list.index(four)
                                            fourr1 = fourr + 1
                                            fourr2 = fourr + 2
                                            finish_list.append(four)

            finishListReal = []
            compareNum = int(finish_list[0][0])
            for elem in finish_list:
                currNum = int(elem[0])
                if currNum < compareNum:
                    break;
                finishListReal.append(elem)
                compareNum = currNum

            finish_string = "\n".join(finishListReal)

            bot.send_message(chat_id, f'Расписание на вторник: \n{finish_string}')



        else:
            bot.send_message(chat_id, f'Сайт крякнулся')

bot.polling(none_stop=True)
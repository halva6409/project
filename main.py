import index
import config
import asyncio
import sql_db
import time
import sqlite3
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(config.TOKEN)

con = sqlite3.connect(config.database)
cur = con.cursor()


user_status = 0
#1 = админ
#0 = не админ
kol_vo = ''

day = ''

one = 'Нет урока'
two = 'Нет урока'
three = 'Нет урока'
four = 'Нет урока'
five = 'Нет урока'
six =  'Нет урока'
seven =  'Нет урока'
eight =  'Нет урока'


complite_admin = 0
#tommorow_shed = []


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)



#АДМИН
@bot.message_handler(commands=['admin'])
async def admin_1(message):
    global user_status, complite_admin
    complite_admin = 1
    user_status = 1
    await bot.send_message(message.chat.id, 'Введите пароль для входа от имени администратора:')

    
@bot.message_handler(func=lambda message: complite_admin == 1)
async def admin_2_5(message):
    global complite_admin
    password = '1'
    if message.text == password and user_status == 1:
        await bot.send_message(message.chat.id, 'На какой день недели хотите записать расписание?')
        complite_admin = 2

@bot.message_handler(func=lambda message: complite_admin == 2)
async def admin_2(message):
    global day,complite_admin
    message.text.lower()
    if message.text == 'пн' or 'вт' or 'ср' or 'чт' or 'пт':
        day = message.text
        await bot.send_message(message.chat.id, 'Хорошо')
        await bot.send_message(message.chat.id, 'Сколько будет уроков?')
        complite_admin = 3



#ПЕРВЫЙ УРОК
@bot.message_handler(func=lambda message: complite_admin == 3)
async def admin_3(message):
    global complite_admin,kol_vo
    kol_vo = message.text
    if kol_vo >= '1':
        await bot.send_message(message.chat.id, 'Напиши первый урок:')
        complite_admin = 4
        time.sleep(1)
    
#ВТОРОЙ УРОК
@bot.message_handler(func=lambda message: complite_admin == 4)
async def admin_4(message):
    global complite_admin,kol_vo,one
    if kol_vo <= '1':
        one = message.text
        if day == 'пн':
            #global 
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', ('ээээээээ',1))
            #cur.execute('''UPDATE nine_monday SET lesson = ? WHERE number = ?''' , (one,1))
        await bot.send_message(message.chat.id, one)
    if kol_vo >= '2':
        await bot.send_message(message.chat.id, 'Напиши второй урок:')
        complite_admin = 5
        one = message.text
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', ('ээээээээ',1))
        #elif day == 'вт':
            #cur.execute
#ТРЕТИЙ УРОК
@bot.message_handler(func=lambda message: complite_admin == 5)
async def admin_5(message):
    global complite_admin,kol_vo,two
    if kol_vo <= '2':
        two = message.text
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', ('эээ',1))
        await bot.send_message(message.chat.id, ( '№ 1 -- ' + one + '                                                                                                      ' 
        +  '№ 2 -- ' + two))
        await bot.send_message(message.chat.id, 'Спасибо за расписание')
    if kol_vo >= '3':
        await bot.send_message(message.chat.id, 'Напиши третий урок:')
        complite_admin = 6
        two = message.text
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (two,2))
        time.sleep(1)


#ЧЕТВЕРТЫЙ УРОК
@bot.message_handler(func=lambda message: complite_admin == 6)
async def admin_6(message):
    global complite_admin,kol_vo,three
    if kol_vo <= '3':
        three = message.text
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (three,3))
        await bot.send_message(message.chat.id, ( '№ 1 -- ' + one + '                                                                                                      ' 
        +  '№ 2 -- ' + two + '                                                                                                      '
        + '№ 3 -- ' + three))
        await bot.send_message(message.chat.id, 'Спасибо за расписание')
    if kol_vo >= '4':
        await bot.send_message(message.chat.id, 'Напиши четветый урок:')
        complite_admin = 7
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (three,3))
        three = message.text
        time.sleep(1)

#ПЯТЫЙ УРОК
@bot.message_handler(func=lambda message: complite_admin == 7)
async def admin_7(message):
    global complite_admin,kol_vo,four
    if kol_vo == '4':
        four = message.text
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (four,4))
        await bot.send_message(message.chat.id, ( '№ 1 -- ' + one + '                                                                                                      ' 
        +  '№ 2 -- ' + two + '                                                                                                      '
        + '№ 3 -- ' + three + '                                                                                                      '
        + '№ 4 -- ' + four))
        await bot.send_message(message.chat.id, 'Спасибо за расписание')
    if kol_vo >= '5':
        await bot.send_message(message.chat.id, 'Напиши пятый урок:')
        complite_admin = 8
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (four,4))
        four = message.text
        time.sleep(1)

#ШЕСТОЙ УРОК
@bot.message_handler(func=lambda message: complite_admin == 8)
async def admin_8(message):
    global complite_admin,kol_vo,five
    if kol_vo == '5':
        five = message.text
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (five,5))
        await bot.send_message(message.chat.id, ( '№ 1 -- ' + one + '                                                                                                      ' 
        +  '№ 2 -- ' + two + '                                                                                                      '
        + '№ 3 -- ' + three + '                                                                                                      '
        + '№ 4 -- ' + four + '                                                                                                      '
        + '№ 5 -- ' +  five))
        await bot.send_message(message.chat.id, 'Спасибо за расписание')
    if kol_vo >= '6':
        await bot.send_message(message.chat.id, 'Напиши шестой урок:')
        complite_admin = 9
        five = message.text
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (five,5))
        time.sleep(1)

#СЕДЬМОЙ УРОК
@bot.message_handler(func=lambda message: complite_admin == 9)
async def admin_9(message):
    global complite_admin,kol_vo,six
    if kol_vo == '6':
        six = message.text
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (six,6))
        await bot.send_message(message.chat.id, ( '№ 1 -- ' + one + '                                                                                                      ' 
        +  '№ 2 -- ' + two + '                                                                                                      '
        + '№ 3 -- ' + three + '                                                                                                      '
        + '№ 4 -- ' + four + '                                                                                                      '
        + '№ 5 -- ' +  five + '                                                                                                      '
        + '№ 6 -- ' + six))
        await bot.send_message(message.chat.id, 'Спасибо за расписание')
    if kol_vo >= '7':
        await bot.send_message(message.chat.id, 'Напиши седьмой урок:')
        complite_admin = 10
        six = message.text
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (six,6))
        time.sleep(1)

#ВОСЬМОЙ УРОК
@bot.message_handler(func=lambda message: complite_admin == 10)
async def admin_10(message):
    global complite_admin,kol_vo,seven
    if kol_vo == '7':
        seven = message.text
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (seven,7))
        await bot.send_message(message.chat.id, ( '№ 1 -- ' + one + '                                                                                                      ' 
        +  '№ 2 -- ' + two + '                                                                                                      '
        + '№ 3 -- ' + three + '                                                                                                      '
        + '№ 4 -- ' + four + '                                                                                                      '
        + '№ 5 -- ' +  five + '                                                                                                      '
        + '№ 6 -- ' + six + '                                                                                                      '
        + '№ 7 -- ' + seven))
        await bot.send_message(message.chat.id, 'Спасибо за расписание')
    if kol_vo == '8':
        await bot.send_message(message.chat.id, 'Напиши восьмой урок:')
        complite_admin = 11
        if day == 'пн':
            cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (seven,7))
        seven = message.text

@bot.message_handler(func=lambda message: complite_admin == 11)
async def admin_11(message):
    global eight,complite_admin
    eight = message.text
    if day == 'пн':
        cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (eight,8))
    await bot.send_message(message.chat.id, ( '№ 1 -- ' + one + '                                                                                                      ' 
    +  '№ 2 -- ' + two + '                                                                                                      '
    + '№ 3 -- ' + three + '                                                                                                      '
    + '№ 4 -- ' + four + '                                                                                                      '
    + '№ 5 -- ' +  five + '                                                                                                      '
    + '№ 6 -- ' + six + '                                                                                                      '
    + '№ 7 -- ' + seven + '                                                                                                      '
    + '№ 8 -- ' + eight))
    await bot.send_message(message.chat.id, 'Спасибо за расписание')
    complite_admin = 0
    if day == 'пн':
        cur.execute('UPDATE nine_monday SET lesson = ? WHERE number = ?', (eight,8))
    
    
#КОНЕЦ ADMIN







#ВЫХОД ИЗ АДМИНА 
@bot.message_handler(commands=['exit_admin'])
async def exit_admin(message):
    if user_status == 1:
        user_status = 0
        await bot.send_message(message.chat.id , "Вы вышли из аккаунта администратора")
    else:
        await bot.send_message(message.chat.id, 'Вы не входили в доступ администратора')

@bot.message_handler(commands=['test'])
async def test_admin(message):
    #await bot.send_message(message.chat.id,  one)
    await bot.send_message(message.chat.id,  two)
    """await bot.send_message(message.chat.id,  three)
    await bot.send_message(message.chat.id,  four)
    await bot.send_message(message.chat.id,  five)
    await bot.send_message(message.chat.id,  six)
    await bot.send_message(message.chat.id, seven)
    await bot.send_message(message.chat.id, eight)"""


#GPT
@bot.message_handler(func=lambda message: True)
async def gpt_answer(message):
    answer_gpt = index.gpt(message.text)
    await bot.send_message(message.chat.id, answer_gpt)
    

#ERROR
@bot.message_handler(func=lambda message: True)
async def send_message(message):
    message_error = 'error'
    await bot.reply_to(message, message_error)

if one == 'Классный час':
    kab_1 = 208
elif two == 'Классный час':
    kab_2 = 208    
elif three == 'Классный час':
    kab_3 = 208
elif four == 'Классный час':
    kab_4 = 208
elif five == 'Классный час':
    kab_5 = 208
elif six == 'Классный час':
    kab_6 = 208
elif seven == 'Классный час':
    kab_7 = 208
elif eight == 'Классный час':
    kab_8 = 208



asyncio.run(bot.polling())






















"""
import index

t = index.gpt('привет')

bot.send(id, t)"""
from datetime import time, date, datetime, timezone, timedelta
import requests
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from random import randint

is_game = {}
one={}
two={}
three={}
four={}
five={}
six={}
seven={}
eight={}
nine={}
fild = {}
################Base functions##################

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Это учебный бот\nОсновные команды:\n/hi (/start) - выводит имя профиля и приветствие\n/xo - игра в крестики-нолики\n/time - выводит время бота\n/sum - выводит сумму двух числе. Формат команды: </sum a b>\n/set - задать время оповещения. Формат команды: </set HH:MM:SS>\n/unset - сбросить время оповещения\n/msg - показать оповещение\n/help - текущая справка')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the alarm message."""
    msg, pic = message()
    await update.message.reply_photo(pic)
    await update.message.reply_text(msg)


################Everyday notification##################

async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Add a job to the queue."""
    chat_id = update.effective_message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        delta = datetime.now().time().hour - update.effective_message.date.time().hour
        if datetime.now().time().hour - update.effective_message.date.time().hour < 0:
            delta = 24 + datetime.now().time().hour - update.effective_message.date.time().hour
        if time.fromisoformat(context.args[0]).hour < 3:
            delta = -21
        due = time.fromisoformat(context.args[0]).replace(hour=time.fromisoformat(context.args[0]).hour - delta)
        job_removed = remove_job_if_exists(str(chat_id), context)
        context.job_queue.run_daily(alarm, due, chat_id=chat_id, name=str(chat_id))

        text = "Timer successfully set!"
        if job_removed:
            text += " Old one was removed."
        await update.effective_message.reply_text(text)

    except (IndexError, ValueError):
        await update.effective_message.reply_text("Usage: /set HH:MM:SS")


def remove_job_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True

async def unset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove the job if the user changed their mind."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = "Timer successfully cancelled!" if job_removed else "You have no active timer."
    await update.message.reply_text(text)

def get_info_about_city(api_url_base_value, city_name, api_token,requests_headers=None):
    response = requests.get(api_url_base_value + city_name + "&appid=" + api_token + "&lang=ru")
    print(response.status_code)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_wether(city = "Moscow"):
    api_token = 'TOKEN'
    api_url_base = 'https://api.openweathermap.org/data/2.5/weather?q='
    wether_json = get_info_about_city(api_url_base, city, api_token)
    iconcode = wether_json["weather"][0]["icon"]
    try:
        temperture = float(wether_json["main"]["temp"]) - 273
    except:
        temperture = None
    iconurl = "http://openweathermap.org/img/w/" + iconcode + ".png"
    description = wether_json["weather"][0]["description"]
    return (temperture, description, iconurl)

def message():
    newyear = date.fromisoformat(str(int(datetime.now().year) + 1) +"-01-01")
    delta = newyear-datetime.now().date()
    W = int(datetime.now().day)+int(datetime.now().month)+(int(datetime.now().year)-2015)%19
    t, d, p = get_wether()
    return (f"🌦Сейчас в Москве: {int(t)}, {d}\n🎅Дней до нового года: {delta.days}\n🌖{W%30}-й лунный день", p)

async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the alarm message."""
    job = context.job
    msg, pic = message()
    await context.bot.sendPhoto(chat_id=job.chat_id, photo=pic, caption=msg)


async def xo(update: Update, context: ContextTypes.DEFAULT_TYPE, new_choise = False):
    if not new_choise:
        fild[update.effective_message.chat_id] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        reply_keyboard = [
            [
                InlineKeyboardButton("_", callback_data="1"),
                InlineKeyboardButton("_", callback_data="2"),
                InlineKeyboardButton("_", callback_data="3"),
            ],
            [
                InlineKeyboardButton("_", callback_data="4"),
                InlineKeyboardButton("_", callback_data="5"),
                InlineKeyboardButton("_", callback_data="6"),
            ],
            [
                InlineKeyboardButton("_", callback_data="7"),
                InlineKeyboardButton("_", callback_data="8"),
                InlineKeyboardButton("_", callback_data="9"),
            ],
        ]
        is_game[update.effective_message.chat_id] = True
        msg = f'"Крестики-нолики"\nТы играешь крестиками\nТвой ход:'
        markup = InlineKeyboardMarkup(reply_keyboard)
        await update.message.reply_text(msg, reply_markup=markup)
    else:
        print(two.get(update.effective_message.chat_id, " "))
        if one.get(update.effective_message.chat_id, " ") == " " and new_choise == "1":
            one[update.effective_message.chat_id] = "❌"
            fild[update.effective_message.chat_id][int(new_choise)-1] = 1
        elif two.get(update.effective_message.chat_id, " ") == " " and new_choise == "2":
            two[update.effective_message.chat_id] = "❌"
            fild[update.effective_message.chat_id][int(new_choise)-1] = 1
            print(True)
        elif three.get(update.effective_message.chat_id, " ") == " " and new_choise == "3":
            three[update.effective_message.chat_id] = "❌"
            fild[update.effective_message.chat_id][int(new_choise)-1] = 1
            print(True)
        elif four.get(update.effective_message.chat_id, " ") == " " and new_choise == "4":
            four[update.effective_message.chat_id] = "❌"
            fild[update.effective_message.chat_id][int(new_choise)-1] = 1
        elif five.get(update.effective_message.chat_id, " ") == " " and new_choise == "5":
            five[update.effective_message.chat_id] = "❌"
            fild[update.effective_message.chat_id][int(new_choise)-1] = 1
        elif six.get(update.effective_message.chat_id, " ") == " " and new_choise == "6":
            six[update.effective_message.chat_id] = "❌"
            fild[update.effective_message.chat_id][int(new_choise)-1] = 1
        elif seven.get(update.effective_message.chat_id, " ") == " " and new_choise == "7":
            seven[update.effective_message.chat_id] = "❌"
            fild[update.effective_message.chat_id][int(new_choise)-1] = 1
        elif eight.get(update.effective_message.chat_id, " ") == " " and new_choise == "8":
            eight[update.effective_message.chat_id] = "❌"
            fild[update.effective_message.chat_id][int(new_choise)-1] = 1
        elif nine.get(update.effective_message.chat_id, " ") == " " and new_choise == "9":
            nine[update.effective_message.chat_id] = "❌"
            fild[update.effective_message.chat_id][int(new_choise)-1] = 1
        else:
            msg = "Неправильная клетка,\nпопробуйте еще раз"
            reply_keyboard = [
                [
                    InlineKeyboardButton(one.get(update.effective_message.chat_id, " "), callback_data="1"),
                    InlineKeyboardButton(two.get(update.effective_message.chat_id, " "), callback_data="2"),
                    InlineKeyboardButton(three.get(update.effective_message.chat_id, " "), callback_data="3"),
                ],
                [
                    InlineKeyboardButton(four.get(update.effective_message.chat_id, " "), callback_data="4"),
                    InlineKeyboardButton(five.get(update.effective_message.chat_id, " "), callback_data="5"),
                    InlineKeyboardButton(six.get(update.effective_message.chat_id, " "), callback_data="6"),
                ],
                [
                    InlineKeyboardButton(seven.get(update.effective_message.chat_id, " "), callback_data="7"),
                    InlineKeyboardButton(eight.get(update.effective_message.chat_id, " "), callback_data="8"),
                    InlineKeyboardButton(nine.get(update.effective_message.chat_id, " "), callback_data="9"),
                ],
            ]
            markup = InlineKeyboardMarkup(reply_keyboard)
            query = update.callback_query
            await query.edit_message_text(msg, reply_markup=markup)
            return "false"
        choise = ai(fild[update.effective_message.chat_id])
        if choise == 0:
            one[update.effective_message.chat_id] = "⭕️"
            fild[update.effective_message.chat_id][int(choise)] = 5
        elif choise == 1:
            two[update.effective_message.chat_id] = "⭕️"
            fild[update.effective_message.chat_id][int(choise)] = 5
        elif choise == 2:
            three[update.effective_message.chat_id] = "⭕️"
            fild[update.effective_message.chat_id][int(choise)] = 5
        elif choise == 3:
            four[update.effective_message.chat_id] = "⭕️"
            fild[update.effective_message.chat_id][int(choise)] = 5
        elif choise == 4:
            five[update.effective_message.chat_id] = "⭕️"
            fild[update.effective_message.chat_id][int(choise)] = 5
        elif choise == 5:
            six[update.effective_message.chat_id] = "⭕️"
            fild[update.effective_message.chat_id][int(choise)] = 5
        elif choise == 6:
            seven[update.effective_message.chat_id] = "⭕️"
            fild[update.effective_message.chat_id][int(choise)] = 5
        elif choise == 7:
            eight[update.effective_message.chat_id] = "⭕️"
            fild[update.effective_message.chat_id][int(choise)] = 5
        elif choise == 8:
            nine[update.effective_message.chat_id] = "⭕️"
            fild[update.effective_message.chat_id][int(choise)] = 5
        print("test",fild[update.effective_message.chat_id])
        if (fild[update.effective_message.chat_id][0]+fild[update.effective_message.chat_id][1]+fild[update.effective_message.chat_id][2] == 3) or (fild[update.effective_message.chat_id][3]+fild[update.effective_message.chat_id][4]+fild[update.effective_message.chat_id][5] == 3) or (fild[update.effective_message.chat_id][6]+fild[update.effective_message.chat_id][7]+fild[update.effective_message.chat_id][8] == 3) or (fild[update.effective_message.chat_id][0]+fild[update.effective_message.chat_id][3]+fild[update.effective_message.chat_id][6] == 3) or (fild[update.effective_message.chat_id][1]+fild[update.effective_message.chat_id][4]+fild[update.effective_message.chat_id][7] == 3) or (fild[update.effective_message.chat_id][2]+fild[update.effective_message.chat_id][5]+fild[update.effective_message.chat_id][8] == 3) or (fild[update.effective_message.chat_id][0]+fild[update.effective_message.chat_id][4]+fild[update.effective_message.chat_id][8] == 3) or (fild[update.effective_message.chat_id][6]+fild[update.effective_message.chat_id][4]+fild[update.effective_message.chat_id][2] == 3):
            msg = "Вы победили!"
            clear(update)
            query = update.callback_query
            await query.edit_message_text(msg)
            return print("win")
        elif (fild[update.effective_message.chat_id][0]+fild[update.effective_message.chat_id][1]+fild[update.effective_message.chat_id][2] == 15) or (fild[update.effective_message.chat_id][3]+fild[update.effective_message.chat_id][4]+fild[update.effective_message.chat_id][5] == 15) or (fild[update.effective_message.chat_id][6]+fild[update.effective_message.chat_id][7]+fild[update.effective_message.chat_id][8] == 15) or (fild[update.effective_message.chat_id][0]+fild[update.effective_message.chat_id][3]+fild[update.effective_message.chat_id][6] == 15) or (fild[update.effective_message.chat_id][1]+fild[update.effective_message.chat_id][4]+fild[update.effective_message.chat_id][7] == 15) or (fild[update.effective_message.chat_id][2]+fild[update.effective_message.chat_id][5]+fild[update.effective_message.chat_id][8] == 15) or (fild[update.effective_message.chat_id][0]+fild[update.effective_message.chat_id][4]+fild[update.effective_message.chat_id][8] == 15) or (fild[update.effective_message.chat_id][6]+fild[update.effective_message.chat_id][4]+fild[update.effective_message.chat_id][2] == 15):
            msg = "Вы проиграли!"
            clear(update)
            query = update.callback_query
            await query.edit_message_text(msg)
            return print("lose")
        if 0 not in fild[update.effective_message.chat_id]:
            msg = "Ничья!"
            query = update.callback_query
            await query.edit_message_text(msg)
            return print("pat")


        reply_keyboard = [
            [
                InlineKeyboardButton(one.get(update.effective_message.chat_id, " "), callback_data="1"),
                InlineKeyboardButton(two.get(update.effective_message.chat_id, " "), callback_data="2"),
                InlineKeyboardButton(three.get(update.effective_message.chat_id, " "), callback_data="3"),
            ],
            [
                InlineKeyboardButton(four.get(update.effective_message.chat_id, " "), callback_data="4"),
                InlineKeyboardButton(five.get(update.effective_message.chat_id, " "), callback_data="5"),
                InlineKeyboardButton(six.get(update.effective_message.chat_id, " "), callback_data="6"),
            ],
            [
                InlineKeyboardButton(seven.get(update.effective_message.chat_id, " "), callback_data="7"),
                InlineKeyboardButton(eight.get(update.effective_message.chat_id, " "), callback_data="8"),
                InlineKeyboardButton(nine.get(update.effective_message.chat_id, " "), callback_data="9"),
            ],
        ]
        msg = "Ваш ход"
        markup = InlineKeyboardMarkup(reply_keyboard)
        query = update.callback_query
        await query.edit_message_text(msg, reply_markup=markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    await query.answer()

    await xo(update, context, query.data)


def ai(fild):
    print(fild)
    randchoise = []
    choise = 0
    if fild[0]+fild[1]+fild[2] == 10:
        print("if1", fild[:3], fild[:3].index(0))
        return fild[:3].index(0)
    if fild[3]+fild[4]+fild[5] == 10:
        print("if2", fild[3:6], fild[3:6].index(0))
        return fild[3:6].index(0)+3
    if fild[6]+fild[7]+fild[8] == 10:
        print("if3", fild[6:], fild[6:].index(0))
        return fild[6:].index(0)+6
    if fild[0]+fild[3]+fild[6] == 10:
        if fild[0] == 0:
            return 0
        elif fild[3] == 0:
            return 3
        else:
            return 6
    if fild[1]+fild[4]+fild[7] == 10:
        if fild[1] == 0:
            return 1
        elif fild[4] == 0:
            return 4
        else:
            return 7
    if fild[2]+fild[5]+fild[8] == 10:
        if fild[2] == 0:
            return 2
        elif fild[5] == 0:
            return 5
        else:
            return 8
    if fild[0]+fild[4]+fild[8] == 10:
        if fild[0] == 0:
            return 0
        elif fild[4] == 0:
            return 4
        else:
            return 8
    if fild[2]+fild[4]+fild[6] == 10:
        if fild[2] == 0:
            return 2
        elif fild[4] == 0:
            return 4
        else:
            return 6
    if fild[4] == 0:
        return 4


    if fild[0] == 0 and fild[1] == 0 and fild[2] == 0:
        randchoise.append(0)
        randchoise.append(1)
        randchoise.append(2)
    if fild[3] == 0 and fild[4] == 0 and fild[5] == 0:
        randchoise.append(3)
        randchoise.append(4)
        randchoise.append(5)
    if fild[6] == 0 and fild[7] == 0 and fild[8] == 0:
        randchoise.append(6)
        randchoise.append(7)
        randchoise.append(8)
    if fild[0] == 0 and fild[3] == 0 and fild[6] == 0:
        randchoise.append(0)
        randchoise.append(3)
        randchoise.append(6)
    if fild[1] == 0 and fild[4] == 0 and fild[7] == 0:
        randchoise.append(1)
        randchoise.append(4)
        randchoise.append(7)
    if fild[2] == 0 and fild[5] == 0 and fild[8] == 0:
        randchoise.append(2)
        randchoise.append(5)
        randchoise.append(8)
    if fild[0] == 0 and fild[4] == 0 and fild[8] == 0:
        randchoise.append(0)
        randchoise.append(4)
        randchoise.append(8)
    if fild[2] == 0 and fild[4] == 0 and fild[6] == 0:
        randchoise.append(2)
        randchoise.append(4)
        randchoise.append(6)
    if randchoise:
        choise = randchoise[randint(0, len(randchoise) - 1)]
        randchoise = []
    else:
        print("while")
        while True:
            choise = randint(0, 8)
            if fild[choise] == 0:
                print(choise, fild[choise])
                break
            elif 0 not in fild:
                break
    print(choise)
    return choise

def clear(update):
    one[update.effective_message.chat_id] = " "
    two[update.effective_message.chat_id] = " "
    three[update.effective_message.chat_id] = " "
    four[update.effective_message.chat_id] = " "
    five[update.effective_message.chat_id] = " "
    six[update.effective_message.chat_id] = " "
    seven[update.effective_message.chat_id] = " "
    eight[update.effective_message.chat_id] = " "
    nine[update.effective_message.chat_id] = " "
    fild[update.effective_message.chat_id] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

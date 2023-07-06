from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    MessageHandler,
    Filters,
    CommandHandler,
)
# import all we need
from cred import TOKEN #importing token 
from menu import main_menu_keyboard, game_menu_keyboard #importing keyboards
from key_buttons import g_buttons #import buttons with games
from key_buttons import m_buttons #import buttons for main menu 
from key_buttons import b_button #separated back button
from key_buttons import m_buttons 
from key_buttons import l_buttons
from menu import onliigri
from menu import dialogs
from learn import abc_level,elementary_level,preint_level,inter_level,upper_int_level,advanced_level
import random #it's options for randomizing choise

balancik = 100


def record(update: Update, context: CallbackContext):
    text = update.message.text
    if text[:6].lower() == 'привет':
        print(text)
        update.message.reply_text(
            f'Привет,{update.effective_user.username}'
        )
    if text[:14].lower() == 'как тебя зовут':
        print(text)
        update.message.reply_text(
            f'Меня зовут Universalny,я-бот'
        )
    if text[:16].lower() == 'сколько тебе лет':
        print(text)
        update.message.reply_text(
            f'мне меньше 1 месяца.'
        )
    if text[:19].lower() == 'кто твой создатель':
        print(text)
        update.message.reply_text(
            f'Моего создателя зовут Нурдан. Подробнее о нем в кнопке О нас.'
        )
    if text[:34].lower() == 'пришли мне инстаграм вашего автора':
        print(text)
        update.message.reply_text(
            f'Конечно! https://www.instagram.com/nnyshanovv/ - это его инстаграм.'
        )


def learn(update: Update, context: CallbackContext):
    update.message.reply_text(f"Choose level:",
        reply_markup=dialogs()
    )
LEARN = m_buttons[5]


def levelabc(update: Update, context: CallbackContext):
    update.message.reply_text(f"""Here are your conversations and words for your level:
                              {abc_level}""""",
        reply_markup=dialogs()
    )
LEVELABC = l_buttons[0]


def levelele(update: Update, context: CallbackContext):
    update.message.reply_text(f"""Here are your conversations and words for your level:
                              {elementary_level}""""",
        reply_markup=dialogs()
    )
LEVELELE = l_buttons[1]


def levelpre(update: Update, context: CallbackContext):
    update.message.reply_text(f"""Here are your conversations and words for your level:
                              {preint_level}""""",
        reply_markup=dialogs()
    )
LEVELPRE = l_buttons[2]


def levelint(update: Update, context: CallbackContext):
    update.message.reply_text(f"""Here are your conversations and words for your level:
                              {inter_level}""""",
        reply_markup=dialogs()
    )
LEVELINT = l_buttons[3]


def leveluppa(update: Update, context: CallbackContext):
    update.message.reply_text(f"""Here are your conversations and words for your level:
                              {upper_int_level}""""",
        reply_markup=dialogs()
    )
LEVELUPPA = l_buttons[4]


def leveladva(update: Update, context: CallbackContext):
    update.message.reply_text(f"""Here are your conversations and words for your level:
                              {advanced_level}""""",
        reply_markup=dialogs()
    )
LEVELADVA = l_buttons[5]

def talk(update: Update, context: CallbackContext):
    update.message.reply_text(f"""
Вы можете поговорить со мной. Я могу ответить на:
                              
привет
как тебя зовут
сколько тебе лет
кто твой создатель
пришлите мне инстаграм вашего автора

Пишите в чат(Пишите так же как я сказал)
""""",reply_markup=main_menu_keyboard())
TALK = m_buttons[4]

def new_back(update: Update, context: CallbackContext):
    text = f"""
{update.effective_user.username},Вы были отправлены в список игр!
"""
    gif_file = open('bye.gif', 'rb')
    context.bot.send_animation(
        chat_id=update.effective_chat.id,
        animation=gif_file,
    )
    update.message.reply_text(f'{text}', reply_markup=game_menu_keyboard())
    gif_file.close()

NEWBACK = b_button[0]

def bout(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""
Добро пожаловать,{update.effective_user.username}!
Это достаточно универсальный бот, который имеет
3 функции: Играть, разговаривать с вами, обучать английскому языку.
Мы добавим больше функций в ближайшее время.
""",
        reply_markup=main_menu_keyboard()
    )

ABOUT = m_buttons[2]

def start(update: Update, context: CallbackContext):
    text = f"""
Добро пожаловать, {update.effective_user.username}!
"""
    gif_file = open('haloo.gif', 'rb')
    context.bot.send_animation(
        chat_id=update.effective_chat.id,
        animation=gif_file,
    )
    update.message.reply_text(
f'{text}',reply_markup=main_menu_keyboard())
    gif_file.close()


def me(update: Update, context: CallbackContext):
    update.message.reply_text("""
Вы выбрали кнопку «О нас». Автора зовут Нурдан.
Ему 17 лет, он из Оша, но в настоящее время живет в Бишкеке. Его
день рождения 7 июня. Он родился в 2006 году. Родился в г.
город Бишкек, и я не знаю, в каком доме он родился. Это его первый
собственный проект. Его уровень английского находится на уровне Upper-Intermediate (я думаю).
Он учится в колледже «Ала-Тоо» и только что закончил первый
год колледжа. Удачи моему автору.
""", reply_markup=main_menu_keyboard())

MEE = m_buttons[3]

def back(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Хорошо! Вас отправили обратно!""",
        reply_markup=main_menu_keyboard()
    )

BACKAT = g_buttons[3]

def balance(update: Update, context: CallbackContext):
    global balancik
    if balancik == 0:
        balancik += 10
        update.message.reply_text(
            f"Ваш баланс был равен нулю. Вы получили 10 баллов.",
            reply_markup=main_menu_keyboard()
        )
    else:
        text = f"""
Ваш баланс составляет {balancik} баллов!"""
    gif_file = open('wallet.gif', 'rb')
    context.bot.send_animation(
        chat_id=update.effective_chat.id,
        animation=gif_file,
        caption=text
    )
    update.message.reply_text(
'Неплохо !',
        reply_markup=main_menu_keyboard()
    )
    gif_file.close()

BLANCE = m_buttons[0]

def games(update: Update, context: CallbackContext):
    text = f"""{update.effective_user.username}, Добро пожаловать в раздел Игры! Выберите игру!"""
    gif_file = open('welcome.gif', 'rb')
    context.bot.send_animation(
        chat_id=update.effective_chat.id,
        animation=gif_file,  
    )
    update.message.reply_text(f'{text}',reply_markup=game_menu_keyboard())
    gif_file.close()

GAME = m_buttons[1]

def penalty_game(update: Update, context: CallbackContext):
    text = f"""
{update.effective_user.username},Вы выбрали пенальти!
У вас есть 5 вариантов:
Left bottom corner, Right bottom corner, Middle, Left top 
corner, Right top corner. Выберите свой вариант:
Пишите полностью как написано выше(Left bottom corner, 
Right bottom corner, Middle, Left top corner,
 Right top corner.)"""
    gif_file = open('standard.gif', 'rb')
    context.bot.send_animation(
        chat_id=update.effective_chat.id,
        animation=gif_file,   
    )
    update.message.reply_text(f'{text}',reply_markup=onliigri())
    gif_file.close()
    

def handle_penalty_option(update: Update, context: CallbackContext):
    options = ["Left bottom corner", "Right bottom corner", "Middle", "Left top corner", "Right top corner"]
    generated_option = random.choice(options)
    user_option = update.message.text

    if user_option == generated_option:
        update.message.reply_text("Поздравляем! Вы угадали правильно и заработали +10 баллов!")
        global balancik
        balancik += 10
    else:
        balancik -= 10
        text = """Ой! Вы потеряли -10 очков!"""
        gif_file = open('oops.gif', 'rb')
        context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=gif_file,
            caption=text
        )
        gif_file.close()
    update.message.reply_text(f"Сгенерированный вариант: {generated_option}\nВаш баланс: {balancik}", reply_markup=onliigri())

def dice_game(update: Update, context: CallbackContext):
    text = f"""
{update.effective_user.username},Вы выбрали игру Кубик!
Бросив кости... Выберите число от 1 до 6."""
    gif_file = open('standard.gif', 'rb')
    context.bot.send_animation(
        chat_id=update.effective_chat.id,
        animation=gif_file,
    )
    update.message.reply_text(f'{text}',reply_markup=onliigri())
    gif_file.close()

def handle_dice_roll(update: Update, context: CallbackContext):
    generated_number = random.randint(1, 6)
    user_number = int(update.message.text)

    if user_number == generated_number:
        update.message.reply_text("Поздравляем! Вы угадали правильно и заработали +5 баллов!")
        global balancik
        balancik += 5
    else:
        balancik -= 5
        text = """Ой! Вы потеряли -5 очков!"""
        gif_file = open('oops.gif', 'rb')
        context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=gif_file,
            caption=text
        )
        gif_file.close()

    update.message.reply_text(f"Сгенерированный вариант: {generated_number}\nВаш баланс: {balancik}", reply_markup=onliigri())

def guess_number_game(update: Update, context: CallbackContext):
    text = f"""
{update.effective_user.username},Вы выбрали игру!
Бросив кости... Выберите число от 1 до 10."""
    gif_file = open('standard.gif', 'rb')
    context.bot.send_animation(
        chat_id=update.effective_chat.id,
        animation=gif_file,
    )
    update.message.reply_text(f'{text}',reply_markup=onliigri())
    gif_file.close()

def handle_guess_number(update: Update, context: CallbackContext):
    generated_number = random.randint(1, 10)
    user_number = int(update.message.text)

    if user_number == generated_number:
        update.message.reply_text("Поздравляем! Вы угадали правильно и заработали +20 баллов!")
        global balancik
        balancik += 20
    else:
        balancik -= 20
        text = """"Ой! Вы потеряли -20 очков!"""
        gif_file = open('oops.gif', 'rb')
        context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=gif_file,
            caption=text
        )
        gif_file.close()
    update.message.reply_text(f"Сгенерированный вариант: {generated_number}\nВаш баланс: {balancik}", reply_markup=onliigri())
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(NEWBACK), new_back))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(TALK), talk))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(LEARN), learn))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(LEVELABC), levelabc))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(LEVELELE), levelele))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(LEVELPRE), levelpre))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(LEVELINT), levelint))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(LEVELUPPA), leveluppa))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(LEVELADVA), leveladva))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(MEE), me))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(ABOUT), bout))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(BLANCE), balance))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(GAME), games))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(g_buttons[0]), penalty_game))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command & Filters.regex("^(Left bottom corner|Right bottom corner|Middle|Left top corner|Right top corner)$"), handle_penalty_option))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(g_buttons[1]), dice_game))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command & Filters.regex("^(1|2|3|4|5|6)$"), handle_dice_roll))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(g_buttons[2]), guess_number_game))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command & Filters.regex("^(1|2|3|4|5|6|7|8|9|10)$"), handle_guess_number))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(BACKAT), back))
updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    record
))
updater.start_polling()
updater.idle()
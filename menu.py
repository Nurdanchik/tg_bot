import telegram 
from key_buttons import m_buttons,g_buttons,b_button,l_buttons

def main_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(m_buttons[0])],
        [telegram.KeyboardButton(m_buttons[1])],
        [telegram.KeyboardButton(m_buttons[2])],
        [telegram.KeyboardButton(m_buttons[3])],
        [telegram.KeyboardButton(m_buttons[4])],
        [telegram.KeyboardButton(m_buttons[5])],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard,resize_keyboard=True,one_time_keyboard=False
    )           


def game_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(g_buttons[0])],
        [telegram.KeyboardButton(g_buttons[1])],
        [telegram.KeyboardButton(g_buttons[2])],
        [telegram.KeyboardButton(g_buttons[3])],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard,resize_keyboard=True,one_time_keyboard=False
    )


def dialogs():
    keyboard = ([
        [telegram.KeyboardButton(l_buttons[0])],
        [telegram.KeyboardButton(l_buttons[1])],
        [telegram.KeyboardButton(l_buttons[2])],
        [telegram.KeyboardButton(l_buttons[3])],
        [telegram.KeyboardButton(g_buttons[3])],
        [telegram.KeyboardButton(l_buttons[4])],
        [telegram.KeyboardButton(l_buttons[5])],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard,resize_keyboard=True,one_time_keyboard=False
    )


def onliigri():
    keyboard = ([
        [telegram.KeyboardButton(b_button[0])],])
    return telegram.ReplyKeyboardMarkup(
        keyboard,resize_keyboard=True,one_time_keyboard=False)

def talk_menu():
    keyboard = ([
        [telegram.KeyboardButton(g_buttons[3])],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard,resize_keyboard=True,one_time_keyboard=False
    )
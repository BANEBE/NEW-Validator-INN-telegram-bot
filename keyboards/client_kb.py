from aiogram import types

b1 = types.KeyboardButton('/start_validation')
b2 = types.KeyboardButton('/help')
b3 = types.KeyboardButton('/start')

kb_client = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.row(b1, b2, b3)


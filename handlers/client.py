from aiogram import types, Dispatcher
from settings import bot
from keyboards.client_kb import kb_client
from serveses.serveses import main_valid_logic
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup



class InnState(StatesGroup):
    waiting_for_inn_value = State()


async def command_start(message: types.Message):
    """
    This handler will be called when user sends `/start command
    """
    await bot.send_message(message.chat.id,
                           "Привет!\nЯ ValidatorInnBot!\n"
                           "Введите команду: /start_validation\n"
                           "Для начала проверки ИНН.",
                           reply_markup=kb_client)
    await message.delete()


async def command_help(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await bot.send_message(message.chat.id,
                           "Маски ввода:\nДля 10-значного ИНН: XXXXXXXXXX\n"
                           "Для 12-значного ИНН: XXXXXXXXXXXX\n"
                           "Для начала проверки ИНН: /start_validation\n",
                           reply_markup=kb_client)
    await message.delete()


async def validate_inn(message: types.Message):
    await message.answer("Введите 10-ти или 12-ти значный ИНН")
    await InnState.waiting_for_inn_value.set()


async def result_send(message: types.Message, state: FSMContext):
    result_text = await main_valid_logic(message.text)
    await message.answer(f"{result_text}\n Проверка завершена!")
    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(validate_inn, commands=['start_validation'])
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(result_send, state=InnState.waiting_for_inn_value)

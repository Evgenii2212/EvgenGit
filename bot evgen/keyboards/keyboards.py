from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='актуальные мероприятия')],
                                     [KeyboardButton(text='предыдущие эфиры')],
                                     [KeyboardButton(text='забрать подарки'),
                                      KeyboardButton(text='О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ivan zolo', callback_data='ivan zolo')],
    [InlineKeyboardButton(text='buster', callback_data='buster')],
    [InlineKeyboardButton(text='evelone', callback_data='evelone')]])


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)

from aiogram import types
keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='tasks'),
        ],
        [
            types.KeyboardButton(text='commands'),
            types.KeyboardButton(text='links')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='All commands'
)
tasks_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='check all')
        ],
        [
            types.KeyboardButton(text='➕Add a new task')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Actions...'
)


from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.for_navigate import tasks_keyboard
import asyncio
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.formatting import Bold, Underline, as_marked_section, as_section


tasks_router = Router()
TASK = []



@tasks_router.message(F.text == 'TASKS')
@tasks_router.message(Command('tasks'))
async def tasks(message: types.Message):
    await message.reply('Please choose your action',
                        reply_markup=tasks_keyboard)


@tasks_router.message(F.text == 'check all')
async def check_all(message: types.Message):
    await message.reply('All your tasks',
                        reply_markup=types.ReplyKeyboardRemove())
    for i in range(len(TASK)):
        await asyncio.sleep(0.4)
        text = as_marked_section(
            'Task',
            as_section(Underline(i+1), Bold(TASK[i])),
            marker='✅'
        )
        builder = InlineKeyboardBuilder()
        builder.add(
            types.InlineKeyboardButton(text='delete the task',
                                       callback_data=f'task_{i}')
        )
        await message.answer(text.as_html(), reply_markup=builder.as_markup())


@tasks_router.callback_query(F.data.split('_')[0] == 'task')
async def del_task(callback: types.CallbackQuery):
    task_id = callback.data.split('_')[1]
    task_to_del = TASK.pop(int(task_id))
    await callback.message.answer(f'Taks: {task_to_del}. Has been deleted successfully')
    await callback.answer('Its ok, task deleted successfully', show_alert=True)




class AddTask(StatesGroup):
    content = State()


@tasks_router.message(StateFilter(None), F.text == '➕Add a new task')
async def add_new_task(message: types.Message, state: FSMContext):
    await message.answer('Enter your task',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddTask.content)


@tasks_router.message(AddTask.content, F.text)
async def add_task_to_list(message: types.Message, state: FSMContext):
    await state.update_data(content=message.text)
    await message.answer('✅Task has been added', reply_markup=tasks_keyboard)
    data = await state.get_data()
    await message.answer(str(data))
    TASK.append(data['content'])
    await state.clear()
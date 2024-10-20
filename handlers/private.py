from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold, TextLink
from keyboards.for_navigate import keyboard
private_router = Router()
@private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.reply('you started work with our bot', reply_markup=keyboard)

@private_router.message(or_f(Command('School links'), F.text == 'School links'))
async def links(message: types.Message):
    text = as_marked_section(
        Bold('MYCDMC links'),
        TextLink('MYSDMC', url='https://myapps.classlink.com/home'),
        TextLink('Focus', url='https://focus.manateeschools.net/focus/Modules.php?modname=misc%2FPortal.php'),
        TextLink('schoology', url=r'https://manatee.schoology.com/home'),
        marker='✅'
    )
    await message.reply(text.as_html())
@private_router.message(or_f(Command('Game links'),F.text == 'Game links'))
async def game_links(message: types.Message):
    text2 = as_marked_section(
      Bold('Game links:'),
        TextLink('Roblox', url='https://www.roblox.com/Login'),
        TextLink('Activison Call of duty', url='https://www.activision.com/#'),
        TextLink('Minecraft', url='https://www.minecraft.net/en-us/msaprofile'),
        marker='🕹️'
    )
    await message.reply(text2.as_html())
@private_router.message(or_f(Command('Youtube links'), F.text == 'Youtube links'))
async def youtube(message: types.Message):
    text3 = as_marked_section(
        Bold('Youtube channels'),
        TextLink('Natural Albertovich', url='https://www.youtube.com/@natural_albertovich'),
        marker='▶️'


    )
    await message.reply(text3.as_html())


@private_router.message(Command('commands'))
async def commands(message: types.Message):
    await message.reply('''Not realized Commands:
      ✅School links - write in chat
      🕹️Game links - write in chat
      ▶️Youtube links - write in chat ''')
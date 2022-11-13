from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import aiohttp
from bs4 import BeautifulSoup as BS


URL = 'https://images.search.yahoo.com/search/images;_ylt=AwrJ.QpoJWljCPIyZvdXNyoA;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZANMT0NVSTA1M0NfMQRzZWMDcGl2cw--?p=%s&fr2=piv-web&fr=yfp-t'
SECRET_TOKEN = '5640616400:AAHqd6j7E0DJ_tMNiUYqgvz3ZiFFwn03Vx8'
bot = Bot(token=SECRET_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Image Bot! Tell me what picture you want to see\Use the Force")

@dp.message_handler()
async def send_image(message: types.Message):
    req = message.text
    async with aiohttp.ClientSession() as ses:
        async with ses.get(URL % req) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BS(html, 'lxml')
                images = soup.select('img[src]')
                try:
                    img_url = images[0]['src']
                    await bot.send_photo(message.chat.id, photo=img_url)
                except IndexError:
                    await message.reply('No images found')
                        

if __name__ == '__main__':
    executor.start_polling(dp)
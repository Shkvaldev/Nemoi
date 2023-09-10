import aiogram
import asyncio
from aiogram import types
#from magic_filter import F
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage

class TGBot:
    def __init__(self, core):
        self.core = core
        self.storage = MemoryStorage()
        try:
            self.bot = aiogram.Bot(self.core.config["TELEGRAM_API_TOKEN"])
            self.dp = aiogram.Dispatcher(storage = self.storage)
            self.rules_apply()
        except Exception as e:
            exit(f"[!] Can not start TGBot: {e}")
    
    def rules_apply(self):
        @self.dp.message(F.voice)
        async def user_input_handler(message: types.Message):
            file_name = message.voice.file_id # Get voice's id
            await self.bot.download(file=file_name, destination=f"{file_name}.ogg")
            answer = self.core.stt.recognize(f"{file_name}.ogg")
            if answer:
                await message.answer(f"{message.from_user.first_name} 🗣: {answer}")

    def run(self):
        try:
            asyncio.run(self.dp.start_polling(self.bot, skip_updates=True))
        except Exception as e:
            exit(f"[!] Can not start TGBot: {e}")
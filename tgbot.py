import time

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
            self.core.log.write(f"[!] Can not start TGBot: {e}")
            exit(f"[!] Can not start TGBot: {e}")
    
    def rules_apply(self):
        @self.dp.message(F.voice) # TODO: add F.audio support
        async def user_input_handler(message: types.Message):
            file_name = message.voice.file_id # Get voice's id
            await self.bot.download(file=file_name, destination=f"{file_name}.ogg")
            answer = self.core.stt.recognize(f"{file_name}.ogg")
            if self.core.config["TELEMETRY"]:
                print(f"{message.from_user.full_name} ({message.from_user.url}) said: {answer}")
                self.core.log.write(f"[{time.strftime('%H:%M:%S')}] {message.from_user.full_name} ({message.from_user.url}) said: {answer}\n")
            if answer:
                await message.reply(f"{message.from_user.first_name} 🗣: {answer}")
                return
            await message.reply(f"{message.from_user.first_name} произнёс нечто неразборчивое :(")

    def run(self):
        try:
            asyncio.run(self.dp.start_polling(self.bot, skip_updates=True))
        except Exception as e:
            self.core.log.write(f"[!] Can not start TGBot: {e}")
            exit(f"[!] Can not start TGBot: {e}")
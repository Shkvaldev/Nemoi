import os
import time
import json

# Project's imports
from checker import Checker
from stt import STT
from tgbot import TGBot

def parse_config(config_path):
    with open(config_path, "r") as config:
        config_data = json.loads(config.read())
        config.close()
        return config_data

class Core:
    def __init__(self):
        self.config = parse_config("config.json")
        # Init logging TODO: rewrite using asyncio
        self.log = open(f"logs/{time.strftime('%H_%M_%S_log.txt')}", "w")
        self.stt = STT(self.config)
        self.tgbot = TGBot(self)
        self.tgbot.run()
        self.log.write(f"[{time.strftime('%H_%M_%S_log.txt')}] Bot is off\n")
        self.log.close()

if __name__ == "__main__":
    Checker(parse_config("config.json"))
    Core()
    os.system("rm -rf __pycache__")
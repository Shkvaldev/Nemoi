# _Немой_
**Приложение для перевода голосовых в текст для Telegram**
> Приложение находится на начальном этапе разработки!

# Особенное спасибо разработчикам:
- **Aiogram: https://github.com/aiogram/aiogram**
- **VOSK: https://alphacephei.com/vosk/**

# Установка и запуск:
1. Установливаем язык программирования Python:
```shell
# Arch Linux
sudo pacman -Sy python python-pip ffmpeg
```
2. Клонируем репозиторий:
```shell
git clone (repo url here)
```
3. Устанавливаем окружение:
```shell
# Глобально
pip install -r requirements.txt --break-system-packages
# Виртуально
python -m venv nemoi_venv
mv Nemoi nemoi_venv
cd nemoi_venv
source bin/activate
pip install -r requirements.txt
```
4. Добавляем токен (регистрируем у BotFather) в config.json
5. Запускаем бота:
> Не забываем активировать виртуальное окружение перед запуском, если установили туда!
```shell
python main.py
```


## Платформы
- **Arch Linux**

## TODO
- **Добавить поддержку Windows**
- **Сделать простой лаунчер (run.sh)**
- **Сделать возможности запуска в качестве демона (службы)**
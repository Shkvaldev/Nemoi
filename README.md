# _Немой_
**Приложение для перевода голосовых в текст для Telegram**
> Приложение находится на начальном этапе разработки!

# Особенное спасибо разработчикам:
- **Aiogram: https://github.com/aiogram/aiogram**
- **whisper-cpp-python: https://github.com/carloscdias/whisper-cpp-python**

- _VOSK: https://alphacephei.com/vosk_ (использовался ранее, но всё равно спасибо)

# Установка и запуск:
1. Установливаем язык программирования Python:
```shell
# Arch Linux
sudo pacman -Sy python python-pip python-setuptools ffmpeg
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
4. Скачиваем модель _ggml-small.bin_:
```shell
wget --show-progress -O ggml-small.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin
```
5. Добавляем токен (регистрируем у BotFather) в config.json
6. Запускаем бота:
> Не забываем активировать виртуальное окружение перед запуском, если установили туда!
```shell
python main.py
```


## Платформа
> Поддержка остальных платформ не планируется в будущем
- **Arch Linux**

## TODO:
- **Скрипт для изменения конфигурационного файла**
- **Скрипт для загрузки моделей Whisper**
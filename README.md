# _Немой_
**Приложение для перевода голосовых в текст для Telegram**
> Приложение находится на начальном этапе разработки!

>Существует облегчённая версия, работающая при помощи VOSK: Nemoi STT Lite

# Особенное спасибо разработчикам:
- **Aiogram: https://github.com/aiogram/aiogram**
- **whisper-cpp-python: https://github.com/carloscdias/whisper-cpp-python**

> _VOSK: https://alphacephei.com/vosk_ (использовался ранее, но всё равно спасибо)

# Установка и запуск:
1. Установливаем системные зависимости:
```shell
# Arch Linux
sudo pacman -Sy python python-pip ffmpeg
```
2. Клонируем репозиторий:
```shell
git clone URL
```
3. Добавляем токен (регистрируем у BotFather) в /usr/share/nemoi-stt-lite/run/src/config.json
4. Запускаем бота:
```shell
sudo systemctl daemon-reload
sudo systemctl start nemoi-stt
```


## Платформа
> Поддержка остальных платформ не планируется в будущем
- **Arch Linux**

## TODO:
- **Скрипт для изменения конфигурационного файла**
- **Скрипт для загрузки моделей Whisper**
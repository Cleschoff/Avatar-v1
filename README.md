# Проверка синхронизации (тест)
# AI-Chat + Live Avatar

Интерактивное веб-приложение с искусственным интеллектом, включающее чат-бот с OpenAI GPT-4 и живого аватара через HeyGen Streaming API.

## 🚀 Технологии

### Backend
- **FastAPI** - современный веб-фреймворк для Python
- **Uvicorn** - ASGI сервер для запуска FastAPI
- **Pydantic** - валидация данных и настройки
- **OpenAI API** - интеграция с GPT-4 для генерации ответов
- **HeyGen API** - стриминг живого аватара
- **WebSocket** - реальное время для транскрипции
- **Pydub** - обработка аудио файлов

### Frontend
- **Vanilla JavaScript** - без фреймворков
- **WebSocket API** - для аудио стриминга
- **MediaRecorder API** - запись аудио
- **Web Audio API** - анализ аудио и VAD
- **LiveKit Client** - подключение к видеопотоку аватара
- **CSS3** - современные стили и анимации

### Инфраструктура
- **Python 3.11+** - основной язык
- **Virtual Environment** - изоляция зависимостей
- **CORS** - межсайтовые запросы
- **Static Files** - раздача фронтенда

## 📁 Структура проекта

```
Avatar/
├── app/                    # Backend приложение
│   ├── core/              # Основные настройки
│   │   └── config.py      # Конфигурация и переменные окружения
│   ├── routers/           # API маршруты
│   │   ├── avatar.py      # Управление аватаром
│   │   ├── chat.py        # Чат с OpenAI
│   │   └── transcribe.py  # Транскрипция аудио
│   └── main.py            # Главный файл приложения
├── public/                # Frontend файлы
│   ├── css/
│   │   └── style.css      # Стили приложения
│   ├── js/
│   │   ├── avatar.js      # Логика аватара
│   │   ├── chat.js        # Логика чата
│   │   └── transcribe.js  # Логика транскрипции
│   └── index.html         # Главная страница
├── requirements.txt        # Python зависимости
└── venv/                  # Виртуальное окружение
```

## 🔧 Установка и запуск

### Предварительные требования
- Python 3.11+
- OpenAI API ключ
- HeyGen API ключ

### Шаги установки
```bash
# 1. Клонирование репозитория
git clone <repository-url>
cd Avatar

# 2. Создание виртуального окружения
python -m venv venv

# 3. Активация окружения
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Установка зависимостей
pip install -r requirements.txt

# 5. Создание .env файла
echo "OPENAI_API_KEY=your_openai_key_here" > .env
echo "HEYGEN_API_KEY=your_heygen_key_here" >> .env

# 6. Запуск приложения
uvicorn app.main:app --reload
```

### Доступ к приложению
- **Основное приложение**: http://127.0.0.1:8000/
- **API документация**: http://127.0.0.1:8000/docs

## 📋 API Endpoints

### Chat API (`/api/chat`)
- **POST** `/api/chat` - отправка сообщения в чат и получение ответа от GPT-4

### Avatar Streaming API (`/api/streaming`)
- **POST** `/api/streaming/token` - получение токена для стриминга
- **POST** `/api/streaming/session` - создание новой сессии аватара
- **POST** `/api/streaming/start` - запуск стриминга аватара
- **POST** `/api/streaming/task` - отправка текста для озвучивания аватаром
- **POST** `/api/streaming/stop` - остановка стриминга аватара

### Transcribe API (`/api/transcribe`)
- **WebSocket** `/api/transcribe/ws` - WebSocket соединение для транскрипции аудио в реальном времени

## 🔍 Детальный анализ файлов

### Backend

#### `app/main.py`
Главный файл FastAPI приложения:
- **Функции**: 
  - Инициализация FastAPI приложения
  - Настройка CORS middleware
  - Подключение роутеров
  - Монтирование статических файлов
- **Особенности**: Автоматическая раздача `index.html` для SPA

#### `app/core/config.py`
Конфигурация приложения:
- **Класс**: `Settings` - настройки через Pydantic
- **Переменные**:
  - `OPENAI_API_KEY` - ключ OpenAI API
  - `HEYGEN_API_KEY` - ключ HeyGen API
  - `HEYGEN_SERVER_URL` - URL сервера HeyGen
  - `AVATAR_ID` - ID аватара по умолчанию
  - `VOICE_ID` - ID голоса по умолчанию

#### `app/routers/chat.py`
Роутер для чат-функциональности:
- **Классы**:
  - `ChatRequest` - модель запроса чата
- **Функции**:
  - `chat()` - основной эндпоинт чата с GPT-4
  - `send_to_avatar()` - отправка текста аватару
- **Особенности**: Стриминг ответов GPT-4 по предложениям

#### `app/routers/avatar.py`
Роутер для управления аватаром:
- **Классы**:
  - `SessionRequest` - параметры сессии аватара
  - `StartRequest` - запрос на запуск
  - `TaskRequest` - запрос на озвучивание текста
- **Функции**:
  - `_heygen_headers()` - формирование заголовков для HeyGen API
  - `create_streaming_token()` - получение токена
  - `new_session()` - создание сессии
  - `start_streaming()` - запуск стриминга
  - `send_task()` - отправка текста аватару
  - `stop_streaming()` - остановка стриминга

#### `app/routers/transcribe.py`
Роутер для транскрипции аудио:
- **Константы**:
  - `MIN_SEGMENT_BYTES` - минимальный размер сегмента
  - `SILENCE_THRESH_DB` - порог тишины
  - `MIN_SILENCE_LEN_MS` - минимальная длина тишины
- **Функции**:
  - `transcribe_stream()` - WebSocket эндпоинт
  - `is_silent()` - проверка на тишину
  - `flush()` - обработка накопленного аудио
- **Особенности**: Фильтрация шумов и автоматическая транскрипция

### Frontend

#### `public/index.html`
Главная HTML страница:
- **Структура**: Двухпанельный интерфейс (видео + чат)
- **Компоненты**:
  - Видеоплеер для аватара
  - Контейнер чата
  - Панель управления (микрофон, ввод, кнопки)
- **Библиотеки**: LiveKit Client для видеопотока

#### `public/js/avatar.js`
Управление аватаром:
- **Объекты**:
  - `ENDPOINTS` - API эндпоинты
  - `refs` - ссылки на DOM элементы
  - `window.avatarStream` - глобальное состояние аватара
- **Функции**:
  - `updateToggleColour()` - обновление цвета кнопки
  - `showSpinner()` / `hideSpinner()` - управление спиннером
  - `bindLiveKit()` - привязка LiveKit событий
  - `startAvatar()` - запуск аватара
  - `stopAvatar()` - остановка аватара
- **Особенности**: Интеграция с LiveKit для видеопотока

#### `public/js/chat.js`
Логика чата:
- **Функции**:
  - `addMessage()` - добавление сообщения в чат
  - `sendMessage()` - отправка сообщения и получение ответа
- **Интеграция**: Автоматическая отправка ответа аватару
- **Особенности**: Глобальная функция `window.sendMessage` для transcribe.js

#### `public/js/transcribe.js`
Захват и транскрипция аудио:
- **Переменные**:
  - `SILENCE_TIMEOUT` - таймаут тишины
  - `VAD_THRESHOLD` - порог детекции голоса
  - `NOISE_CALIBRATION_DURATION` - время калибровки шума
- **Функции**:
  - `createRecorder()` - создание MediaRecorder
  - `startStream()` - запуск аудио потока
  - `stopStream()` - остановка аудио потока
- **Особенности**: 
  - VAD (Voice Activity Detection)
  - Автоматическая калибровка шума
  - WebSocket стриминг аудио

#### `public/css/style.css`
Стили приложения:
- **CSS переменные**: Цветовая схема для состояний
- **Компоненты**:
  - `.main` - основная сетка
  - `.video-wrapper` - зона видео
  - `.chat-wrapper` - зона чата
  - `.message` - стили сообщений
  - `.spinner` - анимация загрузки
- **Особенности**: Адаптивный дизайн, flexbox layout

## 🔄 Поток данных

1. **Пользователь говорит** → `transcribe.js` захватывает аудио
2. **Аудио отправляется** → WebSocket на `/api/transcribe/ws`
3. **Сервер транскрибирует** → OpenAI Whisper API
4. **Текст отправляется** → `chat.js` через `window.sendMessage()`
5. **Запрос к GPT-4** → `/api/chat` эндпоинт
6. **Ответ разбивается** → на предложения
7. **Каждое предложение** → отправляется аватару через `/api/streaming/task`
8. **Аватар озвучивает** → текст в реальном времени

## 🎯 Основные возможности

- **Голосовой ввод** с автоматической транскрипцией
- **Чат с ИИ** через OpenAI GPT-4
- **Живой аватар** с синхронизированной речью
- **Реальное время** без задержек
- **Фильтрация шумов** для качественной транскрипции
- **Адаптивный интерфейс** для разных устройств

## 🚨 Требования к окружению

- **Python**: 3.11+
- **OpenAI API**: Активный ключ
- **HeyGen API**: Активный ключ с доступом к Streaming API
- **Браузер**: Поддержка WebRTC, WebSocket, MediaRecorder

## 🔐 Безопасность

### Работа с API ключами

1. **Локальная разработка**
   ```bash
   # Копируйте шаблон
   cp .env.example .env
   # Добавьте свои ключи в .env (файл НЕ попадет в Git)
   ```

2. **Проверка перед коммитом**
   ```bash
   # Запустите скрипт проверки
   ./scripts/check-secrets.sh
   ```

3. **GitHub Actions / CI/CD**
   - Используйте GitHub Secrets (Settings → Secrets)
   - Никогда не храните ключи в коде

Подробнее см. [docs/SECURITY.md](docs/SECURITY.md)

## 📝 Лицензия

Проект разработан для демонстрации интеграции AI-технологий с живыми аватарами.

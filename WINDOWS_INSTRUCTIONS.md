# 🚀 Инструкция по запуску Avatar в Windows

## Созданные файлы:

1. **AVATAR_MANAGER.bat** - Главное меню управления проектом
2. **WINDOWS_SETUP.bat** - Автоматическая установка окружения
3. **START_SERVER.bat** - Запуск сервера
4. **FIX_PYDANTIC.bat** - Исправление проблем с pydantic
5. **TEST_IMPORTS.py** - Проверка импортов
6. **run_server.py** - Python скрипт для запуска
7. **requirements_windows.txt** - Рабочие версии пакетов

## 📋 Как использовать:

### Способ 1: Через главное меню (рекомендуется)
1. Скопируйте все файлы в папку `D:\My_Projects\Avatar-v1`
2. Запустите **AVATAR_MANAGER.bat**
3. Выберите пункт 1 для полной установки
4. После установки выберите пункт 2 для запуска сервера

### Способ 2: Пошаговый запуск
1. Запустите **WINDOWS_SETUP.bat** для установки
2. Запустите **START_SERVER.bat** для старта сервера

### Способ 3: Если батники не работают
```powershell
cd D:\My_Projects\Avatar-v1
python run_server.py
```

## 🔧 Решение проблем:

### Ошибка с pydantic_core
- Запустите **FIX_PYDANTIC.bat**

### Проверка установки
- Запустите **TEST_IMPORTS.py**

### Альтернативная установка
```powershell
cd D:\My_Projects\Avatar-v1
python -m venv venv_new
venv_new\Scripts\activate
pip install -r requirements_windows.txt
```

## ✅ После успешного запуска:
- Откройте http://127.0.0.1:8000/ в браузере
- API документация: http://127.0.0.1:8000/docs

## ⚠️ Важно:
- Убедитесь, что в файле `.env` прописаны ваши API ключи
- Ключи должны быть БЕЗ кавычек
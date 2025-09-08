#!/usr/bin/env python
"""
Скрипт для запуска сервера Avatar
Решает проблемы с uvicorn в Windows
"""
import uvicorn
import sys
import os

# Добавляем текущую директорию в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("🚀 Запуск Avatar сервера...")
    print("📍 Откройте http://127.0.0.1:8000/ в браузере")
    print("⏹️  Нажмите Ctrl+C для остановки\n")
    
    try:
        uvicorn.run(
            "app.main:app",
            host="127.0.0.1",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n\n✅ Сервер остановлен")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        input("\nНажмите Enter для выхода...")
#!/bin/bash
# Скрипт для обновления .env с вашими ключами
# ВАЖНО: Замените YOUR_REAL_KEYS на ваши настоящие ключи!

cat > /workspace/.env << 'EOF'
# API ключи для проекта Avatar
OPENAI_API_KEY=YOUR_OPENAI_KEY_HERE
HEYGEN_API_KEY=YOUR_HEYGEN_KEY_HERE
EOF

echo "✅ .env файл обновлен!"
echo "🔄 Перезапускаем сервер..."

# Останавливаем старый сервер
pkill -f uvicorn

# Запускаем новый
cd /workspace
source venv_linux/bin/activate
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
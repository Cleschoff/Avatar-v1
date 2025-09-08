#!/bin/bash
# Скрипт проверки на случайные секреты перед коммитом

echo "🔍 Проверка на секреты в коде..."

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Проверяем .env в git status
if git status --porcelain | grep -q "^[AM].*\.env$"; then
    echo -e "${RED}❌ ОШИБКА: Файл .env добавлен в git!${NC}"
    echo "Используйте: git rm --cached .env"
    exit 1
fi

# Ищем потенциальные ключи OpenAI
echo "Поиск ключей OpenAI..."
if grep -r "sk-[a-zA-Z0-9]\{40,\}" . \
    --exclude-dir=.git \
    --exclude-dir=venv \
    --exclude-dir=venv_linux \
    --exclude-dir=node_modules \
    --exclude=*.log \
    --exclude=.env \
    --exclude=.env.* 2>/dev/null; then
    echo -e "${RED}❌ Найдены потенциальные API ключи!${NC}"
    exit 1
fi

# Ищем прямые присвоения ключей
echo "Поиск прямых присвоений..."
if grep -r "OPENAI_API_KEY\s*=\s*[\"'][^\"']\+[\"']" . \
    --exclude-dir=.git \
    --exclude-dir=venv \
    --exclude-dir=venv_linux \
    --exclude=*.log \
    --exclude=.env \
    --exclude=.env.* \
    --exclude=.env.example \
    --exclude=check-secrets.sh 2>/dev/null | \
    grep -v "your_openai_api_key_here" | \
    grep -v "dummy_key_for_testing"; then
    echo -e "${RED}❌ Найдены прямые присвоения API ключей!${NC}"
    exit 1
fi

# Проверяем .gitignore
if ! grep -q "^\.env$" .gitignore; then
    echo -e "${YELLOW}⚠️  Предупреждение: .env не найден в .gitignore${NC}"
fi

echo -e "${GREEN}✅ Проверка пройдена! Секреты не найдены.${NC}"

# Дополнительные рекомендации
echo ""
echo "📌 Рекомендации:"
echo "  - Используйте 'git status' перед каждым коммитом"
echo "  - Храните ключи только в .env файле"
echo "  - Для CI/CD используйте GitHub Secrets"
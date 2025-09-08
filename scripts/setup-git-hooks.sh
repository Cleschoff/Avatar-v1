#!/bin/bash
# Настройка Git hooks для проверки секретов

echo "🔧 Настройка Git hooks..."

# Настраиваем Git для использования нашей папки с хуками
git config core.hooksPath .githooks

echo "✅ Git hooks настроены!"
echo ""
echo "Теперь при каждом коммите будет автоматически:"
echo "  - Проверяться наличие .env в коммите"
echo "  - Искаться случайные API ключи"
echo ""
echo "Чтобы отключить проверку (не рекомендуется):"
echo "  git config --unset core.hooksPath"
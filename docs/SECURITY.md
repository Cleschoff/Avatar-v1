# Безопасность и управление секретами

## 🔐 Локальная разработка

1. **Никогда не коммитьте .env файл**
   - Файл `.env` уже добавлен в `.gitignore`
   - Проверяйте перед каждым коммитом: `git status`

2. **Используйте .env.example**
   ```bash
   # Копируйте шаблон
   cp .env.example .env
   # Добавьте свои ключи
   ```

## 🚀 Продакшен деплой

### Vercel
```bash
vercel env add OPENAI_API_KEY
vercel env add HEYGEN_API_KEY
```

### Heroku
```bash
heroku config:set OPENAI_API_KEY=your-key
heroku config:set HEYGEN_API_KEY=your-key
```

### Railway
Добавьте переменные в веб-интерфейсе или:
```bash
railway variables set OPENAI_API_KEY=your-key
```

### Docker
```dockerfile
# Используйте build args
ARG OPENAI_API_KEY
ARG HEYGEN_API_KEY
ENV OPENAI_API_KEY=$OPENAI_API_KEY
ENV HEYGEN_API_KEY=$HEYGEN_API_KEY
```

## 📱 GitHub Mobile/Codespaces

### GitHub Codespaces
1. Settings → Codespaces → Secrets
2. Добавьте OPENAI_API_KEY и HEYGEN_API_KEY
3. Секреты автоматически доступны в Codespace

### GitHub Actions
```yaml
name: Deploy
on: push

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          HEYGEN_API_KEY: ${{ secrets.HEYGEN_API_KEY }}
        run: |
          # Ваши команды деплоя
```

## ⚠️ Безопасность ключей

### Что делать:
- ✅ Используйте разные ключи для dev/staging/prod
- ✅ Ротируйте ключи регулярно
- ✅ Ограничивайте права ключей (если возможно)
- ✅ Мониторьте использование

### Чего НЕ делать:
- ❌ Не храните ключи в коде
- ❌ Не отправляйте ключи в чаты/email
- ❌ Не используйте production ключи для разработки
- ❌ Не делитесь личными ключами

## 🔍 Проверка безопасности

Перед каждым push:
```bash
# Проверьте, что .env не в staging
git status

# Поиск случайных ключей в коде
grep -r "sk-" . --exclude-dir=.git --exclude-dir=venv
grep -r "OPENAI_API_KEY=" . --exclude-dir=.git --exclude=.env*

# Используйте pre-commit hooks
pip install pre-commit
pre-commit install
```

## 🆘 Если ключ утек

1. **Немедленно отзовите ключ** в OpenAI/HeyGen dashboard
2. Создайте новый ключ
3. Обновите все окружения
4. Проверьте логи на подозрительную активность
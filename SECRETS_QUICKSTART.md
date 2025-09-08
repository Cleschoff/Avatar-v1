# 🚀 Быстрый старт: Настройка API ключей

## Шаг 1: Получите API ключи

### OpenAI (GPT-4)
1. Перейдите на https://platform.openai.com/api-keys
2. Нажмите "Create new secret key"
3. Сохраните ключ (начинается с `sk-`)

### HeyGen (Аватар)
1. Перейдите на https://app.heygen.com/settings
2. Найдите раздел API
3. Создайте или скопируйте ключ

## Шаг 2: Локальная настройка

```bash
# 1. Скопируйте шаблон
cp .env.example .env

# 2. Откройте файл для редактирования
# Windows:
notepad .env
# Mac/Linux:
nano .env

# 3. Вставьте ваши ключи:
OPENAI_API_KEY=sk-ваш-настоящий-ключ-здесь
HEYGEN_API_KEY=ваш-heygen-ключ-здесь
```

## Шаг 3: Проверка

```bash
# Убедитесь, что .env НЕ в git
git status

# Должно показать:
# nothing to commit, working tree clean
# 
# НЕ должно показывать .env в списке файлов!
```

## ⚠️ Важно!

- **НИКОГДА** не коммитьте .env файл
- **ВСЕГДА** проверяйте `git status` перед push
- **ИСПОЛЬЗУЙТЕ** разные ключи для разработки и продакшена

## 🆘 Если случайно закоммитили ключ

```bash
# 1. Удалите из git (файл останется локально)
git rm --cached .env

# 2. Коммит изменений
git commit -m "Remove .env from tracking"

# 3. ВАЖНО: Смените ключи в OpenAI/HeyGen!
```

## 📱 Для GitHub Codespaces

1. Откройте Settings → Codespaces → Secrets
2. Добавьте:
   - `OPENAI_API_KEY`
   - `HEYGEN_API_KEY`
3. Перезапустите Codespace

## 🚀 Для деплоя

См. [docs/SECURITY.md](docs/SECURITY.md) для настройки на хостинге.
# 🔧 Исправление ошибок с API ключами в .env

## Проблема
Красное подчеркивание ключей в VSCode/Cursor означает, что они обернуты в кавычки, что неправильно для .env файлов.

## Решение

### 1. Откройте файл .env

### 2. Удалите кавычки вокруг значений

❌ **НЕПРАВИЛЬНО** (с кавычками):
```env
OPENAI_API_KEY="sk-proj-ef4owGMRUs75v0xGr..."
HEYGEN_API_KEY="RjcIPkDwJRDkMcl2..."
```

✅ **ПРАВИЛЬНО** (без кавычек):
```env
OPENAI_API_KEY=sk-proj-ef4owGMRUs75v0xGr...
HEYGEN_API_KEY=RjcIPkDwJRDkMcl2...
```

### 3. Полный правильный формат .env:
```env
# БЕЗ КАВЫЧЕК!
OPENAI_API_KEY=sk-proj-ef4owGMRUs75v0xGr_dbA2zJRs3T-GlQVtAkRDN3UllIosd28PNd2n_t7xcFF9xVHg7lbcIbcdp1ab1bkJ-hm2JYKjzAjv21Xemqw6C5CEQMp6aMqX1zopRJS
HEYGEN_API_KEY=RjcIPkDwJRDkMcl2HBDMYzg8tXJCjMUJNZdMl2Jcy7JgtATczu0Y1UTU5Mu
```

### 4. Сохраните файл (Ctrl+S)

### 5. Проверьте формат:
```bash
python scripts/validate-env.py
```

### 6. Перезапустите сервер:
```bash
# Windows
venv\Scripts\activate
uvicorn app.main:app --reload

# Linux/Mac
source venv/bin/activate
uvicorn app.main:app --reload
```

## 📌 Важные правила .env файлов

1. **НЕ используйте кавычки** (ни двойные ", ни одинарные ')
2. **НЕ добавляйте пробелы** вокруг знака =
3. **Каждая переменная** на новой строке
4. **Комментарии** начинаются с #

## 🔍 Проверка

После исправления:
- Красное подчеркивание должно исчезнуть
- API функции начнут работать
- В консоли не будет ошибок авторизации

## ⚠️ Безопасность

- Убедитесь, что .env в .gitignore
- Никогда не коммитьте файл с реальными ключами
- Используйте `git status` перед каждым push
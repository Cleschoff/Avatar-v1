#!/usr/bin/env python3
"""
Скрипт проверки формата .env файла
"""
import os
import re
import sys

def validate_env_file(filepath=".env"):
    """Проверяет правильность формата .env файла"""
    
    if not os.path.exists(filepath):
        print(f"❌ Файл {filepath} не найден!")
        return False
    
    errors = []
    warnings = []
    line_num = 0
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line_num += 1
            line = line.strip()
            
            # Пропускаем пустые строки и комментарии
            if not line or line.startswith('#'):
                continue
            
            # Проверяем формат KEY=VALUE
            if '=' not in line:
                errors.append(f"Строка {line_num}: Нет знака '=' - {line}")
                continue
            
            key, value = line.split('=', 1)
            
            # Проверка ключа
            if ' ' in key:
                errors.append(f"Строка {line_num}: Пробелы в имени переменной - '{key}'")
            
            # Проверка на кавычки
            if value.startswith('"') and value.endswith('"'):
                warnings.append(f"Строка {line_num}: Удалите кавычки вокруг значения - {key}=\"{value}\"")
                warnings.append(f"  Правильно: {key}={value[1:-1]}")
            elif value.startswith("'") and value.endswith("'"):
                warnings.append(f"Строка {line_num}: Удалите кавычки вокруг значения - {key}='{value}'")
                warnings.append(f"  Правильно: {key}={value[1:-1]}")
            
            # Проверка API ключей
            if key == "OPENAI_API_KEY":
                if value.startswith('"sk-') or value.startswith("'sk-"):
                    errors.append(f"❌ OPENAI_API_KEY обернут в кавычки! Удалите их.")
                elif not value.startswith('sk-'):
                    warnings.append(f"⚠️  OPENAI_API_KEY должен начинаться с 'sk-'")
            
            if key == "HEYGEN_API_KEY":
                if value.startswith('"') or value.startswith("'"):
                    errors.append(f"❌ HEYGEN_API_KEY обернут в кавычки! Удалите их.")
    
    # Вывод результатов
    print(f"\n🔍 Проверка файла {filepath}:")
    print("=" * 50)
    
    if errors:
        print("\n❌ ОШИБКИ (нужно исправить):")
        for error in errors:
            print(f"  {error}")
    
    if warnings:
        print("\n⚠️  ПРЕДУПРЕЖДЕНИЯ:")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors and not warnings:
        print("✅ Формат файла корректный!")
        return True
    
    if errors:
        print("\n💡 СОВЕТ: В .env файлах НЕ нужны кавычки вокруг значений!")
        print("Правильный формат: KEY=value")
        print("Неправильный формат: KEY=\"value\" или KEY='value'")
    
    return len(errors) == 0

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else ".env"
    valid = validate_env_file(filepath)
    sys.exit(0 if valid else 1)
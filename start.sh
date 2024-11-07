#!/bin/bash

# Проверка наличия Python
if command -v python &> /dev/null; then
    PYTHON_COMMAND="python"
elif command -v python3 &> /dev/null; then
    PYTHON_COMMAND="python3"
else
    echo "Python не установлен"
    exit 1
fi

# Создание виртуального окружения
VENV_DIR=".venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Создание виртуального окружения..."
    $PYTHON_COMMAND -m venv $VENV_DIR
else
    echo "Виртуальное окружение уже существует"
fi

# Активация виртуального окружения
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source "$VENV_DIR/Scripts/activate"
else
    source "$VENV_DIR/bin/activate"
fi

# Установка зависимостей
echo "Установка зависимостей..."
poetry install

# Установка pre-commit хуков
poetry run pre-commit install

cp ./.env.example ./.env
docker-compose --env-file .env up -d
mkdir -p data/raw data/processed

echo "Настройка завершена! Виртуальное окружение создано, зависимости и pre-commit хуки установлены, контейнер с Minio поднят."

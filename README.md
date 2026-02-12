# Проект автотестов для API Прилавка

Данный проект содержит автотесты для проверки поля `name`
в эндпоинте создания набора `/api/v1/kits`.

## Используемые технологии:
- Python
- pytest
- requests

## Структура проекта:

configuration.py — настройки сервера  
data.py — тестовые данные  
sender_stand_request.py — функции для отправки HTTP-запросов  
create_kit_name_kit_test.py — автотесты  

## Запуск тестов

1. Установить зависимости:
pip install pytest requests

2. Запустить сервер.

3. Выполнить команду:
pytest -v

API Autotests Project
Проект автоматизированного тестирования API с использованием Python, pytest и Allure Reports.

Технологии
Python 3.8+ - основной язык программирования
Pytest - фреймворк для тестирования
Allure Report - система отчетности

Установка и настройка
1. Клонирование репозитория
git clone https://github.com/RedLosk/API-test-petstore

2. Настройка виртуального окружения
python -m venv .venv
.venv\Scripts\activate     # Windows

3.Установка зависимостей
pip install -r requirements.txt

Запустите автотесты:
pytest

С подробным выводом
pytest -v

Для открытия отчета в Allure:
pytest --alluredir=./allure-results


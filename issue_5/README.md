# ISSUE-04

Тест функции what_is_year_now() с использованием pytest, unittest.mock, а также pytest-cov.

## Для запуска необходимо


1. Склонировать проект
2. Перейти в директорию `issue-05`
3. Запустить файл `issue_5.py`, используя команды:

```bash
python -m pytest -v issue_5.py
python -m pytest -v issue_5.py --cov
python -m pytest -q issue_5.py --cov . --cov-report html

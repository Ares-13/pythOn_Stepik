# Используем официальный Python образ
FROM python:3.12.6-slim
# Устанавливаем рабочую директорию
WORKDIR /app
# Копируем файл с числами Фибоначчи в контейнер
# Копируем в /app/fibonacci.py
COPY fibonacci.py . 

ENTRYPOINT [ "python" ]
CMD [ "fibonacci.py" ]
# Команда которая выполнится при запуске контейнера

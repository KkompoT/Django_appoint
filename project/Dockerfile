
FROM python:4.2
# Рабочая директория
WORKDIR /app
# Копирую файл с зависимостями в рабочую директорию
COPY requirements.txt .
# инсталю зависимости
RUN pip install --no-cache-dir -r requirements.txt
# Копирую все файлы проекта в рабочую директорию
COPY . .

# Устанавливаю переменные окружения для Django
ENV DJANGO_SETTINGS_MODULE=appoint,settings
ENV PYTHONUNBUFFERED=1

# Запускаю команду для коллекции статических файлов
RUN python manage.py collectstatic --noinput

# Команды для создания и применения миграций
RUN python manage.py makemigrations
RUN python manage.py migrate

# Открываю порт для взаимодействия с контейнером
EXPOSE 8000

CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']




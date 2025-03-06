
FROM python:3.9

WORKDIR /code
COPY requirements.txt /code/
COPY . /code/

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py shell < create_superuser.py && python manage.py runserver 0.0.0.0:8000"]

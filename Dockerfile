FROM python:3.8
LABEL authors="fabioacarvalho"

WORKDIR /app

COPY requirements.txt /app/
COPY . /app/

# Atualiza o pip
RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Django Interview with ChatGPT

This project is an interviewer that uses the ChatGPT API to generate questions based on the requirements of registered vacancies and in the end generates feedback from the candidate.

## What you need to use this project

- Create an account at OpenAI;
- Create an API_KEY;
- Rename the file .env_example to .env and change the necessary data.

---

## Starting the project with Docker
 
### Buildind the image Docker

```shell
    docker build -t chat .
```
<br>

### Starting the container

```shell
    docker run -p 8000:8000 chat
```

<br>

---

## Starting locally

### Install the dependencies:

```shell
    pip install -r requirements.txt
```

<br>

### Run migrate:


```shell
    python manage.py migrate
```

<br>

### Create a super user:

```shell
    python manage.py createsuperuser
```
<br>

### Iniciando o servidor:

```shell
    python manage.py runserver
```

Acesse: [localhost:8000/admin](localhost:8000/admin)

<br>

---

# Preview

### Home adm:

<img src="https://github.com/fabioacarvalho/django-interview-chatgpt/blob/main/assets/img/adm.png?raw=true">

<br>

### List of Jobs

<img src="https://github.com/fabioacarvalho/django-interview-chatgpt/blob/main/assets/img/ListadeVagas.png?raw=true">
<br>

### Create Jobs

<img src="https://github.com/fabioacarvalho/django-interview-chatgpt/blob/main/assets/img/Jobs.png?raw=true">

<br>

### Chat Interview

<img src="https://github.com/fabioacarvalho/django-interview-chatgpt/blob/main/assets/img/InterviewChat1.png?raw=true">

<br>

### Feedback Interview

<img src="https://github.com/fabioacarvalho/django-interview-chatgpt/blob/main/assets/img/InterviewChat2.png?raw=true">
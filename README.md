# Django Interview Chatgpt

Este projeto é um entrevistador que utiliza a API do ChatGPT para gerar perguntas baseado nos requisitos das vagas cadastradas e no final gera um feedback do candidato.

## O que você precisa para utilizar este projeto

- Criar uma conta no OpenAI
- Criar um API_KEY

---

## Iniciando projeto utilizando Docker
 
### Construindo a imagem Docker

```shell
    docker build -t chat .
```
<br>

### Iniciando o contâiner

```shell
    docker run -p 8000:8000 chat
```

<br>

---

## Iniciando Localmente

### Instalando as dependências:

```shell
    pip install -r requirements.txt
```

<br>

### Rodando o migrate:


```shell
    python manage.py migrate
```

<br>

### Criando um super usuário:

```shell
    python manage.py createsuperuser
```
<br>

### Iniciando o servidor:

```shell
    python manage.py runserver
```

Acesse: localhost:8000/admin

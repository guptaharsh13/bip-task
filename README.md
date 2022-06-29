# Bip Task

REST API Backend for Bip Task

## About the Backend

- API
  - Blog API should have 4 Models Posts, Tags, Comments, Authors
  - Post can have many Tags
  - Post can have many Comments
  - Post can have one User
  - CRUD API for Post/Tag/Comment
- API documentation with Swagger
- Databse for this SHOULD be SQLiteCode

## Tools and technology used

- Python3.8
- Django
- Django Rest Framework
- Docker
- pythonanywhere

## Getting Started

To get started

- Clone the repo.

```shell
git clone https://github.com/guptaharsh13/bip-task
```

- Change into the directory.

```shell
cd bip-task
```

### Environment Variables

```shell
touch .env
```

**For running this project successfully you'll need to create a `.env` file and store your firebase credentials there like [`.env.sample`](https://github.com/guptaharsh13/bip-task/tree/master/.env.sample).**

### Local Build

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

### Docker Build

You may install Docker Engine from [here](https://docs.docker.com/engine/install/)

#### Development Run

```shell
docker-compose up --build
```

#### Production Run

```shell
docker build -t <docker hub username>/bip-task .
docker run -p <local port>:80 --env-file .env <docker hub username>/bip-task
```

## API Documentation

- [Swagger](https://hg242322.pythonanywhere.com/swagger/)
- [Redoc](https://hg242322.pythonanywhere.com/redoc/)

## Future Scope

- Add a Custom User model
- Implement Authentication
- Implement Testing

<p align="center">Made with ❤ by Harsh Gupta</p>

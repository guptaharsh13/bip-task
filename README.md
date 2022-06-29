# Bip Task

You can checkout the deployed app [here](https://hg242322.pythonanywhere.com/)
- [Admin Panel](https://hg242322.pythonanywhere.com/bip-task/admin)
  - username - admin
  - password - admin

<details>
<summary>About the Backend</summary>
<ul>
  <li>API</li>
  <ul>
    <li>Blog API should have 4 Models Posts, Tags, Comments, Authors</li>
    <li>Post can have many Tags</li>
    <li>Post can have many Comments</li>
    <li>Post can have one User</li>
    <li>CRUD API for Post/Tag/Comment</li>
</ul>
  <li>API documentation with Swagger</li>
  <li>Databse for this SHOULD be SQLiteCode</li>
</ul>
</details>

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

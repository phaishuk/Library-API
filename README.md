# Library Service

Online management system for book borrowings.

## Features

* JWT authenticated.
* Admin panel /admin/
* Documentation at /api/doc/swagger/
* Books inventory management.
* Books borrowing management.
* Notifications service through Telegram API (bot and chat).
* Scheduled notifications with Django Q and Redis.
* Payments handle with Stripe API.

## Getting access

* create user via /api/users/
* get access token via /api/users/token/

## How to run with Docker

Docker should be installed.

Create `.env` file with your variables (look at `.env.sample`
file, don't change `POSTGRES_DB` and `POSTGRES_HOST`).

```shell
docker-compose build
docker-compose up
```

## How to run locally (without docker)

Install PostgreSQL and create database.

1. Clone project and create virtual environment

```shell
git clone git@github.com:phaishuk/Library-API.git
cd LibraryAPI
python -m venv venv
source venv/bin/activate # on MacOS
venv\Scripts\activate # on Windows
pip install -r requirements.txt
```
2. Set environment variables

Check out `.env.sample` file -> put all necessary variables -> rename `.env.sample` to `.env`

3. Make migrations and run server

```shell
python manage.py migrate
python manage.py runserver
```

4. Getting daily scheduled notifications in Telegram

* in settings.py in `Q_CLUSTER` configuration change 
redis host from `redis` to `127.0.0.1`
* start Redis server
* run `python manage.py qcluster`
* run in separate terminal `python manage.py shell`
to open interactive console
* to activate scheduled task write in the opened console 
`from borrowing import tasks` 
* the task will be first processed in a minute after activating 
and will be scheduled for the same time the next day


A telegram bot has already been created for this application - https://t.me/libraryapi_bot 
1. Write any message in bot
2. To retrieve chat_id use script `teleram-script.py`.
3. Add to env variables `chat_id` retrieved by script, to test functionality.

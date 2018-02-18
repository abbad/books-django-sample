#!/bin/sh

# wait for PSQL server to start
echo 'Sleep for 10 seconds just to make sure that PSQL is running'
sleep 10

cd books_api

echo 'Run migrations.'
python3 manage.py migrate
echo 'Create a couple of fake users to populate the db.'
python3 manage.py create_fake_users
echo 'Run the server.'
python3 manage.py runserver 0.0.0.0:8000

django-admin startproject <name>
py manage.py startapp <name>
py manage.py startapp <name>
git add .
git commit -m ""  
git push -u origin main

adminer:
    docker-compose up -d //run
    http://localhost:8080
    root : 123123
    docker-compose down //stop
    docker-compose down -v //delete


Use Twilio to verify phone number
    pip install twilio

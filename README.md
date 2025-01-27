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


create container in docker:
    add folder DataDiamondShop to drive D
    in command docker use code:
    docker run --name DiamondShop -e MYSQL_ROOT_PASSWORD=12344321 -e MYSQL_DATABASE=CuaHangKimCuong -p 3307:3306 -v D:/DataDiamondShop:/var/lib/mysql -d mysql:latest
    setting in file settings.py
    run: python manage.py makemigrations
         python manage.py migrate


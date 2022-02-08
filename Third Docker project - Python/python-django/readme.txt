By default Django runs on 127.0.0.1:8000

However that's possible to modify explicitely when launching the app (keep that in mind when creating dockerfile and exposing ports in docker file).
Alternative is to hardcode default port and host, but that's not the case here

-- Run on 127.0.0.1:7000 --
python manage.py runserver 7000 || python manage.py runserver 0.0.0.0:7000

-- Run on 127.0.0.1:7000 --
python manage.py runserver 127.10.10.10:7000

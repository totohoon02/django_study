# DJANGO REST FRAMEWORK

### project setup

```
pip install django
django-admin startproject myweb .
python manage.py startapp photo

# run
python manage.py runserver
```

### settings.py

```
USER_APPS = [
    'photo'
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = USER_APPS + DJANGO_APPS

...

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

### migrate & create superuser

```
python manage.py migrate
python manage.py createsuperuser # /admin
```

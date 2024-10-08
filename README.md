# DJANGO STUDY

### PROJECT DIRS

- DRF : Photo App
- Todo : Todo App

### ENV Settings

- python 3.10
- 'venv' on each apps

## <p style="color:#2372dc">DJANGO Settings</p>

### project setup

```
pip install django
django-admin startproject myweb .
python manage.py startapp photo

# run
python manage.py runserver
```

### <p style="color:black">settings.py</p>

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

### Model

- 데이터베이스의 스키마 정의
- 데이터베이스를 적용시키는 과정을 마이그레이션

```
django-admin makemigrations
django-admin migrate
```

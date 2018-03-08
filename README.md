# Welcome to PHONEDB project. It work on django 1.9.

You need add file bookmarks/settings_local.py. Example file:
```python
import os
from settings.settings import BASE_DIR
SECRET_KEY = 'TOKEN'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

# Installing

You must be use Python version 3.6.2. Install Python package with:
```
pip install -r requirements.txt
```
Description:

Данный проект разработан для хранения и поддержания в актуальном состоянии номерного плана клиентов. Разработка ведется для опратора связи. Здесь будет вестись учет основных параметров(номер, пароли, адреса, описание, устройства, логины, пароли, wan, и т.д.). Нужен в первую очередь для учета и аудита.

RoadMap:

Необходимо прикрутить фильтр по всем клиентам, 
добавить учетки readonly, readwrite
Добавить сортировку по столбцам.
Разобраться с формами

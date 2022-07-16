# api_final

<center>
    <a href='https://github.com/kluevEVGA/api_final_yatube/blob/master/LICENSE'>
      <img src='https://img.shields.io/static/v1?label=LICENSE&message=MIT&color=97ca00&style=for-the-badge' alt='bage'/>
     </a>
    <a href='https://python.org'>
      <img src='https://img.shields.io/static/v1?label=Python&message=3.17.3&color=97ca00&style=for-the-badge' alt='bage'/>
     </a>
    <a href='#'>
      <img src='https://img.shields.io/static/v1?label=API&message=1.0.0&color=97ca00&style=for-the-badge' alt='bage'/>
     </a>
</center>

## О проекте

Проект реализует REST API backend сервис на базе встроенной в Python sqlite базы данных.

## Установка

#### Клонировать проект:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git
```

#### Установка окружения:

<p style="font-style: italic">Linux / windows</p>

```
python3 -m venv env
py -m venv venv
```

#### Активировать окружение:

<p style="font-style: italic">Bash(sh) / powerShell</p>

```
source env/bin/activate
.\venv\Scripts\activate
```

#### Установить зависимости:

```
pip install -r requirements.txt
```

#### Запустить проект:

<p style="font-style: italic">
Перейти в папку с проектом, выполнить миграции, запустить сервер
</p>

```
cd .\yatube_api\
python3 manage.py migrate
py manage.py runserver
```

<!-- ЛИЦЕНЗИЯ -->

## Лицензия

Distributed under the `MIT` License. See [LICENSE](https://github.com/kluevEVGA/api_final_yatube/blob/master/LICENSE)
for more
information.

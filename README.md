# Проект по курсу Web-технологии (VK Образование)

В репозитории реализован проект по дисциплине Web-технологии 2022 Технопарка (VK образование) МГТУ им. Н. Э. Баумана. 

**Условия проекта:** [https://github.com/ziontab/tp-tasks](https://github.com/ziontab/tp-tasks)

***Стек технологий:***
<br>
**Frontend:** Bootstrap
<br>
**Backend:** Python Django


```bash
python3 -m venv venv
python3 manage.py startapp app
python3 manage.py runserver

python3 manage.py makemigrations app
python3 manage.py migrate app

python3 manage.py fill_db -a 400000
```

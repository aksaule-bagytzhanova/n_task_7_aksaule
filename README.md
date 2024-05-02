<h1 align="center">This is my project for Task №7 </h1> 
<h3 align="center">My name is Aksaule, CSS student from SDU, I am currently working as a designer</h3>


## Database
![Фото дб](https://github.com/aksaule-bagytzhanova/n_task_7_aksaule/blob/main/readme%20photos/DB.png)

## models.py
С начала мое дб выглядело очень легким и примитивным

Но при процессе я поняла что: 

```markdown
    1. Нужно чтобы Юзеры и Мероприятия должны были связываться в бронировании 
    2. Нужно было чтобы не зарегистрированные пользователи не могли зарегистрироваться на мероприятие и так далее 
```

И вот что у меня вышло в конце

![Фото models.py](https://github.com/aksaule-bagytzhanova/n_task_7_aksaule/blob/main/readme%20photos/models.png)

## Структура проекта 

В конечном итоге у меня вышло 1 проект и 2 приложения 

```markdown
    - Проект: website 
    - Application 1: Users
    - Application 2: Concerts
```
![Фото project](https://github.com/aksaule-bagytzhanova/n_task_7_aksaule/blob/main/readme%20photos/project_s.png)


## User 

При написании моделек Юзера я использовала AbstractUser, что намного облегчело мне работу

А дальше работа была примитивной, добавила form.py чтобы увеличить атрибуты AbstractUser и добавила поле для почты

Все кнобки Логина поставила в navbar и все это разукрасила с bootstrap




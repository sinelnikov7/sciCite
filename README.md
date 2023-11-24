Для запуска приложения необходимо указать в файле .env переменные <br />
где:<br />
DB_USER Логин пользователя базы данных<br />
DB_PASS Пароль базы данных<br />
PGADMIN_DEFAULT_EMAIL Почта для входа в pgadmin<br />
PGADMIN_DEFAULT_PASSWORD Пароль для входа в pgadmin<br />
DB_HOST Хост базы данных<br />
DB_PORT Порт базы данных<br />
DB_NAME Имя базы данных<br />
API_ID Api-ID приложения Telegram<br />
API_HASH Api-hash приложения Telegram<br />
VK_KEY Ключ приложения Вконтакте<br />
<br />
Также для работы нужно установить wkhtmltopdf для создания PDF документа из html шаблона <br />
Для windows скачать и устоновить из https://wkhtmltopdf.org/downloads.html и указать путь в переменной среды PATH
Для Linux sudo apt-get -y install wkhtmltopdf <br />
Установить зависимости pip install -r requirements.txt<br />
Запустить докер docker-compose up из корня каталога<br />
Запустить миграции alembic<br />
alembic revision --autogenerate -m "fist migration" – создание миграций<br />
alembic upgrade head – создание таблиц(применение миграций)<br />
<br />
Созданы Ендпоинты:<br />
<br />
Создание юзера: <br />
method POST <br />
/user/add<br />
{<br />
  "name": "string",<br />
  "surname": "string"<br />
}<br />
<br />
Добовление аккаунта Вконтакте у юзера: <br />
method POST <br />
/vk/add <br />
{ <br />
  "user_id": int, <br />
  "vk_id": "string" <br />
} <br />
<br />
Добовление контакта Telgram: <br />
method POST <br />
/telegram/add <br />
{ <br />
  "user_id": int, <br />
  "telegram_login": "string" <br />
} <br />
<br />
Добовление контакта Instagram: <br />
method POST <br />
/instagram/add <br />
{ <br />
<br />
  "user_id": int, <br />
  "instagram_login": "string" <br />
} <br />
<br />
Формирование отчета по выбранному юзеру: <br />
method GET <br />
/user/generate_pdf/{user_id} <br />
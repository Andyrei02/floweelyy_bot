# floweelyy_bot

Install Alembic
alembic init migrations
Configure alembic.ini
sqlalchemy.url = postgresql+asyncpg://user:pass@localhost/dbname
Create a Migration
alembic revision -m "add products table"
Then run:
alembic upgrade head



## ToDo
- Отчет об активности пользователей: Команда /user_activity отображает количество новых отзывов пользователей.
    - Всего пользователей
    - Новых за сегодня
    - Новых за неделю
    - Новых за месяц
    - Данные актуальны на текущий момент
- Уведомления
    - Уведомление о новом заказе: Бот отправляет сообщение в Telegram-чат при создании нового заказа, включая информацию о пользователе и заказанных продуктах. 
    - Уведомление об отмене заказа
- Django: Веб-фреймворк, использующийся для обработки данных и интеграции с ботом
- REST API: Для взаимодействия с Telegram API и отправки уведомлений. 
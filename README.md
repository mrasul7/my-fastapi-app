## 🚀 Функциональность

### Telegram Бот
* **Команды:**
  * `/start` - Приветственное сообщение и регистрация пользователя в системе
* **Интерактивные элементы:**
  * Кнопка "Поделиться номером" для отправки контактных данных
  * Inline-кнопка "Мои данные" для просмотра сохраненной информации
  * Навигация "Назад" в меню

### FastAPI Backend
* **API Endpoints:**
  * `POST /user/send_message` - Отправка сообщения пользователю по номеру телефона
* **Аутентификация:** API защищено токеном
* **Документация API:** Автоматически сгенерированная документация доступна по адресу `/docs`

## 📦 Установка и Запуск
uv pip install -r requirements.txt
docker-compose up

### Предварительные требования
* Python 3.10+
* PostgreSQL база данных
* Telegram Bot Token от [@BotFather](https://t.me/BotFather)



Отправка сообщения пользователю
POST /user/send_message
Authorization: Bearer your_api_token
Content-Type: application/json

{
  "phone_number": "79991234567",
  "text": "Текст сообщения"
}
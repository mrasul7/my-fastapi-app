FROM python:3.13-slim

WORKDIR /app

# Устанавливаем uv
RUN pip install uv

# Копируем файлы зависимостей
COPY pyproject.toml uv.lock ./

# Устанавливаем зависимости через uv
RUN uv sync --frozen --no-dev

# Копируем весь код проекта
COPY . .

ENV PYTHONPATH=/app
ENV PATH="/app/.venv/bin:$PATH"

# Запускаем бота (точка входа - bot_service.py)
CMD ["python", "bot_service.py"]
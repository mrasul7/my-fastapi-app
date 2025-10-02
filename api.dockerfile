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

# Запускаем API (точка входа - api_service.py)
CMD ["python", "api_service.py"]
FROM python:3.11

# Installing worcking dir and poetry
WORKDIR /WB_Notice_task

RUN pip install poetry

COPY pyproject.toml poetry.lock* /WB_Notice_task/
# Disable venv poetry, 
RUN poetry config virtualenvs.create false
# Installing libs
RUN poetry install --no-dev



# Coping cod
COPY . /WB_Notice_task

# Укажите команду для запуска приложения
CMD ["python", "main.py"]

FROM python:3.9

WORKDIR /opt/app

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

ENV PATH="${PATH}:/opt/poetry/bin"

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python -
RUN echo $PATH
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

CMD [ "python", "./app.py" ]
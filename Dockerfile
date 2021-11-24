FROM python:3.7.2
COPY . /app
WORKDIR /app
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python

ENV PATH="${PATH}:/opt/poetry/bin"
RUN ln -s /opt/poetry/bin/poetry poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev


WORKDIR /app/dockerip

ENV PORT 8000


CMD ["sh", "-c" ,"gunicorn main:app --bind :$PORT"]
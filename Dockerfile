FROM python:3.9.12-slim

WORKDIR /code

RUN pip install fastapi uvicorn jinja2

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

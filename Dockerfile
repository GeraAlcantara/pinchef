FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/requirements.txt

# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk update && \
    apk add --virtual build-base gcc g++ musl-dev && \
    apk add postgresql-dev libressl-dev libffi-dev libpq alpine-sdk

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
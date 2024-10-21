FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app/
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./api/  /app/api/
COPY ./app/  /app/app/
COPY ./tests/  /app/tests/
COPY ./entrypoint.sh  /app/

ENTRYPOINT ["./entrypoint.sh"]

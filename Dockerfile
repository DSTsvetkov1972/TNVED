# FROM python:3.10-slim

# WORKDIR /app

# COPY ./requirements.txt /app/
# RUN pip install -r requirements.txt

# ENV PYTHONPATH=/app/
# ENV PYTHONUNBUFFERED=1
# ENV PYTHONDONTWRITEBYTECODE=1



# COPY ./api/  /app/api/
# COPY ./app/  /app/app/
# COPY ./tests/  /app/tests/
# COPY ./entrypoint.sh  /app/

# ENTRYPOINT ["./entrypoint.sh"]

FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8505

ENTRYPOINT ["streamlit", "run", "service/app/ui.py", "--server.port=8505", "--server.address=0.0.0.0"]

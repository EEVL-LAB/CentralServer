FROM python:3.8

RUN pip install -r requirements.txt

COPY . /app

CMD uvicorn app:app --host 0.0.0.0 --port 8080
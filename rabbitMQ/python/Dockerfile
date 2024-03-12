FROM python:3.9

WORKDIR /app

RUN pip install pika --upgrade  # Install Pika

COPY send.py ./

CMD ["python", "send.py"]


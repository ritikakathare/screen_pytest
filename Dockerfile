FROM python:latest

WORKDIR /app

COPY screen_time.py . 

CMD ["python", "screen_time.py"]

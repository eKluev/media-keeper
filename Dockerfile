FROM python:3.10

ENV PYTHONUNBUFFERED 1

EXPOSE 7000
WORKDIR /app/

COPY . /app/
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7000"]
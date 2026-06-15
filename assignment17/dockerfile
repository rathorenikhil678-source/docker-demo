FROM python:3.12

RUN apt-get update && \
    apt-get install -y default-jdk

RUN pip install pyspark

WORKDIR /app

COPY . .

CMD ["python", "app.py"]
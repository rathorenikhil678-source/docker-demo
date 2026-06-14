FROM python:3.11

# Install Java
RUN apt-get update && \
    apt-get install -y default-jdk && \
    apt-get clean

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "employee_rdd.py"]
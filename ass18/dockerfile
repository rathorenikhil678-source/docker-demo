FROM python:3.12-slim

# Install Java
RUN apt-get update && \
    apt-get install -y openjdk-21-jdk wget && \
    rm -rf /var/lib/apt/lists/*

# Java Environment
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Spark Download
RUN wget -q https://archive.apache.org/dist/spark/spark-3.5.6/spark-3.5.6-bin-hadoop3.tgz && \
    tar -xzf spark-3.5.6-bin-hadoop3.tgz && \
    mv spark-3.5.6-bin-hadoop3 /opt/spark && \
    rm spark-3.5.6-bin-hadoop3.tgz

# Spark Environment
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

WORKDIR /workspace

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8080", "--no-browser", "--allow-root"]
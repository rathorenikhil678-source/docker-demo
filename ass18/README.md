# Assignment 18 - PySpark Partition Management

## Objective

Create a PySpark application that generates a DataFrame containing 5 million records using `spark.range()`. Display the initial number of partitions, increase the partitions to 12 using `repartition()`, and then reduce the partitions to 3 using `coalesce()`.

---

## Technologies Used

* Python 3.12
* Apache Spark 3.5.6
* PySpark
* Docker
* JupyterLab

---

## Project Structure

```
assignment18/
│
├── Dockerfile
├── requirements.txt
├── Assignment18.ipynb
└── README.md
```

---

## Build Docker Image

```bash
docker build -t assignment18-app .
```

---

## Run Docker Container

```bash
docker run -it --rm -p 8080:8080 -v ${PWD}:/workspace assignment18-app
```

Open Jupyter Lab in your browser:

```
http://localhost:8080
```

---

## PySpark Code

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Assignment18") \
    .getOrCreate()

df = spark.range(5000000)

print("Initial Partitions:", df.rdd.getNumPartitions())

df_repartition = df.repartition(12)
print("Partitions after Repartition:", df_repartition.rdd.getNumPartitions())

df_coalesce = df_repartition.coalesce(3)
print("Partitions after Coalesce:", df_coalesce.rdd.getNumPartitions())

spark.stop()
```

---

## Expected Output

```
Initial Partitions: 2
Partitions after Repartition: 12
Partitions after Coalesce: 3
```

---

## Features

* Generated 5 million records using `spark.range()`
* Checked initial partition count
* Increased partitions using `repartition(12)`
* Reduced partitions using `coalesce(3)`
* Executed inside a Docker container
* Accessed through JupyterLab

---


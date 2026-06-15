# Assignment 17 - PySpark DataFrame Sales Analysis

## Tasks Performed

1. Read CSV into PySpark DataFrame
2. Sort products by sales descending
3. Display top 3 products
4. Filter products with sales > 80000
5. Save filtered data to CSV
6. Dockerized application

## Build Image

```bash
docker build -t sales-analysis-app .
```

## Run Container

```bash
docker run sales-analysis-app
```

## Output



- Sorted products
+----------+------------+-----------+------+
|product_id|product_name|   category| sales|
+----------+------------+-----------+------+
|       101|      Laptop|Electronics|150000|
|       103|          TV|Electronics|120000|
|       102|      Mobile|Electronics| 95000|
|       108|         Bed|  Furniture| 90000|
|       106|        Sofa|  Furniture| 80000|
|       105|       Table|  Furniture| 45000|
|       104|       Chair|  Furniture| 30000|
|       107|  Headphones|Electronics| 25000|
+----------+------------+-----------+------+


Top 3 Products By Sales

+----------+------------+-----------+------+
|product_id|product_name|   category| sales|
+----------+------------+-----------+------+
|       101|      Laptop|Electronics|150000|
|       103|          TV|Electronics|120000|
|       102|      Mobile|Electronics| 95000|
+----------+------------+-----------+------+


Products With Sales > 80000

+----------+------------+-----------+------+
|product_id|product_name|   category| sales|
+----------+------------+-----------+------+
|       101|      Laptop|Electronics|150000|
|       102|      Mobile|Electronics| 95000|
|       103|          TV|Electronics|120000|
|       108|         Bed|  Furniture| 90000|
+----------+------------+-----------+------+

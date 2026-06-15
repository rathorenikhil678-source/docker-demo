from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SalesDataFrame") \
    .getOrCreate()


df = spark.read.csv(
    "sales.csv",
    header=True,
    inferSchema=True
)

print("\nProducts Sorted By Sales\n")

df.orderBy(col("sales").desc()).show()

print("\nTop 3 Products By Sales\n")

df.orderBy(col("sales").desc()) \
  .limit(3) \
  .show()

print("\nProducts With Sales > 80000\n")

high_sales = df.filter(col("sales") > 80000)

high_sales.show()

high_sales.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output/high_sales_products")

spark.stop()
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("EmployeeRDDProcessing") \
    .master("local[*]") \
    .getOrCreate()

sc = spark.sparkContext


rdd = sc.textFile("employee_data.csv")


header = rdd.first()
data_rdd = rdd.filter(lambda row: row != header)


employee_rdd = data_rdd.map(lambda x: x.split(",")) \
    .map(lambda x: (int(x[0]), x[1], x[2], int(x[3])))




print("\nEmployees Sorted by Salary (Descending)")

sorted_salary = employee_rdd.sortBy(lambda x: x[3], ascending=False)

for emp in sorted_salary.collect():
    print(emp)


# 2. Total salary by department

print("\n Department-wise Salary Totals")

dept_salary = employee_rdd.map(lambda x: (x[2], x[3])) \
    .reduceByKey(lambda a, b: a + b)

for dept in dept_salary.collect():
    print(dept)


# 3. Top 3 Highest Paid Employees

top3 = sorted_salary.take(3)

output_lines = [
    f"ID:{emp[0]}, Name:{emp[1]}, Department:{emp[2]}, Salary:{emp[3]}"
    for emp in top3
]

with open("output/top_3_employees.txt", "w") as f:
    for line in output_lines:
        f.write(line + "\n")

print("\nTop 3 employees saved to output/top_3_employees.txt")

spark.stop()
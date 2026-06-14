# Employee  RDD Assignment

## Requirements

- Docker
- Git

## Build Docker Image

```bash
docker build -t employee-rdd-app .
```

## Run Container

```bash
docker run --rm employee-rdd-app
```

## Project Features

- Read employee CSV using Spark RDD
- Sort employees by salary descending
- Calculate department-wise salary totals
- Save top 3 highest-paid employees to file

## Output
=== Employees Sorted By Salary (Descending) ===

['4', 'Priya', 'Finance', '70000']
['3', 'Neha', 'IT', '65000']
['7', 'Rohit', 'Finance', '60000']
['1', 'Amit', 'IT', '55000']
['5', 'Karan', 'IT', '50000']
['6', 'Simran', 'HR', '45000']
['2', 'Rahul', 'HR', '40000']

 Department Salary Totals

IT: 170000
HR: 85000
Finance: 130000

Top 3 employees saved to output/top_3_highest_paid.txt
Console:
- Sorted employees
- Department salary totals

File:
- output/top_3_highest_paid.txt
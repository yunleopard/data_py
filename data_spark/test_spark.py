'''
Created on Nov 12, 2018

@author: yangzh
'''
from pyspark.sql import SparkSession
spark = SparkSession\
        .builder\
        .getOrCreate()
 
#sc = spark.sparkContext
#myRdd = sc.parallelize([1,2,3,4])
#print(myRdd.take(5))

Employee = spark.createDataFrame([
                        ('1', 'Joe',   '70000', '1'),
                        ('2', 'Henry', '80000', '2'),
                        ('3', 'Sam',   '60000', '2'),
                        ('4', 'Max',   '90000', '1')],
                        ['Id', 'Name', 'Sallary','DepartmentId']
                       )

Employee.show(5)
Employee.printSchema()
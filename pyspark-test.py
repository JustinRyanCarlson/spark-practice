from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = (SparkConf()
    .setMaster("local")
    .setAppName("My app")
    .set("spark.executor.memory", "1g"))

sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

df = sqlContext.read.load('./test.csv',
    format='com.databricks.spark.csv',
    header= 'true',
    inferSchema='true')

df.show()
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

# Spark configuration
conf = (SparkConf()
    .setMaster("local")
    .setAppName("My app")
    .set("spark.executor.memory", "1g"))

# setting Spark contextas the config we set
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

# constructing a dataframe from a CSV
df = sqlContext.read.load('./test.csv',
    # format of the data
    format='com.databricks.spark.csv',
    # means that the csv files contains the header
    header= 'true',
    # telling sqlContext to automatically detect the data type of each column in data frame. 
    # If we do not set inferSchema to be true, all columns will be read as string
    inferSchema='true')

print(type(df))
# show dataframe in the console
df.show()
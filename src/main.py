import sys
from pyspark.sql import SparkSession
import os

if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
if os.path.exists('libs.zip'):
    sys.path.insert(0, "libs.zip")

from logger import Log4j


# --conf "-Dlog4j.configuration=file:log4j.properties -Dlogfile.name=hello-spark -Dspark.yarn.app.container.log.dir=app-logs"


def main():
    spark = SparkSession \
        .builder \
        .master("yarn") \
        .appName("HelloSparkSQL") \
        .getOrCreate()

    logger = Log4j(spark)

    # if len(sys.argv) != 2:
    #    logger.error("Usage: HelloSpark <filename>")
    #    sys.exit(-1)

    surveyDF = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv("./data/sample.csv")

    surveyDF.createOrReplaceTempView("survey_tbl")
    countDF = spark.sql(
        "select Country, count(1) as count from survey_tbl where Age<40 group by Country")

    countDF.show()
    logger.info(countDF.count())


if __name__ == "__main__":
    main()

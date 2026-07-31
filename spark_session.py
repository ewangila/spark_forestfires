from pyspark.sql import SparkSession
from pyspark.sql.functions import mean
from pyspark.sql import functions as F

# Step 1: Initialize SparkSession and load data
spark = SparkSession.builder.master('local').appName('ForestFires').getOrCreate()
spark_df = spark.read.csv('./forestfires.csv', header='true', inferSchema='true')

print("Initial Data Look")
spark_df[['month','day','rain']].show(5)

# Step 2: Aggregations
print("\nAverage Area Burned by Month")
spark_df_months = spark_df.groupBy('month').agg({'area': 'mean'})
for row in spark_df_months.collect():
    print(row)

# Step 3: Boolean Masking
print("\nImpact of Rain on Fire Area")
no_rain = spark_df.filter(spark_df['rain'] == 0.0)
some_rain = spark_df.filter(spark_df['rain'] > 0.0)

print('No rain fire area:')
no_rain.select(mean('area')).show()
print('Some rain fire area:')
some_rain.select(mean('area')).show()

# Step 4: Binning (Optimized using .isin for cleaner syntax)
print("\nAverage Area by Season (Binned)")
df_months_binned = spark_df.withColumn('month',
    F.when(spark_df['month'].isin('jun', 'jul', 'aug'), 'Summer') \
     .when(spark_df['month'].isin('dec', 'jan', 'feb'), 'Winter') \
     .otherwise('Spring/Fall')
)

result = df_months_binned.select('month', 'area').groupBy('month').agg({'area': 'mean'}).distinct()
result.show()

spark.stop()
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

def load(dataset="dbfs:/FileStore/Individual_Project3_Kelly_Tong/"
                "women_stem.csv"):
    spark = SparkSession.builder.appName("Read CSV").getOrCreate()
    # load csv and transform it by inferring schema
    women_stem_df = spark.read.csv(
        dataset, header=True, inferSchema=True
    )

    columns = women_stem_df.columns

    # Calculate mid index
    mid_idx = len(columns) // 2

    # Split columns into two halves
    columns1 = columns[:mid_idx]
    columns2 = columns[mid_idx:]

    # Create two new DataFrames
    women_stem_df1 = women_stem_df.select(*columns1)
    women_stem_df2 = women_stem_df.select(*columns2)

    # add unique IDs to the DataFrames
    women_stem_df1 = women_stem_df1.withColumn(
        "id", monotonically_increasing_id()
    )
    women_stem_df2 = women_stem_df2.withColumn(
        "id", monotonically_increasing_id()
    )

    # transform into a delta lakes table and store it
    women_stem_df1.write.format("delta").mode("overwrite").saveAsTable(
        "women_stem1"
    )
    women_stem_df2.write.format("delta").mode("overwrite").saveAsTable(
        "women_stem2"
    )
    
    num_rows = women_stem_df1.count()
    print(num_rows)
    num_rows2 = women_stem_df2.count()
    print(num_rows2)
    
    return "finished transform and load"

if __name__ == "__main__":
    load()

from pyspark.sql import SparkSession
import matplotlib.pyplot as plt


# sample query
def query_transform():
    """
    Run a predefined SQL query on a Spark DataFrame.

    Returns:
        DataFrame: Result of the SQL query.
    """
    spark = SparkSession.builder.appName("Query").getOrCreate()
    query = (
        "SELECT "
        "w1.Major,"
        "w1.Major_category, "
        "w1.Total, "
        "w2.Men, "
        "w2.Women, "
        "w2.ShareWomen, "
        "w2.Median, "
        "(w2.Men + w2.Women) AS total_menwomen, "
        "COUNT(*) as total_entries "
        "FROM "
        "women_stem1 AS w1 "
        "JOIN "
        "wome_stem2 AS w2 "
        "ON w1.id = w2.id "
        "ORDER BY total_menwomen DESC "
        "LIMIT 10"
    )


    query_result = spark.sql(query)
    return query_result


# sample viz for project
def viz():
    query = query_transform()
    count = query.count()
    if count > 0:
        print(f"Data validation passed. {count} rows available.")
    else:
        print("No data available. Please investigate.")

    # Convert the query_result DataFrame to Pandas for plotting
    query_result_pd = query.toPandas()

    # Bar Plot 
    plt.figure(figsize=(15, 7))
    query_result_pd.plot(x='Major', y=['total_menwomen'], kind='bar')
    plot_title = ('Major vs. Total Men&Women')
    plt.title(plot_title)
    plt.ylabel('Counts')
    plt.xlabel('Major')
    plt.xticks(rotation=45)
    plt.legend(title='Metrics')
    plt.tight_layout()
    plt.show()
    

if __name__ == "__main__":
    query_transform()

from pyspark.sql import DataFrame

def read_table(spark, table_name: str) -> DataFrame:
    return spark.table(table_name)

def write_table(df: DataFrame, table_name: str, mode: str = "overwrite") -> None:
    (
        df.write
        .mode(mode)
        .format('delta')
        .saveAsTable(table_name)
    )
import pyspark.sql.functions as F
from pyspark.sql import DataFrame
from pyspark.sql.types import StringType


def trim_string_columns(df: DataFrame) -> DataFrame:
    for field in df.schema.fields:
        if field.dataType == StringType():
            df = df.withColumn(field.name, F.trim(F.col(field.name)))
    return df

def map_codes_to_labels(df: DataFrame, column: str, mapping: dict, default_value: str = 'N/A') -> DataFrame:
    expr = F.when(F.lit(False), F.lit(None))
    for code, label in mapping.items():
        expr = expr.when(F.upper(F.col(column)) == code, label)
    return df.withColumn(column, expr.otherwise(default_value))

def rename_columns(df: DataFrame, mapping: dict) -> DataFrame:
    for old_name, new_name in mapping.items():
        df = df.withColumnRenamed(old_name, new_name)
    return df
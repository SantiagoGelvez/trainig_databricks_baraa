from pyspark.sql import DataFrame

CATALOG = 'baraa_dev_project'
BRONZE_SCHEMA = 'bronze'
SILVER_SCHEMA = 'silver'
GOLD_SCHEMA = 'gold'

def bronze_table(name: str) -> str:
    return f'{CATALOG}.{BRONZE_SCHEMA}.{name}'

def silver_table(name: str) -> str:
    return f'{CATALOG}.{SILVER_SCHEMA}.{name}'

def gold_table(name: str) -> str:
    return f'{CATALOG}.{GOLD_SCHEMA}.{name}'

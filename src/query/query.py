import pandas as pd
from sqlalchemy import create_engine


def query(connection_string, query, result_csv_file):
    engine = create_engine(connection_string)
    df = pd.read_sql(query, engine)
    df.to_csv(result_csv_file, index=False, encoding="utf-8")



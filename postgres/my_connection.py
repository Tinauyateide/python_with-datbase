# importing my dependencies
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

pg_url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/demo'

engine = create_engine(pg_url, pool_recycle=-1)

print('Engine created successfully')

df = pd.read_csv("my_students.csv")

df.to_sql('my_students', con=engine, index=False)

print("Done"),
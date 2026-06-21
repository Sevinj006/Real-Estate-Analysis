import mysql.connector
import pandas as pd
conn = mysql.connector.connect(
    host="localhost",
    user="root",   
    password="",
    database="realestate"
)
df = pd.read_sql("SELECT * FROM housing", conn)

df["price_per_m2"] = df["price"] / df["area"]

df.to_excel("housing_data.xlsx", index=False)

print(df)
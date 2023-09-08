pip install sqlalchemy
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
 
# Set up a connection to the Databricks SQL Endpoint using SQLAlchemy
# Replace with your own values for the JDBC/ODBC driver and endpoint URL
#engine = sqlalchemy.create_engine("databricks+odbc://<Driver Name>:<Host Name>:<Port Number>?Authentication=<Auth Type>")
 
hostname = "dbc-1e8b3c46-6329.cloud.databricks.com"
token = "dapie406676db10514f02bc4ddc90265239d"
port = 443
db = "hive_metastore.coresignal_data.jobs_cleaned"
http_path = "/sql/1.0/warehouses/9400158928ed9893"

conn_string = (
    "databricks://token:{token}@{host}:{port}/{database}?http_path={http_path}".format(
        token=token,
        host=hostname,
        port=port,
        database=db,
        http_path=http_path,
    )
)

engine = create_engine(conn_string, echo=True)



# Define a function to execute SQL queries and return the results as a Pandas dataframe
def run_query(query):
    with engine.connect() as con:
        rs = con.execute(query)
        df = pd.DataFrame(rs.fetchall(), columns=rs.keys())
    return df
 
# Example query to retrieve data from a Delta table
query = "SELECT * FROM my_delta_table"
 
# Call the function to execute the query and display the results in Streamlit
result_df = run_query(query)
st.dataframe(result_df)

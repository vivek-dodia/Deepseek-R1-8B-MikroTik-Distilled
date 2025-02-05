import duckdb

# Connect to an in-memory DuckDB database
con = duckdb.connect(':memory:')

# Read the Parquet file into a DuckDB table
con.execute("CREATE TABLE forum_data AS SELECT * FROM read_parquet('C:/Users/Vivek/Documents/MikroTik_dis/parquet_data/forum/threads.parquet')")

# View the first few rows
print("First few rows:")
print(con.execute("SELECT * FROM forum_data LIMIT 5").fetchdf())

# Get dataset info
print("\nDataset info:")
print(con.execute("DESCRIBE forum_data").fetchdf())

# Get column names and data types
print("\nColumn names and data types:")
print(con.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'forum_data'").fetchdf())

# Close the connection
con.close()

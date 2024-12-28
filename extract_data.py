import pandas as pd
from sqlalchemy import create_engine

# Load the CSV file into a DataFrame
df = pd.read_csv('sales_data.csv')

# Save the transformed data to a new CSV file
df.to_csv('transformed_sales_data.csv', index=False)
print("\nTransformed data saved to 'transformed_sales_data.csv'")

# Add a 'Profit' column by calculating SalesAmount - CostAmount
df['Profit'] = df['SalesAmount'] - df['CostAmount']

# Show the first few rows of the updated dataset
print("Updated Dataset with Profit:")
# Show the first few rows of the dataset to verify the data
print(df.head())

# Database connection details
db_user = 'root'  # Replace with your MySQL username
db_password = 'admin123'  # Replace with your MySQL password
db_host = 'localhost'  # Default MySQL host
db_port = '3306'  # Default MySQL port
db_name = 'sales_data'  # Replace with your database name

# Create a connection to the MySQL database
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# Load the DataFrame into the MySQL table
table_name = 'sales'  # Replace with your MySQL table name
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

print(f"Data successfully loaded into the table '{table_name}' in the database '{db_name}'.")

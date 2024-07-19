import pandas as pd

# Define the file path
file_path = 'C:\\Users\\Abdul Basit\\Downloads\\dataset.csv'  # Replace with your file path

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame before modification
print("Before modification:")
print(df)

# Ensure 'order_id' column contains only integers
df['order_id'] = pd.to_numeric(df['order_id'], errors='coerce').astype('Int64')

# Drop rows with NaN values in 'order_id'
df = df.dropna(subset=['order_id'])

# Modify the 'order_id' column where values are greater than 500
df.loc[df['order_id'] > 500, 'order_id'] = 500

# Ensure 'product_id' is not 0 and drop rows where it is
df = df[df['product_id'] != 0]

# Ensure 'amount' is not greater than 1500
df.loc[df['amount'] > 1500, 'amount'] = 1500

# Ensure 'status' is not null or None, drop rows where it is
df = df.dropna(subset=['status'])

# Remove duplicate rows
df = df.drop_duplicates()

# Display the DataFrame after modification
print("\nAfter modification:")
print(df)

# Save the modified DataFrame back to a CSV file
df.to_csv('C:\\Users\\Abdul Basit\\Downloads\\modified_dataset.csv', index=False)

print("\nThe modified CSV file has been saved as 'C:\\Users\\Abdul Basit\\Downloads\\modified_dataset.csv'.")

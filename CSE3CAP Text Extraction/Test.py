import pandas as pd
import json

def excel_to_json(excel_file_path, json_file_path):
    # Read data from Excel file
    df = pd.read_excel(excel_file_path)
    
    # Debug: Print DataFrame before filling NaN values
    print("DataFrame before filling NaN values:")
    print(df.head())
    
    # Replace NaN values with 'N/A'
    df = df.fillna('N/A')
    
    # Debug: Print DataFrame after filling NaN values
    print("\nDataFrame after filling NaN values:")
    print(df.head())
    
    # Convert DataFrame to list of dictionaries
    data = df.to_dict(orient='records')
    
    # Write JSON data to file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage:
excel_file_path = 'Main.xlsx'  # Replace 'Main.xlsx' with your Excel file path
json_file_path = 'output.json'  # Replace 'output.json' with the desired JSON file path
excel_to_json(excel_file_path, json_file_path)


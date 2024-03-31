#!/usr/bin/env python3
import botocore.session
import csv
import json  # For converting string list representation to list
import time

region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region)  # low-level client

# DAX Cache (for learning purpose)
import sys
if len(sys.argv) > 1:
    from amazondax import AmazonDaxClient
    dax_cluster_endpoint = sys.argv[1]  # Assuming the DAX endpoint is the first argument
    dynamodb = AmazonDaxClient(session, endpoints=[dax_cluster_endpoint], region_name=region)
    print("DAX in use.")

table_name = "game-skill-version-001"
csv_file_path = "dynamodb_02_add_items_skill_version.csv"  # Update this to the path of your CSV file

# Function to convert string value to correct DynamoDB format
def convert_to_dynamodb_format(val, dtype):
    if dtype == 'N':
        return {'N': str(val)}
    elif dtype == 'S':
        return {'S': str(val)}
    elif dtype == 'SS':
        return {'SS': val}
    else:
        raise ValueError(f"Unsupported DynamoDB data type: {dtype}")

# Open and read the CSV file
start_time = time.time()
item_count = 0
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert CSV row to DynamoDB item format
        item = {
            "name": convert_to_dynamodb_format(row["name"], 'S'),
            "price": convert_to_dynamodb_format(row["price"], 'N'),
            "is_available": convert_to_dynamodb_format(row["is_available"], 'S'),
            "version": convert_to_dynamodb_format(row["version"], 'N')
        }
        
        # Add the item to DynamoDB
        response = dynamodb.put_item(TableName=table_name, Item=item)
        item_count += 1
        print(f"Finished adding item ({row['name']}, {row['price']})")

print(f"Finished adding all {item_count} items from CSV.")
duration = time.time() - start_time
print(f"The script took {duration:.0f} seconds to complete.")


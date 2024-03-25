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

table_name = "game-python-001"
csv_file_path = "dynamodb_05_add_items_1000.csv"  # Update this to the path of your CSV file

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
            "hour": convert_to_dynamodb_format(row["hour"], 'N'),
            "type": convert_to_dynamodb_format(row["type"], 'S'),
            "duration": convert_to_dynamodb_format(row["duration"], 'N'),
            "winner": convert_to_dynamodb_format(row["winner"], 'S'),
            "players": convert_to_dynamodb_format(json.loads(row["players"]), 'SS'),  # Parse the string list
            "is_vip": convert_to_dynamodb_format(row["is_vip"], 'S'),
        }
        
        # Add the item to DynamoDB
        response = dynamodb.put_item(TableName=table_name, Item=item)
        item_count += 1
        print(f"Finished adding item ({row['hour']}, {row['type']})")

print(f"Finished adding all {item_count} items from CSV.")
duration = time.time() - start_time
print(f"The script took {duration:.0f} seconds to complete.")


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

def convert_to_dynamodb_format(val, dtype):
    if dtype == 'N':
        return {'N': str(val)}
    elif dtype == 'S':
        return {'S': str(val)}
    elif dtype == 'SS':
        return {'SS': val}
    else:
        raise ValueError(f"Unsupported DynamoDB data type: {dtype}")

def chunked_list(iterable, size):
    """Return a list of successive n-sized chunks from iterable."""
    chunked = []
    for i in range(0, len(iterable), size):
        chunked.append(iterable[i:i + size])
    return chunked

# Open and read the CSV file
start_time = time.time()
items = []
item_count = 0
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        item = {
            "hour": convert_to_dynamodb_format(row["hour"], 'N'),
            "type": convert_to_dynamodb_format(row["type"], 'S'),
            "duration": convert_to_dynamodb_format(row["duration"], 'N'),
            "winner": convert_to_dynamodb_format(row["winner"], 'S'),
            "players": convert_to_dynamodb_format(json.loads(row["players"]), 'SS'),
            "is_vip": convert_to_dynamodb_format(row["is_vip"], 'S'),
        }
        items.append({'PutRequest': {'Item': item}})

# Split items into chunks of 25 for batch writing
item_batch_size = 25
for chunk in chunked_list(items, item_batch_size):
    response = dynamodb.batch_write_item(RequestItems={table_name: chunk})
    item_count += item_batch_size

print(f"Finished adding all {item_count} items from CSV.")
duration = time.time() - start_time
print(f"The script took {duration:.0f} seconds to complete.")

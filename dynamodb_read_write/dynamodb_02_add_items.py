#!/usr/bin/env python3
import botocore.session

region = 'us-east-2'
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region) # low-level client

table_name = "game-python-001"

# item01
partition_key = '10'
sort_key = 'baseball'
duration = '121'
winner = 'tommy919'
players = ["kkdd303", "tommy919", "yoyodi"]
params = {
    'TableName': table_name,
    'Item': {
        "hour": {'N': partition_key},
        "type": {'S': sort_key},
        "duration": {'N': duration},
        "winner": {'S': winner},
        "players": {'SS': players}, 
    }
}

response = dynamodb.put_item(**params)
print(f"finished adding item ({partition_key}, {sort_key})")

# item02
partition_key = '11'
sort_key = 'poker'
duration = '312'
winner = 'yoyodi'
players = ["harry", "zebie", "yoyodi"]
is_vip = True
params = {
    'TableName': table_name,
    'Item': {
        "hour": {'N': partition_key},
        "type": {'S': sort_key},
        "duration": {'N': duration},
        "winner": {'S': winner},
        "players": {'SS': players},  
        "is_vip": {'BOOL': is_vip},
    }
}

response = dynamodb.put_item(**params)
print(f"finished adding item ({partition_key}, {sort_key})")

# item03 
partition_key = '12'
sort_key = 'tennis'
duration = '70'
winner = 'kkdd303'
players = ["kkdd303", "zebie", "yoyodi"] 
is_vip = False
params = {
    'TableName': table_name,
    'Item': {
        "hour": {'N': partition_key},
        "type": {'S': sort_key},
        "duration": {'N': duration},
        "winner": {'S': winner},
        "players": {'SS': players},  
        "is_vip": {'BOOL': is_vip},
    }
}

response = dynamodb.put_item(**params)
print(f"finished adding item ({partition_key}, {sort_key})")

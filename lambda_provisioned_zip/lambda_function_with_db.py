import sys
import time

is_db_connection_built = False

def lambda_handler(event, context):
    create_database_connection()
    time.sleep(3)  # processing main logic
    return 'Hello from AWS Lambda using Python' + sys.version + '!\n'

def create_database_connection():
    global is_db_connection_built  # Declare the variable as global
    if is_db_connection_built is False:
        print('DB connection is being built')
        time.sleep(5)  # getting db connection
        is_db_connection_built = True
        print('DB connection built')
    else:
        print('DB connection already built')

# static initilization 
print('static initialization starts')
create_database_connection()
print('static initialization ends')

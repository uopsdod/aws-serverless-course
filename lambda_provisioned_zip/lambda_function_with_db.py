import sys
import time

is_db_connection_built = False

def lambda_handler(event, context):
    create_database_connection()
    return 'Hello from AWS Lambda using Python' + sys.version + '!\n'

def create_database_connection():
    global is_db_connection_built  # Declare the variable as global
    if is_db_connection_built is False:
        print('DB connection is being built')
        time.sleep(5)  # Delay for 120 seconds or 2 minutes
        is_db_connection_built = True
        print('DB connection built')
    else:
        print('DB connection already built')

    time.sleep(3)  # Delay for 120 seconds or 2 minutes

# static initilization 
print('static initialization starts')
create_database_connection()
print('static initialization ends')

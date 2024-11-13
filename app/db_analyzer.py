from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import reflection
import os
from getpass import getpass

def upload_and_analyze_db(db_url):
    # Create an engine and connect to the database
    engine = create_engine(db_url)
    connection = engine.connect()

    # Reflect the database schema
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Get schema details
    schema_details = {}
    inspector = reflection.Inspector.from_engine(engine)

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        foreign_keys = inspector.get_foreign_keys(table_name)
        
        schema_details[table_name] = {
            'columns': columns,
            'foreign_keys': foreign_keys
        }

    connection.close()
    return schema_details

def get_db_credentials():

    db_user = os.getenv('DB_USER') or input("Enter database username: ")
    db_password = os.getenv('DB_PASSWORD') or getpass("Enter database password: ")
    db_host = os.getenv('DB_HOST') or input("Enter database host: ")
    db_name = os.getenv('DB_NAME') or input("Enter database name: ")

    return f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"

def get_db_schema():
    db_url = get_db_credentials()
    schema_details = upload_and_analyze_db(db_url)
    print(schema_details)

if __name__ == "__main__":
    print("db_analyzer loaded successfully")

# Example usage:
# db_url = 'mysql+pymysql://username:password@localhost/dbname'
# schema_details = upload_and_analyze_db(db_url)
# print(schema_details)

from src.aws.dynamo.dynamo_client import dynamo
from dotenv import load_dotenv
from os import getenv as env

load_dotenv()

def fetch_hash_on_dynamo(hash):
    try:
        key = {
            "hash": {"S": hash}
        }

        item = dynamo.get_item(TableName=env('dynamo_table'), Key=key)
    except Exception as err:
        return f'error: {str(err)}'
        # raise err

print(fetch_hash_on_dynamo(""))
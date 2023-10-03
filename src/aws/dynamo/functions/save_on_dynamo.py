from src.aws.dynamo.dynamo_client import dynamo
from dotenv import load_dotenv
from os import getenv as env

load_dotenv()

def save_data_on_dynamo(api_return):
    try:
        item = {
            "hash": {"S": api_return["unique_id"]},
            "audio_data": {
                "M": {
                    "received_phrase": {"S": api_return["received_phrase"]},
                    "url_to_audio": {"S": api_return["url_to_audio"]},
                    "created_audio": {"S": api_return["created_audio"]},
                }
            },
        }
        dynamo.put_item(TableName=env("dynamo_table"), Item=item)
    except Exception as err:
        raise err
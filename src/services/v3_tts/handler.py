from src.aws.polly.functions.text_to_speech import get_audio_and_date
from src.aws.s3.functions.save_audio_on_s3 import save_audio_on_s3_and_get_link
from src.aws.dynamo.functions.fetch_on_dynamo import fetch_hash_on_dynamo
from src.aws.dynamo.functions.save_on_dynamo import save_data_on_dynamo
from src.utils.hash_generator import hash_generator
import json

def v3_tts_lambda(event, context):
    try:
        # text = event["phrase"]
        user_post = json.loads(event["body"])

        text = user_post['phrase']

        text_hash = hash_generator(text)

        fetched_item = fetch_hash_on_dynamo(text_hash)

        if 'Item' in fetched_item:
        
            api_return = {
                'received_phrase': fetched_item['Item']['audio_data']['M']['received_phrase']['S'],
                'url_to_audio': fetched_item['Item']['audio_data']['M']['url_to_audio']['S'],
                'created_audio': fetched_item['Item']['audio_data']['M']['created_audio']['S'],
                'unique_id': fetched_item['Item']['hash']['S']
            }

        else:
            audio_file, created_date = get_audio_and_date(text)

            audio_link = save_audio_on_s3_and_get_link(
                key=text_hash, audio_file=audio_file)

            api_return = {
                'received_phrase': text,
                'url_to_audio': audio_link,
                'created_audio': created_date,
                'unique_id': text_hash
            }

            save_data_on_dynamo(api_return)

        return json.dumps(api_return)
        # return api_return
    
    except Exception as err:
        # return f'error: {str(err)}'
        raise err
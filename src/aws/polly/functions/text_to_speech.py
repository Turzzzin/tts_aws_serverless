from src.aws.polly.polly_client import polly
from src.utils.format_date import format_date

def get_audio_and_date(phrase):
    try:
        response = polly.synthesize_speech(
            Engine='neural', 
            Text=phrase, 
            OutputFormat='mp3', 
            VoiceId='Vitoria'
        )
        audio_data = response['AudioStream'].read()

        creation_date = response['ResponseMetadata']['HTTPHeaders']['date']
        creation_date = format_date(creation_date)

        return audio_data, creation_date
    except Exception as err:
        raise err

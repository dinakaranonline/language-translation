import json
from translate import Translator


def lambda_handler(event, context):

    body = json.loads(event['body'])
    text = body['text']
    translated_text=get_prediction(text)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'text': text,
            'translated_text': translated_text
        })
    }


def get_prediction(text):
    source = "en"
    target = "hi"
    translation = translator.translate(source, target, text)
    print(translation)
    #return jsonify({"output":translation})
    return translation
    #return ("output":translation)

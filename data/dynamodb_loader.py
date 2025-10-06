import boto3
import json
import os
from dotenv import load_dotenv

def load_to_db():
    load_dotenv()
    table_name = os.getenv("DB")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    with open('colors.json') as file:
        data = json.load(file)

    for language, info in data.items():
        item = {
            'language': language,
            'colour': info.get('color'),
            'url': info.get('url')
        }
        table.put_item(Item=item)

def retrieve_all():
    load_dotenv()
    table_name = os.getenv("DB")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    data = table.scan()
    return data
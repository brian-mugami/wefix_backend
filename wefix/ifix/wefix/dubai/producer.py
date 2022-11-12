import os

import pika
import json

from dotenv import load_dotenv
load_dotenv(".env", verbose=True)
url=os.environ.get("RABBITMQ")
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)

channel = connection.channel()
connection.process_data_events(10)

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

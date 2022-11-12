import pika
import json

params = pika.URLParameters("amqps://tuykftrq:qjNYSlazuJLTjVjSNN8E_YkBaJ1S6rdf@rat.rmq2.cloudamqp.com/tuykftrq")

connection = pika.BlockingConnection(params)

channel = connection.channel()
connection.process_data_events(10)
def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='wefix', body=json.dumps(body), properties=properties)
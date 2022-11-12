import json
import os
import django
import pika
from dotenv import load_dotenv
load_dotenv(".env", verbose=True)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wefix.settings")
django.setup()
from dubai.models import UserModel, LocationModel

url = os.environ.get("RABBITMQ")
params = pika.URLParameters(url)


connection = pika.BlockingConnection(params)
connection.process_data_events(10)

channel = connection.channel()

channel.queue_declare(queue='wefix')
def callback(ch=None, method=None, properties=None, body=None):
    print("Received in admin")
    data = json.loads((body))
    print(data)

    if properties.content_type == "user created":
        location = LocationModel.objects.get(id=data["location"])
        user = UserModel(usertype=data["usertype"], location=location, first_name = data["first_name"],last_name = data["last_name"],company_name = data["company_name"],
                         password = data["password"],email = data["email"],phone = data["phone"],image = data["image"])
        user.save()
        print ("user created")

channel.basic_consume(queue="wefix", on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()


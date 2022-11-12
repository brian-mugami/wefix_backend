import json
import os

import pika
from dotenv import load_dotenv
from website.models import LocationModel, WorkerTypeModel
from website.db import db
from app import app

load_dotenv(".env", verbose=True)
params = pika.URLParameters(os.environ.get("RABITMQ_URL"))

connection = pika.BlockingConnection(params)
connection.process_data_events(10)

channel = connection.channel()
#queue is associated with the routing key
channel.queue_declare(queue='main')

def callback(ch=None, method=None, properties=None, body=None):
    print("Received in main")
    data = json.loads(body)
    print(data)
    with app.app_context():
        if properties.content_type == "location_created":
            location = LocationModel(id=data["id"], name=data["name"])
            db.session.add(location)
            db.session.commit()
            print("Location created")

        elif properties.content_type == "location deleted":
            location = LocationModel.query.filter_by(name=data["name"]).first()
            db.session.delete(location)
            db.session.commit()

        elif properties.content_type == "location updated":
            location = LocationModel.query.filter_by(name=data["name"]).first()
            location.name = data["name"]
            db.session.commit()

        elif properties.content_type == "worktype created":
            work = WorkerTypeModel(**data)
            db.session.add(work)
            db.session.commit()

        elif properties.content_type == "worktype updated":
            work = WorkerTypeModel.filter_by(name=data["name"]).first()
            work.name = data["name"]
            db.session.commit()

        elif properties.content_type == "location deleted":
            work = WorkerTypeModel.filter_by(name=data["name"]).first()
            db.session.delete(work)
            db.session.commit()

channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()


channel.close()

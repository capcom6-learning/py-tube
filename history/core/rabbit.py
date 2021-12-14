import pika
import json

from core import Configuration
from . import database

def connectAndListen():
    connection = pika.BlockingConnection(pika.URLParameters(Configuration.RABBIT))
    channel = connection.channel()
    channel.exchange_declare(exchange='viewed', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='viewed', queue=queue_name)

    def callback(ch, method, properties, body):
        print(body)
        msg = json.loads(body)
        database.addToHistory(msg['videoPath'])
        ch.basic_ack(method.delivery_tag)

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=False)

    channel.start_consuming()

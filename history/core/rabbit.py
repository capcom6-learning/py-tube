import pika
import json

from . import database

class RabbitClient:
    def __init__(self, url: str):
        self.connection = pika.BlockingConnection(pika.URLParameters(url))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='viewed', exchange_type='fanout')

    def start_consuming(self):
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        self.channel.queue_bind(exchange='viewed', queue=queue_name)

        def callback(ch, method, properties, body):
            print(body)
            msg = json.loads(body)
            database.addToHistory(msg['videoPath'])
            ch.basic_ack(method.delivery_tag)

        self.channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=False)

        self.channel.start_consuming()

    def stop_consuming(self):
        self.channel.stop_consuming()

    def close(self):
        self.connection.close()

# def connectAndListen():
#     connection = pika.BlockingConnection(pika.URLParameters(Configuration.RABBIT))
#     channel = connection.channel()
#     channel.exchange_declare(exchange='viewed', exchange_type='fanout')

#     result = channel.queue_declare(queue='', exclusive=True)
#     queue_name = result.method.queue

#     channel.queue_bind(exchange='viewed', queue=queue_name)

#     def callback(ch, method, properties, body):
#         print(body)
#         msg = json.loads(body)
#         database.addToHistory(msg['videoPath'])
#         ch.basic_ack(method.delivery_tag)

#     channel.basic_consume(
#         queue=queue_name, on_message_callback=callback, auto_ack=False)

#     channel.start_consuming()

#     return connection

# def stopListening(channel):
#     channel.start_consuming()

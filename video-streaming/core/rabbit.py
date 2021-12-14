import pika
from pika import connection

from core import Configuration

connection = None

def makeChannel():
    global connection
    connection = pika.BlockingConnection(pika.URLParameters(Configuration.RABBIT))
    channel = connection.channel()
    channel.exchange_declare(exchange='viewed', exchange_type='fanout')
    return channel

def closeChannel():
    connection.close()

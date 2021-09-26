import pika


def rabbitmq_connection(func):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    def wrapper(*args, **kwargs):
        func(channel, *args, **kwargs)
        connection.close()

    return wrapper

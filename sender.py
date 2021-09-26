from rabbitmq import rabbitmq_connection


@rabbitmq_connection
def publish_message(channel, queue: str, message: str):
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='', routing_key=queue, body=message)


if __name__ == '__main__':
    user_message = input('Message: ')
    publish_message(queue='notifications', message=user_message)

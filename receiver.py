from rabbitmq import rabbitmq_connection


def callback(ch, method, properties, body: bytes):
    print(body.decode())


@rabbitmq_connection
def run_receiver(channel, queue: str):
    channel.queue_declare(queue=queue)
    channel.basic_consume(queue=queue, auto_ack=True, on_message_callback=callback)
    channel.start_consuming()


if __name__ == '__main__':
    run_receiver(queue='notifications')

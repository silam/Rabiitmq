import pika

credentials = pika.PlainCredentials('snow', 'snowpass')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials, socket_timeout=300))
channel = connection.channel()

channel.queue_declare(queue='sample_test', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='sample_test', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

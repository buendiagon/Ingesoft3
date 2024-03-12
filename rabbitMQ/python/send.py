import pika

# Establish connection to RabbitMQ (outside the loop for efficiency)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

# Declare the queue (if it doesn't exist)
channel.queue_declare(queue='hello')

print("Press Ctrl+C to quit")
try:
    while True:
        message = input("Message: ")
        channel.basic_publish(exchange='', routing_key='hello', body=message)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    # Close the connection gracefully
    connection.close()


import pika
import os
import time

# Obtener las credenciales de las variables de entorno
user = os.getenv('RABBITMQ_USER')
password = os.getenv('RABBITMQ_PASS')

connected = False

while not connected:
    try:
        # Conectarse a RabbitMQ con las credenciales proporcionadas por las variables de entorno
        credentials = pika.PlainCredentials(user, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', credentials=credentials))
        connected = True
    except pika.exceptions.AMQPConnectionError:
        print("Conexión rechazada, esperando 5 segundos antes de intentar nuevamente...")
        time.sleep(5)

# Declarar una cola
channel = connection.channel()
channel.queue_declare(queue='test_queue')

# Enviar mensajes a la cola
for i in range(5):  # Enviar 5 mensajes como ejemplo
    message = f'Mensaje {i+1}'
    channel.basic_publish(exchange='', routing_key='test_queue', body=message)
    print("Mensaje enviado:", message)

# Cerrar la conexión
connection.close()

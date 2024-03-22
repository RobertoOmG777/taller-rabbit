FROM python:3.9-slim

# Copiar el script de Python al contenedor
COPY . /app

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar la biblioteca pika
RUN pip install pika

# Configurar las variables de entorno para las credenciales
ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=password

# Ejecutar el script de Python al iniciar el contenedor
CMD ["python", "producer.py"]

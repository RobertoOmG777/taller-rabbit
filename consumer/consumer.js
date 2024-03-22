var amqp = require('amqplib/callback_api');
var connected = false;

function connectToRabbitMQ() {
    amqp.connect('amqp://rabbitmq', function(error0, connection) {
        if (error0) {
            console.log("Conexión rechazada, esperando 5 segundos antes de intentar nuevamente...");
            setTimeout(connectToRabbitMQ, 5000);
            return;
        }
        connected = true;
        console.log("Conexión exitosa a RabbitMQ");
        connection.createChannel(function(error1, channel) {
            if (error1) {
                throw error1;
            }
            var queue = 'test_queue';
            channel.assertQueue(queue, {
                durable: false
            });
            console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", queue);
            channel.consume(queue, function(msg) {
                console.log(" [x] Received %s", msg.content.toString());
            }, {
                noAck: true
            });
        });
    });
}

connectToRabbitMQ();

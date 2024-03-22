FROM node:14-alpine

WORKDIR /consumer

COPY . .

RUN npm install amqplib

CMD ["node", "./consumer.js"]
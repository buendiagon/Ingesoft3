FROM node:20.11-alpine
WORKDIR /app

COPY package.json ./
RUN npm install

COPY receive.js ./

CMD ["node", "receive.js"]


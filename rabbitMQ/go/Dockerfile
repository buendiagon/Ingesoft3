FROM golang:1.19-alpine

WORKDIR /app

RUN go mod init receive

RUN go get github.com/rabbitmq/amqp091-go

COPY receive.go ./

RUN go build -o receive

CMD ["./receive"]


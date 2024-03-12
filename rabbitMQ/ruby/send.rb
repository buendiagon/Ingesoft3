require 'bunny'

connection = Bunny.new(automatically_recover: false, hostname: 'rabbitmq')
connection.start

channel = connection.create_channel
queue = channel.queue('hello')

begin
  loop do
    puts "Message: "
    message = gets.chomp
    channel.default_exchange.publish(message, routing_key: queue.name)
  end
rescue Interrupt => _
  puts "\nExiting..."
ensure
  connection.close
end


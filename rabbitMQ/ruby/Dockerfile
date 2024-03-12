FROM ruby:3.1

WORKDIR /app

RUN gem install bunny --version ">= 2.13.0"

COPY send.rb ./ 

CMD ["ruby", "send.rb"]


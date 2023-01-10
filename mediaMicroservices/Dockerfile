FROM yg397/thrift-microservice-deps:xenial

COPY ./ /media-microservices
RUN cd /media-microservices \
    && mkdir -p build \
    && cd build \
    && cmake .. \
    && make \
    && make install

RUN apt-get update && apt-get install -y \
  lcov \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /media-microservices
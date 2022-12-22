FROM debian:bullseye-slim

RUN apt-get update
RUN apt-get -y install gcc
RUN rm -rf /var/lib/apt/lists/*

COPY hello.c .
RUN gcc -s -Os -o hello hello.c

CMD ["./hello"]

FROM debian:bullseye-slim

RUN apt-get update ; \
    apt-get -y install \
        gcc \
    ; \
    rm -rf /var/lib/apt/lists/*

COPY hello.c .
RUN gcc -s -Os -o hello hello.c

CMD ["./hello"]

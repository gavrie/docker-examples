FROM buildpack-deps:bullseye

COPY hello.c .
RUN gcc -s -Os -o hello hello.c

CMD ["./hello"]

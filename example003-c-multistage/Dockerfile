FROM buildpack-deps:bullseye as build

COPY hello.c .
RUN gcc -s -Os -o hello hello.c

#####################################

FROM debian:bullseye-slim

COPY --from=build hello .

CMD ["./hello"]

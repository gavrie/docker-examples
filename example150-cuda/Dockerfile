FROM nvidia/cuda:11.2.0-devel-ubuntu20.04 as builder

RUN set -eux; \
        apt-get update; \
        DEBIAN_FRONTEND=noninteractive \
            apt-get install -yq --no-install-recommends \
                curl \
                cmake \
                libx11-dev \
                libtiff-dev \
                libboost-all-dev \
                libexplain-dev \
                libsystemd-dev \
        ; \
        rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY . .

ENV CUDA_HOME /usr/local/cuda
ENV PATH $CUDA_HOME/bin:$PATH

RUN mkdir build \
        && cd build \
        && cmake .. \
        && cmake --build .

###################

FROM nvidia/cuda:11.2.0-base-ubuntu20.04 as runtime

RUN set -eux; \
        apt-get update; \
        DEBIAN_FRONTEND=noninteractive \
            apt-get install -yq --no-install-recommends \
                libboost-program-options1.71.0 \
                libboost-filesystem1.71.0 \
                libboost-thread1.71.0 \
                libboost-log1.71.0 \
        ; \
        rm -rf /var/lib/apt/lists/*

RUN useradd ubuntu -d /home/ubuntu -u 1000 -m

COPY --from=builder /src/build/hello /usr/local/bin

USER ubuntu

WORKDIR /home/ubuntu

CMD ["hello"]
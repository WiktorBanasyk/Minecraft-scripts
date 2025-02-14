FROM openjdk:8-jdk-slim

RUN apt-get update && apt-get install -y \
    git \
    maven \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY . /workspace

CMD ["mvn", "clean", "install"]

FROM ubuntu:17.10

RUN apt-get -y update && \
    apt-get install -y git make clang libboost-program-options-dev zlib1g-dev openjdk-8-jdk && \
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 && \
    export PATH=$PATH:/usr/lib/jvm/java-8-openjdk-amd64/bin && \
    git clone https://github.com/JohnLangford/vowpal_wabbit.git && \
    cd vowpal_wabbit/ && \
    make && make install

CMD ["vw", "--version"]

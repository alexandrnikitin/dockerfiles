FROM centos:7

RUN yum -y update && \
    yum -y install git make cmake libtool zlib-devel which && \
    yum -y install boost boost-devel && \
    yum -y install java-1.8.0-openjdk-devel && \
    export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk && \
    yum -y install clang gcc-c++ && \
    git clone https://github.com/JohnLangford/vowpal_wabbit.git && \
    cd vowpal_wabbit/ && \
    make && make install

CMD ["vw", "--version"]

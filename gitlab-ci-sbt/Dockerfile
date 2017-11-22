FROM centos:7

ENV JAVA_VERSION 8u151
ENV JAVA_BUILD b12
ENV JAVA_UUID e758a0de34e24606bca991d704f6dcbf
ENV JAVA_INSTALL_DIR jdk1.8.0_151
ENV SBT_VERSION 0.13.16

# System
RUN yum upgrade -y && yum update -y && yum clean all && \
    yum -y install wget git


# Java
RUN wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    "http://download.oracle.com/otn-pub/java/jdk/$JAVA_VERSION-$JAVA_BUILD/$JAVA_UUID/jdk-$JAVA_VERSION-linux-x64.rpm" \
    -O /tmp/jdk-8-linux-x64.rpm && \
    yum -y install "/tmp/jdk-8-linux-x64.rpm" && \
    rm "/tmp/jdk-8-linux-x64.rpm"

ENV JAVA_HOME /usr/java/$JAVA_INSTALL_DIR


# SBT
RUN curl https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-sbt-rpm.repo && \
    yum install bc sbt-$SBT_VERSION -y

ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

# Ansible
RUN yum install -y epel-release && yum update -y && yum install ansible -y

# SSH keys
RUN yum install -y openssh-clients
RUN mkdir -p /root/.ssh
COPY id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa

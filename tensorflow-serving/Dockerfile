FROM ubuntu:16.04

RUN apt-get -y update && \

    apt-get install -y curl && \
    echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && \
    curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add - && \
    
    apt-get -y update && \
    apt-get install -y tensorflow-model-server

CMD ["/bin/bash"]

# Pull base image.
FROM ubuntu:18.04

# Install.
RUN apt update && \
  apt-get install -y make && \
  apt-get install -y g++

COPY . /root/tp2/

# Set environment variables.
ENV HOME /root
ENV PATH="/root/tp2/bin/:${PATH}"

# Define working directory.
WORKDIR /root/tp2/questoes/

# Build
RUN make -C ../
RUN make -C ../ clean 

# Define default command.
CMD clear && bash
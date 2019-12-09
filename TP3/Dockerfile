
# Pull postgres image
FROM postgres:latest

# # Part 1 ==============================

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install -y unzip && \
    apt-get install -y gcc && \
    apt-get install -y nano && \
    apt-get install -y make

# # Part 2 ==============================

RUN mkdir /tpch-tool && \
    cd /tpch-tool && \
    wget http://200.129.163.221/tpch/tpc-h-tool.zip && \
    unzip tpc-h-tool.zip && \
    mv 2.18.0_rc2/ tpch && \
    rm tpc-h-tool.zip && \
    export PATH=$PATH:/tpch-tool/tpch/dbgen/ && \
    cd tpch/dbgen/ && \
    wget http://200.129.163.221/tpch/Makefile && \
    wget http://200.129.163.221/tpch/execute-queries.sh && \
    chmod +x execute-queries.sh

# # Part 3 ==============================

COPY helper/psql_script.sc /home/

ENV PATH=$PATH:/tpch-tool/tpch/dbgen/

RUN cd /tpch-tool/tpch/dbgen/ && \
    make && \
    dbgen -s 1 && \
    mkdir csv

COPY helper/for.sh /home/
RUN /home/for.sh

RUN cd /tpch-tool/tpch/dbgen/ && \
    mv *.csv csv/ && \
    mkdir sql && \
    cd /tpch-tool/tpch/dbgen/sql/ && \
    wget http://200.129.163.221/tpch/tpch-build.sql && \
    wget http://200.129.163.221/tpch/tpch-postgres-create-index.sql

COPY ./setup.sh /home

WORKDIR /home
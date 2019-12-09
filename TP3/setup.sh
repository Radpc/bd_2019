#!/bin/bash

cat /home/psql_script.sc | psql -U postgres

cd /tpch-tool/tpch/dbgen/sql
wget http://200.129.163.221/tpch/tpch-sql-postgres.zip
unzip tpch-sql-postgres.zip
rm tpch-sql-postgres.zip
rm /home/psql_script.sc
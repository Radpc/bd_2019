create database tpch;
\c tpch;
\i /tpch-tool/tpch/dbgen/sql/tpch-build.sql
\i /tpch-tool/tpch/dbgen/sql/tpch-postgres-create-index.sql
\d+ 
\q
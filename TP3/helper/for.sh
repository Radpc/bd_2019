#!/bin/bash

for i in `ls /tpch-tool/tpch/dbgen/*.tbl`; do sed 's/|$//' $i > ${i/tbl/csv}; echo $i; done
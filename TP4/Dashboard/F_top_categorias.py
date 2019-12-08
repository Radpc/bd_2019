#!/usr/bin/env python3

import sys
import psycopg2

# First argument is SV_ADDRESS
# Second argument is SV_USER
# Third argument is SV_PASSWORD
# Fourth argument is BD_NAME

# Check if there is 4 args
if (len(sys.argv) == 1):
    try:
        with open('../default_postgres.txt', 'r') as f:
            ls = f.readlines()
            SV_ADDRESS = ls[0].split()[1]
            SV_USER = ls[1].split()[1]
            SV_PASSWORD = ls[2].split()[1]
            BD_NAME = ls[3].split()[1]
            busca = ls[5].split()[1].lower()
    except:
        print("Invalid arguments!")
        exit()
elif (len(sys.argv) == 2):
    try:
        with open('../default_postgres.txt', 'r') as f:
            ls = f.readlines()
            SV_ADDRESS = ls[0].split()[1]
            SV_USER = ls[1].split()[1]
            SV_PASSWORD = ls[2].split()[1]
            BD_NAME = ls[3].split()[1]
            busca = sys.argv[1]
    except:
        print("Invalid arguments!")
        exit()

else:
    SV_ADDRESS, SV_USER, SV_PASSWORD, BD_NAME, busca = sys.argv[1:]

try:
    con = psycopg2.connect(host=SV_ADDRESS, database=BD_NAME,
                           user=SV_USER, password=SV_PASSWORD)
except:
    print("Connection could not been made!")
    exit()

cur = con.cursor()

sql = "SELECT categoria, AVG(aval) FROM categorizacao JOIN produto ON categorizacao.asin_produto \
     = asin JOIN review ON review.asin_produto = asin WHERE \
     util > 30 GROUP BY categorizacao.categoria ORDER BY AVG(aval) DESC, AVG(rank) LIMIT 10 ;"

cur.execute(sql)

results = cur.fetchall()

if len(results) == 0:
    print("No results found :(")
    exit()

print("Resultados para o TOP 10 CATEGORIAS \n")

for result in results:
    print("[" + str(result[1])[:3] + "] - " + result[0])


con.close()

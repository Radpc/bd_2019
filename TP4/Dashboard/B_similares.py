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
            busca = ls[4].split()[1]
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
            busca = sys.argv[1].lower()
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

if (len(busca) == 10):
    sql = "SELECT asin,rank FROM produto WHERE asin ='" + \
        busca + "' OR lower(nome) LIKE '%" + busca + "%';"
else:
    sql = "SELECT asin,rank FROM produto WHERE lower(nome) LIKE '%" + \
        busca + "%';"

cur.execute(sql)

results = cur.fetchall()

if len(results) == 0:
    print("No results found :(")
    exit()

# Checar similares

asin = results[0][0]
salesrank = results[0][1]

sql = "SELECT asin_similar FROM similares WHERE asin_produto = '" + asin + "';"
cur.execute(sql)

results = cur.fetchall()

counter = 0

for result in results:
    sql = "SELECT asin,rank,nome FROM produto WHERE asin ='" + \
        result[0] + "';"
    cur.execute(sql)
    res = cur.fetchall()

    if (len(res) != 0):
        req = res[0]
        if (int(req[1]) < salesrank):
            print("[" + req[0] + "] - " + str(req[2]) +
                  " , " + str(req[1]) + "º lugar")
            counter += 1

if (counter == 0):
    print("None found..")
else:
    print("\n" + str(counter) + " result(s) with better salesrank!")

con.close()

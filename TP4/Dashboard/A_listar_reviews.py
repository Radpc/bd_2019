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
    sql = "SELECT asin,nome FROM produto WHERE asin ='" + \
        busca + "' OR lower(nome) LIKE '%" + busca + "%';"
else:
    sql = "SELECT asin,nome FROM produto WHERE lower(nome) LIKE '%" + \
        busca + "%';"

cur.execute(sql)

results = cur.fetchall()

if len(results) == 0:
    print("No results found :(")
    exit()

# Checar reviews

asin = results[0][0]
nome = results[0][1]


# Checar review uteis e boas
print("Avaliacoes mais uteis e positivas de [" + nome + "]")
print("-------------------------------------------")

sql = "SELECT * FROM review WHERE asin_produto = '" + \
    asin + "' ORDER BY util DESC, aval DESC;"
cur.execute(sql)
reviews = cur.fetchall()

if (len(reviews) < 5):
    j = len(reviews)
else:
    j = 5

for i in range(0, j):
    print("Usuario: " + reviews[i][1] + " - Util=" +
          str(reviews[i][5]) + " , Aval=" + str(reviews[i][3]))

print("")

# Checar review uteis e ruins
print("Avaliacoes mais uteis e negativas de [" + nome + "]")
print("-------------------------------------------")

sql = "SELECT * FROM review WHERE asin_produto = '" + \
    asin + "' ORDER BY util DESC, aval ASC;"
cur.execute(sql)
reviews = cur.fetchall()

if (len(reviews) < 5):
    j = len(reviews)
else:
    j = 5

for i in range(0, j):
    print("Usuario: " + reviews[i][1] + " - Util=" +
          str(reviews[i][5]) + " , Aval=" + str(reviews[i][3]))

print("")

con.close()

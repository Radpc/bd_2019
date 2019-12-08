#!/usr/bin/env python3

import sys
import psycopg2

# First argument is SV_ADDRESS
# Second argument is SV_USER
# Third argument is SV_PASSWORD
# Fourth argument is BD_NAME

# Check if there is 4 args
if (len(sys.argv) != 5):
    try:
        with open('../default_postgres.txt', 'r') as f:
            ls = f.readlines()
            SV_ADDRESS = ls[0].split()[1]
            SV_USER = ls[1].split()[1]
            SV_PASSWORD = ls[2].split()[1]
            BD_NAME = ls[3].split()[1]
    except:
        print("Invalid arguments!")
        exit()
else:
    SV_ADDRESS, SV_USER, SV_PASSWORD, BD_NAME = sys.argv[1:]


try:
    con = psycopg2.connect(host=SV_ADDRESS, database=BD_NAME,
                           user=SV_USER, password=SV_PASSWORD)
except:
    print("Connection could not been made!")
    exit()

cur = con.cursor()

schemas = ['produto',
           'similares',
           'categorizacao',
           'review']

for name in schemas:
    try:
        cur.execute('DROP TABLE ' + name + ' cascade')
        con.commit()
    except:
        print("Failed in dropping " + name +
              "'s schema. Does it really exist?")
        exit()

print("Dropped tables successfully!")
con.close()

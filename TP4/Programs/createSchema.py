import sys
import psycopg2

# First argument is SV_ADDRESS
# Second argument is SV_USER
# Third argument is SV_PASSWORD
# Fourth argument is BD_NAME

filename = "schema.sql"

# Check if there is 4 args
if (len(sys.argv) != 5):
    print("Invalid arguments!")
    exit()

SV_ADDRESS, SV_USER, SV_PASSWORD, BD_NAME = sys.argv[1:]


try:
    con = psycopg2.connect(host=SV_ADDRESS, database=BD_NAME,
                           user=SV_USER, password=SV_PASSWORD)
except:
    print("Connection could not been made!")
    exit()


cur = con.cursor()

sql = open("schemas/schema.sql").read()
cur.execute(sql)
con.commit()
# cur.execute('select * from cidade;')
# recset = cur.fetchall()
# for rec in recset:
#     print(rec)
con.close()

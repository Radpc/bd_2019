import sys
import psycopg2

# First argument is SV_ADDRESS
# Second argument is SV_USER
# Third argument is SV_PASSWORD
# Fourth argument is BD_NAME

schemas = ['produto',
           'similares',
           'categoria',
           'review']

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

for name in schemas:
    with open("schemas/schema_" + name + ".sql") as file:
        sql = file.read()
    try:
        cur.execute(sql)
        con.commit()
    except:
        print("error in " + name + "'s schema :(")

con.close()

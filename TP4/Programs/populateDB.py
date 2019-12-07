import sys
import psycopg2

# First argument is SV_ADDRESS
# Second argument is SV_USER
# Third argument is SV_PASSWORD
# Fourth argument is BD_NAME

# schemas = ['produto',
#            'cliente',
#            'similares',
#            'categoria',
#            'review']

# # Check if there is 4 args
# if (len(sys.argv) != 5):
#     print("Invalid arguments!")
#     exit()

# SV_ADDRESS, SV_USER, SV_PASSWORD, BD_NAME = sys.argv[1:]

# try:
#     con = psycopg2.connect(host=SV_ADDRESS, database=BD_NAME,
#                            user=SV_USER, password=SV_PASSWORD)
# except:
#     print("Connection could not been made!")
#     exit()


# cur = con.cursor()

# STATUS

def checkId(line):
    if line[:3] == 'Id:':
        return line.split()[1].strip()
    else:
        return False


def checkAsin(line):
    if line[:5] == 'ASIN:':
        return line.split()[1].strip()
    else:
        return False


def checkTitle(line):
    if line[:8] == '  title:':
        return line[9:]
    else:
        return False


def checkGroup(line):
    if line[:8] == '  group:':
        return line[9:]
    else:
        return False


def checkSalesrank(line):
    if line[:12] == '  salesrank:':
        return line.split()[1].strip()
    else:
        return False
    pass


def checkSimilar(line):
    pass


def checkCategories(line):
    pass


def checkReview(line):
    pass


functions = {'id': checkId,
             'asin': checkAsin,
             'title': checkTitle,
             'group': checkGroup,
             'salesrank': checkSalesrank,
             'similar': checkSimilar,
             'categories': checkCategories,
             'reviews': checkReview}

order = ['id', 'asin', 'title', 'group',
         'salesrank', 'similar', 'categories', 'reviews']

n = 0

with open('../test_file.txt', 'r') as file:
    for line in file:
        check_for = functions[order[n]]
        if check_for(line):
            if n < len(order):
                n += 1
            else:
                n = 0
        else:
            n = 0

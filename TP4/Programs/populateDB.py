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

product = {
    # 'id': '',
    'asin': '',
    'title': '',
    'group': '',
    'salesrank': ''
}

similars = []
similar_f = open('similars.txt', 'w')


def generateSQLProduct(product):
    return 'INSERT INTO produto VALUES (\'' + product['asin'] + '\',\'' + product['title'] + \
        '\',\'' + product['group'] + '\',' + product['salesrank'] + ');'


# ---------------------------------------------------------------------------


def checkId(line):
    if line[:3] == 'Id:':
        # product['id'] = line.split()[1].strip()
        return True
    else:
        return False


def checkAsin(line):
    if line[:5] == 'ASIN:':
        product['asin'] = line.split()[1].strip()
        return True
    else:
        return False


def checkTitle(line):
    if line[:8] == '  title:':
        product['title'] = line[9:-1]
        return True
    else:
        return False


def checkGroup(line):
    if line[:8] == '  group:':
        product['group'] = line[9:-1]
        return True
    else:
        return False


# FINAL
def checkSalesrank(line):
    if line[:12] == '  salesrank:':
        product['salesrank'] = line.split()[1].strip()
        sql = generateSQLProduct(product)
        print(sql)
        return True
    else:
        return False
# ---------------------------------------------------------------------------


def checkSimilar(line):
    if line[:10] == '  similar:':
        similars = line.strip().split()[2:]

        if similars != []:
            similar_f.write(product['asin'])
            for s in similars:
                similar_f.write(" " + s)
            similar_f.write("\n")
        return True
    else:
        return False

    pass

# ---------------------------------------------------------------------------


def checkCategories(line):
    pass

# ---------------------------------------------------------------------------


def checkReview(line):
    pass

# ---------------------------------------------------------------------------


functions = {  # 'id': checkId,
    'asin': checkAsin,
    'title': checkTitle,
    'group': checkGroup,
    'salesrank': checkSalesrank,
    'similar': checkSimilar,
    'categories': checkCategories,
    'reviews': checkReview}

order = [  # 'id',
    'asin', 'title', 'group',
    'salesrank', 'similar', 'categories', 'reviews']

n = 0


with open('../test_file.txt', 'r') as file:
    for line in file:

        # PRODUCT
        if n < 4:
            if functions[order[n]](line):
                n += 1
            else:
                n = 0

        # SIMILARS
        elif n == 4:
            if functions[order[n]](line):
                n = 0
            else:
                n = 0

        # CATEGORIES
        elif n == 5:
            pass

        # REVIEWS
        elif n == 6:
            pass


similar_f.close()

#!/usr/bin/env python3

import sys
import psycopg2

filename = 'amazon-meta.txt'

# First argument is SV_ADDRESS
# Second argument is SV_USER
# Third argument is SV_PASSWORD
# Fourth argument is BD_NAME

# # Check if there is 4 args
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

product = {
    # 'id': '',
    'asin': '',
    'title': '',
    'group': '',
    'salesrank': ''
}

category_lines = -1
categories = []
review_lines = -1


def generateSQLProduct(product):
    if "'" in product['title']:
        product['title'] = product['title'].replace("'", "''")

    if "'" in product['group']:
        product['group'] = product['group'].replace("'", "''")

    sql = 'INSERT INTO Produto VALUES (\'' + product['asin'] + '\',\'' + product['title'] + \
        '\',\'' + product['group'] + '\',' + product['salesrank'] + ');'
    cur.execute(sql)


def generateSimilaresSQL(similares):
    for s in similares:
        sql = 'INSERT INTO Similares VALUES (\'' + \
            product['asin'] + '\',\'' + s + '\');'
        cur.execute(sql)


def generateCategoriesSQL(categories):
    for s in categories:
        if "'" in s:
            s = s.replace("'", "''")
        sql = 'INSERT INTO Categorizacao VALUES(\'' + \
            product['asin'] + '\',\'' + s + '\');'
        cur.execute(sql)


def generateReview(review):

    sp = review.split()
    sql = 'INSERT INTO Review VALUES (\'' + \
        product['asin'] + '\',\'' + sp[2] + '\',\'' + sp[0] + \
        '\',' + sp[4] + ',' + sp[6] + ',' + sp[8] + ');'

    cur.execute(sql)


# ---------------------------------------------------------------------------


# def checkId(line):
#     if line[:3] == 'Id:':
#         # product['id'] = line.split()[1].strip()
#         return 1
#     else:
#         return 0


def checkAsin(line):
    if line[:5] == 'ASIN:':
        product['asin'] = line.split()[1].strip()
        return 1
    else:
        return 0


def checkTitle(line):
    if line[:8] == '  title:':
        product['title'] = line[9:-1]
        return 1
    else:
        return -1


def checkGroup(line):
    if line[:8] == '  group:':
        product['group'] = line[9:-1]
        return 1
    else:
        return -2


# FINAL
def checkSalesrank(line):
    if line[:12] == '  salesrank:':
        product['salesrank'] = line.split()[1].strip()
        generateSQLProduct(product)
        return 1
    else:
        return -3
# ---------------------------------------------------------------------------


def checkSimilar(line):
    if line[:10] == '  similar:':
        similars = line.strip().split()[2:]

        if similars != []:
            generateSimilaresSQL(similars)
        return 1
    else:
        return -4

# ---------------------------------------------------------------------------


def checkCategories(line):
    global category_lines
    global categories
    if (category_lines > 0):
        for s in line.strip().split('|')[1:]:
            if s not in categories:
                categories.append(s)

        if (category_lines == 1):
            generateCategoriesSQL(categories)
            con.commit()
            categories = []
            category_lines = -1
            return 1
        else:
            category_lines -= 1
            return 0
    else:
        if (line[:13] == "  categories:"):
            category_lines = int(line.strip().split()[1])
            return 0
        else:
            categories = []
            category_lines = -1
            return -5


# ---------------------------------------------------------------------------


def checkReview(line):
    global review_lines

    if (review_lines > 0):
        generateReview(line.strip())
        if (review_lines == 1):
            review_lines = -1
            return -6
        else:
            review_lines -= 1
            return 0
    else:
        if (line[:10] == "  reviews:"):
            review_lines = int(line.strip().split()[4])
            return 0
        else:
            review_lines = -1
            return -6

    print("--------")
    return -6

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
l_number = 0

with open('../' + filename, 'r') as file:
    for line in file:
        n += functions[order[n]](line)
        l_number += 1
        if (l_number % 10000 == 0):
            print("Line " + str(l_number))

con.close()

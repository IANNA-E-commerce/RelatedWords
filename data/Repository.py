import array
import csv
import os

import mysql.connector
import numpy

from scripts.TreatData import TreatData

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bd_weg'
)

# Criar um cursor
cursor = conn.cursor()

# Executar uma consulta SQL
cursor.execute('SELECT name, id FROM product')

# Buscar os resultados
products = cursor.fetchall()
print("products 1 - ", products)
# products = TreatData.refactoring_data_db(products)
# print(products)

# path = os.path.join('../dict', 'data_db.csv')
#
# with open(path, 'w', newline='') as archive_csv:
#     writer_csv = csv.writer(archive_csv)
#     writer_csv.writerow(["Id", "Product"])
#     writer_csv.writerows(products)

# Fechar a conexão
conn.close()
cursor.close()

import csv
import os

import mysql.connector

from scripts.TreatData import TreatData

class Repository:

    # Connection to DB
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='bd_weg'
    )

    def find_name_id_products():
        cursor = Repository.conn.cursor()

        cursor.execute('SELECT name, id FROM product')

        products = cursor.fetchall()
        products = TreatData.refactoring_data_db(products)

        path = os.path.join('../dict', 'data_db.csv')

        with open(path, 'w', newline='') as archive_csv:
            writer_csv = csv.writer(archive_csv)
            writer_csv.writerow(["Id", "Product"])
            writer_csv.writerows(products)

        Repository.conn.close()
        cursor.close()

    def return_product(id):
        cursor = Repository.conn.cursor()

        cursor.execute("SELECT * FROM product WHERE id = %s", (id,))

        product = cursor.fetchall()

        Repository.conn.close()
        cursor.close()
        return product

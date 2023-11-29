import time

import pymysql

class Controller:

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='bd_weg')

    def monitor_update_queue():
        try:
            with Controller.connection.cursor() as cursor:
                while True:
                    cursor.execute("SELECT * FROM log_update LIMIT 1")
                    result = cursor.fetchone()

                    if result:
                        data = {
                            'product_id': result[1],
                            'product_name': result[2],
                            'operation': result[3]
                        }

                        cursor.execute(f"DELETE FROM log_update WHERE id = {result[0]}")
                    else:
                        time.sleep(1)
        finally:
            connection.close()

    if __name__ == '__main__':
        monitor_update_queue()

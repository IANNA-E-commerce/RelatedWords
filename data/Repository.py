import mysql.connector
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
cursor.execute('SELECT p.name, c.name FROM product as p, category as c where p.category_id = c.id')

# Buscar os resultados
products = cursor.fetchall()
TreatData.refactoring_data_bd(products)

# Fechar a conexão
conn.close()
cursor.close()

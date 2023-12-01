# import time
# import mysql.connector
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from scripts.SpellingChecker import SpellingChecker
# from scripts.SuggestProducts import SuggestProducts
#
# class Controller:
#
#     app = Flask(__name__)
#     CORS(app)
#
#     # @staticmethod
#     # def monitor_update_queue():
#     #     try:
#     #         with Controller.conn.cursor() as cursor:
#     #             while True:
#     #                 cursor.execute("SELECT * FROM log_update LIMIT 1")
#     #                 result = cursor.fetchone()
#     #
#     #                 if result:
#     #                     data = {
#     #                         'product_id': result[1],
#     #                         'product_name': result[2],
#     #                         'operation': result[3]
#     #                     }
#     #
#     #                     cursor.execute(f"DELETE FROM log_update WHERE id = {result[0]}")
#     #                 else:
#     #                     time.sleep(1)
#     #     finally:
#     #         Controller.conn.close()
#
#     @staticmethod
#     @app.route('/related_words', methods=['GET'])
#     def related_words():
#         phrase = request.args.get('input')
#         lang = request.args.get('language')
#
#         input_info = [phrase, lang]
#         print("input_info: ", input_info)
#
#         phrase_treated = SpellingChecker.custom_spell_check(input_info)
#         print("phrase_treated: ", phrase_treated)
#
#         products = SuggestProducts.main([phrase_treated, input_info[1]])
#         print("products: ", products)
#
#         # Criar o JSON
#         answer = jsonify({'original_phrase': phrase, 'treated_phrase': phrase_treated, 'products': products})
#
#         # Reinicializa as variáveis antes de finalizar a função
#         del input_info, phrase_treated, products
#
#         # Retorna o array como JSON
#         return answer
#
#
# # Configuração da conexão fora da classe
# Controller.conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='bd_weg'
# )
#
# if __name__ == '__main__':
#     # Executa o método para monitorar a fila antes de iniciar o aplicativo Flask
#     # Controller.monitor_update_queue()
#
#     # Executa o aplicativo Flask
#     Controller.app.run(debug=True)

import mysql.connector
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from scripts.SpellingChecker import SpellingChecker
from scripts.SuggestProducts import SuggestProducts

app = Flask(__name__)
CORS(app)

@app.route('/related_words', methods=['GET'])
def related_words():
   conn = mysql.connector.connect(
       host='localhost',
       user='root',
       password='root',
       database='bd_weg'
   )

   try:
       correct = request.args.get('correct')
       phrase = request.args.get('input')
       lang = request.args.get('language')

       input_info = [phrase, lang]
       print("input_info: ", input_info)

       if correct:
           phrase = SpellingChecker.custom_spell_check(input_info)
           print("phrase_treated: ", phrase)

       products = SuggestProducts.main(input_info)
       print("products: ", products)

       answer = jsonify({'original_phrase': request.args.get('input'), 'treated_phrase': phrase, 'products': products})
   finally:
       conn.close()

   return answer

if __name__ == '__main__':
   app.run(debug=True)

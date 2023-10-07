import sqlite3
import logging

# Configurar o sistema de logs
logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def selectNumeroRegistro(numero_registro):
    try:
        with sqlite3.connect('bulario.db') as conn:
            cursor = conn.cursor()

            # Executar a consulta
            cursor.execute("SELECT * FROM medicamentos WHERE numero_registro = ?", (numero_registro,))
            
            # Recuperar o resultado
            result = cursor.fetchone()

            # Verificar se algum registro foi encontrado
            if result:
                return result
            else:
                print("Nenhum registro foi encontrado com o número de registro fornecido.")
    except sqlite3.Error as e:
        error_message = f"Erro ao select do medicamento: {e}"
        logging.error(error_message)

# retorna todos os registros que não tem pdf valido (existe_bula = N)
def selectTodosSemBula():
    try:
        with sqlite3.connect('bulario.db') as conn:
            cursor = conn.cursor()

            # Executar a consulta
            cursor.execute("SELECT numero_registro FROM medicamentos WHERE existe_bula = 'N'")
            
            # Recuperar o resultado
            result = cursor.fetchall()

            # Verificar se algum registro foi encontrado
            if result:
                result = [tupla[0] for tupla in result]
                return result
            else:
                print("Nenhum registro foi encontrado com o número de registro fornecido.")
    except sqlite3.Error as e:
        error_message = f"Erro ao select do medicamento: {e}"
        logging.error(error_message)

# conta todos os registros que não tem pdf valido (existe_bula = N)
def selectQuantidadeRegistros():
    try:
        with sqlite3.connect('bulario.db') as conn:
            cursor = conn.cursor()

            # Executar a consulta
            cursor.execute("SELECT COUNT(id) FROM medicamentos WHERE existe_bula = 'N'")
            
            # Recuperar o resultado
            result = cursor.fetchone()

            # Verificar se algum registro foi encontrado
            if result:
                return result[0]
            else:
                print("Nenhum registro foi encontrado.")
    except sqlite3.Error as e:
        error_message = f"Erro ao select do medicamento: {e}"
        logging.error(error_message)
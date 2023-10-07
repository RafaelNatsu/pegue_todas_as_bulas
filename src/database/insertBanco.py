import sqlite3
import logging

# Configurar o sistema de logs
logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def inserirMedicamento(nome_medicamento, numero_registro, existe_bula):
    try:
        with sqlite3.connect('bulario.db') as conn:
            cursor = conn.cursor()
            nome_medicamento = nome_medicamento.replace(" ", "").lower()
            # Executar o INSERT
            cursor.execute("INSERT INTO medicamentos (nome_medicamento, numero_registro, existe_bula) VALUES (?, ?, ?)", (nome_medicamento, numero_registro, existe_bula))
            conn.commit()
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            # Tratar a exceção de violação de chave única (numero_registro duplicado)
            error_message = f"Nome do medicamento duplicado: {nome_medicamento}(numeroRegistro={numero_registro})"
            logging.error(error_message)
        else:
            # Outro tipo de erro de integridade
            error_message = f"Erro de integridade ao inserir o medicamento: {e}"
            logging.error(error_message)
    except sqlite3.Error as e:
        # Outros erros de banco de dados
        error_message = f"Erro ao inserir o medicamento: {e}"
        logging.error(error_message)

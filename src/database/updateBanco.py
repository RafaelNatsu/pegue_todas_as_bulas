import sqlite3
import logging

# Configurar o sistema de logs
logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def updateMedicamento(numero_registro, existe_bula):
    try:
        with sqlite3.connect('bulario.db') as conn:
            cursor = conn.cursor()
            
            # Executar o UPDATE
            cursor.execute("UPDATE medicamentos SET existe_bula = ? WHERE numero_registro = ?", (existe_bula, numero_registro))
            conn.commit()

            # Verificar se algum registro foi atualizado
            if cursor.rowcount > 0:
                print("Registro atualizado com sucesso.")
            else:
                print("Nenhum registro foi atualizado. Verifique se o ID e o nome correspondem.")
    except sqlite3.Error as e:
        error_message = f"Erro ao update o medicamento: {e}"
        logging.error(error_message)

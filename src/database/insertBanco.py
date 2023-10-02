import sqlite3

def inserirMedicamento(nome_medicamento, id_medicamento, existe_pdf):
    # Conectar ao banco de dados
    conn = sqlite3.connect('bulario.db')
    cursor = conn.cursor()

    # Executar o INSERT
    cursor.execute("INSERT INTO medicamentos (nome_medicamento, id_medicamento, existe_pdf) VALUES (?, ?, ?)",(nome_medicamento, id_medicamento, existe_pdf))
    conn.commit()

    # Fechar conexão com o banco de dados
    cursor.close()
    conn.close()
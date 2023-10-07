import sqlite3

def criarBanco():
    # Conectar ao banco de dados (ou criar se não existir)
    conn = sqlite3.connect('bulario.db')
    cursor = conn.cursor()

    # Verificar se a tabela já existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='medicamentos'")
    tabela_existe = cursor.fetchone()

    # Criar a tabela se não existir
    if not tabela_existe:
        cursor.execute('''CREATE TABLE medicamentos
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nome_medicamento TEXT,
                           numero_registro INTEGER UNIQUE,
                           existe_bula INTEGER)''')
        conn.commit()

    # Fechar conexão com o banco de dados
    cursor.close()
    conn.close()
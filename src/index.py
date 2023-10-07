import threading
import time
import json
import logging
import concurrent.futures
import requests
from bulario.bulario import Bulario
from database.criaBanco import criarBanco
from database.insertBanco import inserirMedicamento

logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# tenta executar a requisição e espera o codigo 200, caso não de, ele tenta novamente 3 vezes
def realizarRequisicao(nomeMedicamento, pagina, quantidade):
    tentativas = 0
    while tentativas < 3:
        try:
            bula = Bulario()
            # Gera url
            urlProximo = bula.pesquisar(nomeMedicamento=nomeMedicamento, quantidade=quantidade, pagina=pagina)
            response = requests.get(urlProximo, headers=bula.getHeader())
            if response.status_code == 200:
                jsonResponseProximo = json.loads(response.text)
                return jsonResponseProximo
            else:
                logging.error(f"Requisição {nomeMedicamento} falhou. Tentando novamente...")
        except Exception as e:
            logging.error(f"Erro ao processar a requisição {nomeMedicamento}: {str(e)}")
        tentativas += 1
        time.sleep(60 * 2)

    logging.error(f"Requisição {nomeMedicamento} falhou após {tentativas} tentativas.")

def insereRemedioBanco(nomeMedicamento, pagina, quantidade):
    resultado = realizarRequisicao(nomeMedicamento, pagina, quantidade)
    count = 0
    # percorre todo os medicamentos da requisição
    for medicamento in resultado.get('content'):
        inserirMedicamento(medicamento['nomeProduto'], medicamento['numeroRegistro'], 'N')
        # faz uma pausa para evitar problemas no sqlite por quantidade de registro por transação.
        if count % 500 == 0:
            time.sleep(0.5)
        count += 1

def main():
    # Verifica se existe o banco
    criarBanco()
    # Faz uma requisição para resgatar a quantidade de paginas e alguns medicamentos
    jsonResponse = realizarRequisicao("", pagina=1, quantidade=1000)
    quantidadeTotalDePaginas = jsonResponse.get('totalPages')
    tamanhoGrupo = 4

    # processa de 4 em 4
    with concurrent.futures.ThreadPoolExecutor(max_workers=tamanhoGrupo) as executor:
        for i in range(1, quantidadeTotalDePaginas + 1, tamanhoGrupo):
            grupoThreads = []
            for j in range(tamanhoGrupo):
                pag = i + j
                if pag <= quantidadeTotalDePaginas:
                    t = executor.submit(insereRemedioBanco, "", pag, 1000)
                    grupoThreads.append(t)
            for t in grupoThreads:
                t.result()  # Aguarda o término da thread
    print("Todas as requisições foram processadas.")

if __name__ == "__main__":
    main()

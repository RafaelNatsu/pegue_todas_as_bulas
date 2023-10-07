import concurrent.futures
import json
import logging
import requests
import re
import time
from bulario.bulario import Bulario
from utils.salvarPdf import salvarPdf
from database.criaBanco import criarBanco
from database.updateBanco import updateMedicamento
from database.selectBanco import selectTodosSemBula, selectQuantidadeRegistros

logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def criarBancoEIniciar():
    criarBanco()

def realizarRequisicao(idMedicamento):
    tentativas = 0
    while tentativas < 3:
        try:
            bula = Bulario()
            # Constroi a url
            url = bula.pesquisaPorIdMedicamento(idMedicamento)
            resposta = requests.get(url, headers=bula.getHeader())

            # Retorna json
            if resposta.status_code == 200:
                jsonResponseProximo = json.loads(resposta.text)
                jsonResponseProximo = jsonResponseProximo.get('content')[0]
                return jsonResponseProximo
            elif resposta.status_code == 429:
                time.sleep(10)
                return None
            else:
                print(f"Requisição do registro medicamento: {idMedicamento} falhou. Code:{resposta.status_code} Tentando novamente...")
                return None
        except Exception as e:
            logging.error(f"Erro ao processar a requisição do registro medicamento {idMedicamento}: {str(e)}")
        return None
    logging.error(f"Requisição id {idMedicamento} falhou após {tentativas} tentativas.")

def realizarRequisicaoDownload(idBulaPacienteProtegido):
    tentativas = 0
    while tentativas < 3:
        try:
            bula = Bulario()
            # Gera url
            urlProximo = bula.criaUrlPdf(idBulaPacienteProtegido)
            resposta = requests.get(urlProximo, headers=bula.getHeader())
            if resposta.status_code == 200:
                return resposta
            elif resposta.status_code == 429:
                time.sleep(10) # sleep para "aliviar" para o servidor
                return None
            else:
                print(f"Requisição do registro medicamento: {idBulaPacienteProtegido} falhou. Tentando novamente...")
                return None
        except Exception as e:
            print(f"Erro ao processar a requisição do registro medicamento {idBulaPacienteProtegido}: {str(e)}")
            return None
    logging.error(f"Requisição id da bula do paciente {idBulaPacienteProtegido} falhou após {tentativas} tentativas.")

def processarMedicamento(idMedicamento):
    try:
        bula = Bulario()
        registroMedicamento = realizarRequisicao(idMedicamento);
        # verifica se existe algo
        if registroMedicamento is not None:
            pdf = realizarRequisicaoDownload(registroMedicamento.get('idBulaPacienteProtegido'))
            if isinstance(pdf, requests.Response):
                # resgata da requisição o nome e o tipo do documento
                contentDispositionHeader = pdf.headers['Content-Disposition']
                filename = re.findall("filename=(.+)", contentDispositionHeader)
                nomeArquivo = filename[0].strip('"')
                salvarPdf("./pdf/"+nomeArquivo, pdf.content)
                updateMedicamento(idMedicamento, 'S')
            else:
                return {"erro_no_id": idMedicamento}
        else:
            return {"erro_no_id": idMedicamento}
    except Exception as e:
        print(f"Erro ao processar da requisição do registro medicamento {idMedicamento}: {str(e)}")

def main():

    #Verifica caso existe, se não é criado.
    criarBancoEIniciar()

    #resgata do banco todos registro com o existe_bula = 'N'
    registrosMedicamentos = selectTodosSemBula()
    
    tamanhoGrupo = 4
    # inicia o loop do processamento
    with concurrent.futures.ThreadPoolExecutor(max_workers=tamanhoGrupo) as executor:
        for idMedicamento in registrosMedicamentos:
            executor.submit(processarMedicamento, idMedicamento)
        time.sleep(10)

    print("Todas as requisições foram processadas. Execute novamente caso esteja faltando")


if __name__ == "__main__":
    main()

# from database import criaBanco;

# cria banco se não existir
# criaBanco.criar_banco();
# receber o json com todos os medicamentos

# inserir medicamentos no banco
## inserirMedicamento(nome_medicamento, id_medicamento=oqueRecebeNoJson, existe_pdf=false)

# apos inserios todos os remedio
# Deve-se criar uma estrategia para baixar os pdf's
# pesquisa por nome (para receber o ID da bula)
# tenta baixar
# caso de erro
    # pula e deixa registrado no banco existe_pdf como falso
# caso de certo
    # registra no banco existe_pdf como verdadeiro e salva pdf

# preciso verificar a melhor estrategia para baixar
# coisas importantes para lembrar: o id gerado é um token jwt de 5 minutos

# from bulario.bulario import Bulario
# import requests
# import json

# bula = Bulario();
# url = bula.pesquisar(nomeMedicamento='dipirona');

# response = requests.get(url,headers=bula.getHeader());
# jsonResponse = json.loads(response.text)
# # print(jsonResponse.get('content')[0]['idBulaPacienteProtegido']);
# urlPdf = bula.criaUrlPdf(jsonResponse.get('content')[0]['idBulaPacienteProtegido'])
# pdf = requests.get(url=urlPdf)
# # print(pdf.content)

# from utils.salvarPdf import salvarPdf
# salvarPdf('teste2.pdf',pdf.content)

# interação no banco
# from database.criaBanco import criarBanco
# from database.insertBanco import inserirMedicamento
# criarBanco();
# inserirMedicamento("nome_medicamento", "id_medicamento", "N")
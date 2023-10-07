import requests
from bulario.utils import randomUserAgent;

class Bulario:
    def __init__(self):
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "authorization": "Guest",
            "cache-control": "no-cache",
            "if-modified-since": "Mon, 26 Jul 1997 05:00:00 GMT",
            "pragma": "no-cache",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "cookie": "FGTServer=77E1DC77AE2F953D7ED796A08A630A01A53CF6FE5FD0E106412591871F9A9BBCFBDEA0AD564FD89D3BDE8278200B; _pk_id.42.210e=8eca716434ce3237.1690380888.; _cfuvid=L.SzxLLxZoWYrYqhaiRgS5MTkV77mwE5uIyLNWvyufk-1690462598410-0-604800000; _pk_ref.42.210e=%5B%22%22%2C%22%22%2C1690462669%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.42.210e=1; cf_clearance=tk5QcLSYPlUQfr8s2bTGXyvC2KZdHcEIYU8r6HCgNvQ-1690462689-0-160.0.0",
            "Referer": "https://consultas.anvisa.gov.br/",
            "UserAgent": randomUserAgent(),
            "Referrer-Policy": "no-referrer-when-downgrade"
        }
        self.params = {
            "totalPages": 0,
            "totalElements": 0,
            "last": False,
            "numberOfElements": 0,
            "first": True,
            "sort": None,
            "size": 0,
            "number": 0
        }
    
    # pesquisa o medicamento por nome, caso vazio retorna todos medicamentos
    def pesquisar(self, nomeMedicamento='', pagina='', quantidade=''):
        __page = pagina;
        __count = quantidade;
        url = f'https://consultas.anvisa.gov.br/api/consulta/bulario?count={__count}&filter%5BnomeProduto%5D={nomeMedicamento}&page={__page}'
        return url

    # cria o a url para baixar o pdf
    def criaUrlPdf(self, idBulaPaciente):
        url = f'https://consultas.anvisa.gov.br/api/consulta/medicamentos/arquivo/bula/parecer/{idBulaPaciente}/?Authorization='
        return url
    
    # retorna url de um medicamento pelo nome
    def pesquisaMedicamento(self, nomeMedicamento):
        url = f"https://consultas.anvisa.gov.br/api/consulta/bulario?count=1&filter%5BnomeProduto%5D={nomeMedicamento}&page=1"
        return url
    
    # retorna url de um medicamento pelo id
    def pesquisaPorIdMedicamento(self, numeroRegistro):
        url = f"https://consultas.anvisa.gov.br/api/consulta/bulario?count=1&filter%5BnumeroRegistro%5D={numeroRegistro}&page=1"
        return url
    
    def setParametros(self,totalDePaginas,totalDeElementos,numeroDeElementosPagina,quantidade,pagina):
        totalDePaginas
        totalDeElementos
        numeroDeElementosPagina
        self.params = {
            "totalPages": totalDePaginas,
            "totalElements": totalDeElementos,
            "last": False if totalDePaginas > pagina else True,
            "numberOfElements": numeroDeElementosPagina,
            "first": True if pagina == 1 else False,
            "size": quantidade,
            "number": pagina
        }
    
    def getHeader(self):
        return self.headers;
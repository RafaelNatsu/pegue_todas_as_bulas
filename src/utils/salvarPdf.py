
import io

def salvarPdf(nomeArquivo, conteudo):
    stream = io.FileIO(nomeArquivo, 'w')
    with stream as arquivo:
        # Escreve dados no arquivo
        arquivo.write(conteudo);

# pegue_todas_as_bulas
 O software irá baixar todas as bulas da anvisa

# Requerimentos
- Python 3.11

# Executando script
Inicialmente execute o seguinte comando para iniciar o processo de criação da base de dados.
```bash
python src/index.py
```
Apos executar o comando, inicie o processo para baixar as bula.
O processo demora bastante, apesar de utilizar threads para deixar em paralelo as requisições. (com uma internet boa demora umas 4h na primeira vez)
Execute o script algumas vezes até conseguir todas as bulas. (não foi implementado o loop para evitar bloqueio de bot)
(mas é uma possibilidade futura de ser implementado uma logica boa para este loop)
```bash
python src/baixarBula.py
```

# "Estratégia"
A estratégia que foi pensada para solucionar o problema principal, que era, a instabilidade do site de consulta das bulas. Foi pensado em fazer da seguinte forma:
- Cortar requisições desnecesárias
- Caso apareça alguma falha, "pula" para o proximo.

Para isso, criei uma classe para construir a url e montar o header necessário para as requisições.
Como existia a possibilidade de em qualquer uma das requisições dar algum erro, pensei em registrar os medicamentos que existem em um banco de dados sqlite. 
O quer iria evitar a duplicidade de bula.
Como tambem foi verificado que existe uma base de dados grande de medicamentos, decidi separar os processos, utilizando as threads.

# Motivos para o script
Conversando com um grande amigo, vi uma possibilidade de me desafiar e ajuda-lo. E por fim o motivo é apenas este hehehehe

Para qualquer pessoa que queria utilizar, fique a vontade, o intuito da criação desta ferramenta é apenas para fins educativos.
Aceito dicas para melhorias!
E peço que utilize de forma conciente (para não sugar os recursos do sistema que é publico)
E SE puder, ajude a comunidade! Somos fortes juntos.

Ass. Rafael Yukio Natsu
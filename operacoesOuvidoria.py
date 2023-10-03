from operacoesbd import *

connection = abrirBancoDados('localhost', 'root', '', 'ouvidoria-facisa')

def listarManifestacoes(manifestacoes):
  sql = "SELECT * FROM manifestacoes"
  listaManifestacoes = listarBancoDados(connection, sql)
  
  for i in range(len(listaManifestacoes)):
    print(i + 1, 'Posição - Manifestação:', listaManifestacoes[i])

def criarManifestacoes(manifestacoes):
  
  tipoManifestacao = int(input("Digite a opção da manifestação: "))
  
  if tipoManifestacao == 1:
    tipoManifestacao = "Sugestão"
  elif tipoManifestacao == 2:
    tipoManifestacao == "Reclamação"
  elif tipoManifestacao == 3:
    tipoManifestacao == "Elogio"
  
  novaManifestacao = input("Digite sua sugestão: ")
  
  sql = "insert into manifestacoes(tipo_manifestacao, manifestacao) values (%s, %s);"
  dados = (tipoManifestacao, novaManifestacao)
  insertNoBancoDados(connection, sql, dados)
      
  print("Sugestão cadastrada com sucesso")
  

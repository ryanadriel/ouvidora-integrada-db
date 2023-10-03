from operacoesbd import *
from operacoesOuvidoria import *

connection = abrirBancoDados('localhost', 'root', '', 'ouvidoria-facisa')

opcao = 0
manifestacoes = [ [] for _ in range(3) ]

while opcao != 5:
  print("Bem vindo ao sistema de ouvidoria! \n Digite uma opção: \n 1 - Listar \n 2 - Cadastro \n 3 - Exclusão \n 4 - Alteração \n 5 - Desconectar")
  
  opcao = int(input("Digite um opção: "))
  
  #Listagem de manifestações
  if opcao == 1:
    print("Listagem de Manifestações")
    
    listarManifestacoes(manifestacoes)
  
  #Adicionar manifestação
  elif opcao == 2:
    print("Insira os dados para adicionar uma nova manifestação:")
    print("Escolha o tipo de manifestação: \n 1 - Sugestão \n 2 - Reclamação \n 3 - Elogio")
    
    criarManifestacoes(manifestacoes)
      
  #Remover Manifestação
  elif opcao == 3:
    print("Escolha o tipo de manifestação a ser removida: \n 1 - Sugestão \n 2 - Reclamação \n 3 - Elogio")
    tipoManifestacao = int(input("Digite a opção: "))
    
    if tipoManifestacao == 1:
      print("Remover sugestão")

      for manifesto in range(len(manifestacoes[0])):
        print('-', manifesto + 1, manifestacoes[0][manifesto])
      
      opcaoManifesto = int(input("Digite a opção para ser removida: "))
      
      manifestacoes[0].pop(opcaoManifesto - 1)
      print("Manifestação removida com sucesso")
      
  elif opcao == 4:
    print("Escolha o tipo de manifestação a ser alterada: \n 1 - Sugestão \n 2 - Reclamação \n 3 - Elogio")
    tipoManifestacao = int(input("Digite a opção: "))
    
    if tipoManifestacao == 1:
      print("Alterar sugestão")

      for manifesto in range(len(manifestacoes[0])):
        print('-', manifesto + 1, manifestacoes[0][manifesto])
      
      opcaoManifesto = int(input("Digite a opção para ser alterada: "))
      
      novoManifesto = input("Digite a nova manifesteção")
      
      manifestacoes[0] = novoManifesto
      print("Manifestação alterada com sucesso")
    
   
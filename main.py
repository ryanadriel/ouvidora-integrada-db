opcao = 0
manifestacoes = [ [] for _ in range(3) ]

while opcao != 5:
  print("Bem vindo ao sistema de ouvidoria! \n Digite uma opção: \n 1 - Listar \n 2 - Cadastro \n 3 - Exclusão \n 4 - Alteração \n 5 - Desconectar")
  
  opcao = int(input("Digite um opção: "))
  
  if opcao == 1:
    #Listagem de manifestações
    if len(manifestacoes) != 0:
      print("Listagem de Manifestações:")
      for x in manifestacoes:
        print("-" + x)
    else:
      print("Não possui manifestações no momento!")
      
  elif opcao == 2:
    print("Insira os dados para adicionar uma nova manifestação:")
    print("Escolha o tipo de manifestação: \n 1 - Sugestão \n 2 - Reclamação \n 3 - Elogio")
    
    tipoManifestacao = input("Digite o tipo da manifestacao: ")
    
    if tipoManifestacao == 1:
      novaSugestao = input("Digite sua sugestão")
      manifestacoes.append(0, novaSugestao)
      print("Manifestação cadastrada com sucesso")
    
    elif tipoManifestacao == 2:
      novaReclamacao = input("Digite sua Reclamação: ")
      manifestacoes.append(1, novaReclamacao)
      print("Manifestação cadastrada com sucesso")
    elif tipoManifestacao == 3:
      novoElogio = input("Digite seu elogio: ")
      manifestacoes(3, novoElogio)
      print("Manifestação cadastrada com sucesso")
  elif opcao == 3:
    
    if len(manifestacoes) != 0:
      print("Manifestações:")
      
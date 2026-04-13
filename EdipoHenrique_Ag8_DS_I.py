
#Iniciar os contadores
excelente = 0
ruim = 0

for i in range(1, 5):
    print(f"Entrevistado {i} ---:\n")

    #Coletar informações do entrevistado

    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")

    #Coleta de opinião
    print("\nOpinião sobre o atendimento: ")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = input("\nDigite o número da sua opinião: ")

    #Estrutura de decisão para contabilizar 

    if opiniao == "1":
        excelente = excelente + 1
    if opiniao == "3":
        ruim = ruim + 1
    # opinião 2 não será contabilizada

#Exibir os resultados

print("\n--- RESULTADO DA PESQUISA")
print("Quantidade de votos EXCELENTES --> ", excelente)
print("Quantidade de votos RUINS --> ", ruim)




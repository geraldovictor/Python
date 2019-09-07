print("Hello","world!!",sep="-", end="\n")
quantidade = 5
print(type(quantidade))
nome = "geraldo"
print(type(nome))
dia = 5
mes = 3
ano = 1998
tentativas = 3

print("********************")
print("Jogo de adivinhação")
print("********************")

print("Adivinhe o ano que eu nasci")

exemplo = input("Digite uma entrada: ")
chute= int(exemplo)
print("sua entrada: ",exemplo)

if(ano==chute):
    print("voce acertou")
else:
    print("voce errou")
tentativas-=1

while (tentativas>0 and chute!=ano): #precisa dar tab para o que estiver dentro do while ser interpretado
    pass #verifica se não tem nenhum erro de sintaxe
    print("********************")
    print("Jogo de adivinhação")
    print("********************")

    print("Adivinhe o ano que eu nasci")

    exemplo = input("Digite uma entrada: ")
    chute= int(exemplo)
    print("sua entrada: ",exemplo)

    if(ano==chute):
        print("voce acertou")
    else:
        print("voce errou")
    tentativas-=1

print("o ano que eu nasci é %d" %ano)

print(len(nome)) # retorna quantas letras tem o nome

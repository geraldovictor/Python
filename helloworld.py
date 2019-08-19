print("Hello","world!!",sep="-", end="\n")
quantidade = 5
print(type(quantidade))
nome = "geraldo"
print(type(nome))
dia = 5
mes = 3
ano = 1998
tentativas = 3


while (tentativas>0 || ano==chute):
    pass
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

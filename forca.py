# ROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS
palavra = "escola"
limite_tentativas = len(palavra)+ 5

letras_acertadas =[]
for letra in palavra:
        letras_acertadas.apend("_")

contador = 1
while(contador <= limite_tentativas):
    print("tentativas:", contador,"/", limite_tentativas)
    chute = input("digite a letra:")
    print(chute)
    for letra in palavra:
        if chute == letra:
            print("acertou")
        else :
            print("errou")
        indice = 0
        for letra in palavra:
            if chute == letra:
            
               letras_acertadas[indice] = chute
               índice= indice +1
    contador = contador +1


# Para executar: python3 forca.py
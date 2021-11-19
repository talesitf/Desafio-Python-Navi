from math import *

X = []
media = 0
posicao_maior = 0

maior = -inf

#PERCORRE AS 10 POSIÇÕES
for i in range(0,10): 
    
    #CALCULA O NÚMERO A SER ADICONADO 
    if i%2 == 0:
        adicao = 3**i + 7*factorial(i)
        media += adicao
        X.append(adicao)
    else:
        adicao = 2**i + 4*log(i)
        media += adicao
        X.append(adicao)
    #FAZ A COMPARAÇÃO PRA DECIDIR O MAIOR NÚMERO E SUA POSIÇÃO
    if adicao > maior: 
        posicao_maior = i
        maior = adicao

media = media/10
print('A posição do maior elemento desse vetor é {%d} e a média desse vetor é: %.2f' % (posicao_maior,media))
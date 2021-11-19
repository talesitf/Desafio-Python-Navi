num_min = 2*49*37 # O menor número par,múltiplo de 37 e múltiplo de 49 simultaneamente é num_min

n_multiplos = int(5000000/num_min) # O número de múltiplos de um número em um intervalo é a parte inteira 
                                   # da divisão do limite máximo do intervalo por dito número

print('Existem, entre 1 e 5000000, {} números que são simultaneamente: Pares, múltiplos de 37 e de 49.'.format(n_multiplos))
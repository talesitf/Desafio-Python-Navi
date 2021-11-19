dict_notas = {}
maior = -1
aluno_m ='a'
for i in range(0,5):
    nome = input('Aluno:')
    nota = float(input('Nota:'))
    dict_notas[nome] = nota

for Aluno in dict_notas.keys():
    if dict_notas[Aluno] > maior:
        maior = dict_notas[Aluno]
        aluno_m = Aluno
    
    
print('O aluno com maior nota é ''{}'' com nota: {}'.format(aluno_m,maior))
 
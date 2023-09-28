# -*- coding: utf-8 -*-
"""
2023/2

@author: joisa
"""

# QUESTAO:
# Considere o dicionario dicPorMat com:
    
# CHAVE (do dic externo): MATRICULA DO ALUNO
# VALOR: dicionário interno com disciplinas e respectivas 
#        notas desse aluno, ou seja:
#            CHAVE (do dic interno): disciplina
#            VALOR: nota do aluno na disciplina 

# Um dicionário com essa descrição é disponibilizado 
# no bloco principal

# 1A) Escreva uma função, denominada qualNota, que:
#     - receba o dicionario descrito, um aluno (mat) e uma 
#     disciplina
#     - retorne a nota do aluno na disciplina. Caso o aluno 
#     não seja encontrado,deve ser retornado -1. Caso a 
#     disciplina não tenha sido cursada pelo aluno,  deve 
#     ser retornado -2.

def qualNota(dic, mat, dis):
    info = dic.get(mat)
    if info == None:
        return -1
    score = info.get(dis)
    return score
    


# 1B) Escreva uma função, denominada criaDicBonsDeUmaDisc, que:
#     - receba o dicionario por matricula descrito no 
#       inicio da questao e uma disciplina
#     - crie e retorne um novo dicionário somente com 
#     os alunos com nota maior do que 7 na disciplina,
#     em que cada elemento é:
#     CHAVE : aluno (mat)
#     VALOR: nota do aluno na disciplina 

def criaDicBonsDeUmaDisc(dic, disp):
    newdic = {}
    for student, classes in dic.items():
        score = classes.get(disp, 0)
        if score > 7:
            newdic[student] = score
    return newdic

# 1C) Escreva uma função, denominada criaDicPorDisc, que:
#     - receba o dicionario por matricula descrito
#     - crie e retorne um novo dicionário de dicionarios, 
#     em que cada elemento é:
#     CHAVE (dic externo): disciplina
#     VALOR: dicionario com alunos e respectivas notas 
#            nessa disciplina, ou seja:
#            CHAVE (do dic interno): aluno (matricula)
#            VALOR: nota do aluno na disciplina     
           


def criaDicPorDisc(dic):
    newdic = {}
    for student, classes in dic.items():
        for disp, score in classes.items():
            liststudents = newdic.get(disp, {})
            liststudents[student] = score
            newdic[disp] = liststudents
    return newdic


            

#BLOCO PRINCIPAL


dicPorMat= {'1612299': {'ENG1000': 7.8, 'FIS1033': 5.7, 'MAT1161': 7.6, 'QUI1740': 7.9}, 
            '1413399': {'ENG1000': 8.4, 'MAT1161': 9.2, 'MAT1260': 5.3}, 
            '1511188': {'FIS1033': 8.7, 'MAT1161': 8.5, 'QUI1740': 8.3}, 
            '1412222': {'FIS1033': 5.8, 'MAT1161': 7.2, 'MAT1260': 5.9}, 
            '1619999': {'ENG1000': 6.7, 'MAT1260': 5.1}, 
            '1617777': {'MAT1260': 6.3, 'QUI1740': 9.4}, 
            '1418833': {'ENG1000': 6.9, 'FIS1033': 7.1}, 
            '1611155': {'MAT1260': 5.3, 'QUI1740': 8.9}, 
            '1414466': {'FIS1033': 9.4, 'MAT1161': 5.5, 'MAT1260': 6.1}, 
            '1312211': {'FIS1033': 6.7, 'QUI1740': 6.7}, 
            '1713300': {'ENG1000': 6.3, 'FIS1033': 5.4, 'MAT1161': 5.4, 'MAT1260': 7.1}, 
            '1111188': {'MAT1161': 4.5, 'MAT1260': 6.1}, 
            '1412200': {'ENG1000': 6.2, 'MAT1260': 6.6}, 
            '1519911': {'MAT1260': 9.1, 'QUI1740': 5.4}, 
            '1512211': {'ENG1000': 8.3, 'MAT1161': 9.1}, 
            '1417700': {'FIS1033': 6.6, 'QUI1740': 8.8}, 
            '1618811': {'MAT1260': 4.8, 'QUI1740': 8.2}, 
            '1511100': {'MAT1161': 7.1, 'MAT1260': 7.3}, 
            '1414400': {'ENG1000': 6.7, 'MAT1161': 6.7, 'MAT1260': 6.7}}



print('\n---- Teste da 1A----')
print('MAT: 9992222 - DISC: FIS1033')
resp= qualNota(dicPorMat,'9992222','FIS1033' )
if resp == -1:
    print('Aluno não encontrado')
elif resp == -2:
    print('Aluno não cursou a disciplina')
else:
    print('NOTA:', resp)
    
print('\nMAT: 1512211 - DISC: FIS1033')
resp= qualNota(dicPorMat,'1512211','FIS1033' )
if resp == -1:
    print('Aluno não encontrado')
elif resp == -2:
    print('Aluno não cursou a disciplina')
else:
    print('NOTA:', resp)
    
print('\nMAT: 1713300 - DISC: FIS1033')
resp= qualNota(dicPorMat,'1713300','FIS1033' )
if resp == -1:
    print('Aluno não encontrado')
elif resp == -2:
    print('Aluno não cursou a disciplina')
else:
    print('NOTA:', resp)
    
print('\n---- Teste da 1B----')
print('Dic com alunos com nota > 7 em ENG1000 ')
dAc7= criaDicBonsDeUmaDisc(dicPorMat,'ENG1000')
print(dAc7)

print('\n---- Teste da 1C----')
dicPorDisc = criaDicPorDisc(dicPorMat)
print('DISCIPLINAS com seus alunos e notas ')
print(dicPorDisc)
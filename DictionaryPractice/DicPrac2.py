# -*- coding: utf-8 -*-
"""
Exercício para casa (em 29/03/2023)

@author: JOISA
"""
'''
Uma revista mensal sobre comida visita alguns restaurantes e pontua alguns aspectos com 
notas de 1 a 5, sendo 1 a pior nota para o aspecto e 5 a melhor nota. O resultado das 
visitas do últimos mês encontram-se no dicionário dos restaurantes abaixo, em que cada 
elemento/item é  RESTAURANTE: { dicionário com aspectos e pontuação de cada aspecto}

'''

dicRestaurante= { 'CEU_AZUL' :{'comida': 3 , 'preco': 3 , 'atendimento': 2 ,'localizacao':3 },

                  'DELIXIUS' :{'comida': 4 , 'preco': 3 , 'atendimento': 5 ,'localizacao':5},

                  'GULLOZZOS':{'comida': 5 , 'preco': 2 , 'atendimento': 4 ,'localizacao':4},

                  'XIKIXOKO' :{'comida': 3 , 'preco': 3 , 'atendimento': 3 ,'localizacao':3},

                  'TEMPERINHO':{'comida': 3 , 'preco': 4 , 'atendimento': 4 ,'localizacao':3},

                  'FAVORITO' :{'comida': 4 , 'preco': 4 , 'atendimento': 3 ,'localizacao':4}

                }
'''
A) Escreva uma função, denominada notaDeUmAspectoDoRestaurante,  que:

- receba um restaurante, um aspecto e o dicionário dos restaurantes (dicionário de dicionários 
em que cada elemento/item é  RESTAURANTE: { dicionário com aspectos e pontuação de cada 
aspecto}, ou seja, CHAVE acaba sendo o Restaurante e o VALOR acaba sendo um dicionario de aspecto-nota )
- retorne a nota desse aspecto do restaurante recebido

'''
def notaDeUmAspectoDoRestaurante(rest, asp, dic):
    aspects = dic.get(rest)
    print(aspects)
    if aspects == None:
        print("Restaurant doesn't exist!")
        return 0
    score = aspects.get(asp)
    return score


'''
B) Escreva uma função, denominada notaFinalDoRestaurante,  que:

- receba um restaurante e o dicionário dos restaurantes (dicionário de dicionários 
em que cada elemento/item é  RESTAURANTE: { dicionário com aspectos e pontuação de cada 
aspecto}, 
- retorne a nota final do restaurante (soma das notas/4)

'''
def notaFinalDoRestaurante(rest, dic):
    tot = 0
    aspects = dic.get(rest, 0)
    if aspects == None:
        print("Restaurant doesn't exist")
        return 0
    for score in aspects.values():
        tot += score

    return tot / 4

'''
C) Escreva uma função, denominada criaDicNotasFinaisDosRestaurantes,  que:

- receba o dicionario dos restaurantes (dicionário de dicionários 
em que cada elemento/item é  RESTAURANTE: { dicionário com aspectos e pontuação de cada 
aspecto}, 
-  crie e retorne um novo dicionario em que cada elemento acaba sendo:
         RESTAURANTE: nota final do restaurante

'''
def criaDicNotasFinaisDosRestaurantes(dic):
    newdic = {}
    for rest in dic:
        score = notaFinalDoRestaurante(rest, dic)
        newdic[rest] = score
    return newdic


'''
D)
Considere um dicionario com pesos para as diferentes aspectos avaliados:

dPesos = {'comida': 10 , 'preco': 2 , 'atendimento': 7 ,'localizacao':8}

Escreva uma função, denominada notaFinalPonderadaDoRestaurante,  que:

- receba um restaurante , o dicionario de pesos dos aspectos e o dicionário dos restaurantes
(dicionário de dicionários  em que cada elemento/item é  RESTAURANTE: { dicionário com aspectos e pontuação de cada 
aspecto}, 
- retorne a nota final do restaurante considerando os pesos recebidos 

'''
def notaFinalPonderadaDoRestaurante(rest, dPesos, dRest):
    dAspNotaDoRest = dRest.get(rest)
    if dAspNotaDoRest==None:
        print ('Restaurante nao encontrado')
        return 0
    
    # usando variaveis desnecessarias:
    notaAcum=0
    # ao totalizar devem ser considerados os pesos de cada aspecto
    for (aspecto, nota) in dAspNotaDoRest.items():
        notaAcum += nota*dPesos[aspecto]
    somaDosPesos = sum(dPesos.values())
    notaFinal = notaAcum/somaDosPesos 
    return notaFinal


'''
E) Escreva uma função, denominada criaDicAsp, que receba o dicionario 
de restaurantes e um aspecto, e crie e retorne um novo dic com
CHAVE: restaurante
Valor: Nota do aspecto nesse restaurante
'''
def criaDicAsp( dicRest , asp ):
    dRestNota ={}
    for rest, dAspNota in dicRest.items():
        dRestNota[rest]= dAspNota[asp]
    return dRestNota


#########################################################
#  BLOCO PRINCIPAL

dicRestaurante= { 'CEU_AZUL' :{'comida': 3 , 'preco': 3 , 'atendimento': 2 ,'localizacao':3 },

                  'DELIXIUS' :{'comida': 4 , 'preco': 3 , 'atendimento': 5 ,'localizacao':5},

                  'GULLOZZOS':{'comida': 5 , 'preco': 2 , 'atendimento': 4 ,'localizacao':4},

                  'XIKIXOKO' :{'comida': 3 , 'preco': 3 , 'atendimento': 3 ,'localizacao':3},

                  'TEMPERINHO':{'comida': 3 , 'preco': 4 , 'atendimento': 4 ,'localizacao':3},

                  'FAVORITO' :{'comida': 4 , 'preco': 4 , 'atendimento': 3 ,'localizacao':4}

                }

print('------ Dicionário dos restaurantes ------')
print(dicRestaurante)

print('\n------------------------------------------')

print('--- A) Testes da notaDeUmAspectoDoRestaurante --- ')        
respostaA = notaDeUmAspectoDoRestaurante('TEMPERINHO','atendimento',dicRestaurante)
print(respostaA)
respostaA = notaDeUmAspectoDoRestaurante('TEMPERAO','atendimento',dicRestaurante)
print(respostaA)
respostaA = notaDeUmAspectoDoRestaurante('TEMPERINHO','ambiente',dicRestaurante)
print(respostaA)

print('\n------------------------------------------')

print('--- B) Teste da notaFinalDoRestaurante --- ') 
respostaB= notaFinalDoRestaurante('GULLOZZOS',dicRestaurante )
print(respostaB)

print('\n------------------------------------------')

print('--- C) Teste da criaDicNotasFinaisDosRestaurantes --- ') 
dicRestNotaFinal= criaDicNotasFinaisDosRestaurantes(dicRestaurante)
print(dicRestNotaFinal)

print('\n------------------------------------------')

print('--- D) Teste da criaDicNotasFinaisDosRestaurantes --- ') 
criaDicNotasFinaisDosRestaurantes
dPesos = {'comida': 10 , 'preco': 2 , 'atendimento': 7 ,'localizacao':8}
respostaD= notaFinalPonderadaDoRestaurante('FAVORITO',dPesos,dicRestaurante)
print('FAVORITO->', respostaD)
respostaD= notaFinalPonderadaDoRestaurante('TEMPERINHO',dPesos,dicRestaurante)
print('TEMPERINHO->', respostaD)

print('\n------------------------------------------')
print('--- E) Teste da criaDicAsp --- ') 
dRN= criaDicAsp(dicRestaurante,'preco' )
print(dRN)

print('\n------------------------------------------')

###########################################################
#   SAIDA  ESPERADA  PARA OS TESTES DISPONIBILIZADOS

# ------ Dicionário dos restaurantes ------
# {'CEU_AZUL': {'comida': 3, 'preco': 3, 'atendimento': 2, 'localizacao': 3}, 
#  'DELIXIUS': {'comida': 4, 'preco': 3, 'atendimento': 5, 'localizacao': 5}, 
#  'GULLOZZOS': {'comida': 5, 'preco': 2, 'atendimento': 4, 'localizacao': 4}, 
#  'XIKIXOKO': {'comida': 3, 'preco': 3, 'atendimento': 3, 'localizacao': 3}, 
#  'TEMPERINHO': {'comida': 3, 'preco': 4, 'atendimento': 4, 'localizacao': 3}, 
#  'FAVORITO': {'comida': 4, 'preco': 4, 'atendimento': 3, 'localizacao': 4}}

# ------------------------------------------
# --- A) Testes da notaDeUmAspectoDoRestaurante --- 
# 4
# Restaurante nao encontrado
# 0
# Aspecto nao avaliado
# 0

# ------------------------------------------
# --- B) Teste da notaFinalDoRestaurante --- 
# 3.75

# ------------------------------------------
# --- C) Teste da criaDicNotasFinaisDosRestaurantes --- 
# {'CEU_AZUL': 2.75, 'DELIXIUS': 4.25, 'GULLOZZOS': 3.75, 
#  'XIKIXOKO': 3.0, 'TEMPERINHO': 3.5, 'FAVORITO': 3.75}

# ------------------------------------------
# --- D) Teste da criaDicNotasFinaisDosRestaurantes --- 
# FAVORITO-> 3.740740740740741
# TEMPERINHO-> 3.3333333333333335

# ------------------------------------------
# -*- coding: utf-8 -*-
###########################################################################################
#########################################################################################
# Turma:
# Professor:
# Nome completo:
# Matrícula PUC-Rio:

###########################################################################################
###########################################################################################
'''
Questão 2 
Teste as classes construídas por você, executando o código que se encontra 
comentado na área de testes 

'''
from dataP1 import *
#Escreva aqui a classe Arquivo

class Arquivo:
    def __init__(self, nome, autor, start, text = " ", end = Data()):
        self.nome = nome
        self.autor = autor
        self.start = start 
        self.text = text
        self.end = end

    def __str__(self):
        s = "{}.txt, {}, {}, {}".format(self.nome, self.autor, self.start, Arquivo.tamanho(self))
        return s
    
    def __repr(self):
        r = "{}.txt, {}, {}, {}".format(self.nome, self.autor, self.start, Arquivo.tamanho(self))
        return r
    
    def __add__(self, other):
        name = "{} {}".format(self.name, other.name)
        autor = "sistema"
        text = "{}\n{}".format(self.text, other.text)
        day = Data()
        return Arquivo(name, autor, day, text)
    
    def tamanho(self):
        size = len(self.text)
        return size
    
    def substituiTexto(self, text, date):
        self.text = text
        self.end = date
        
    def adicionaTexto(self, text, date):
        self.text = "{}{}".format(self.text, text)
        self.end = date

    def exibeTexto(self):
        print("{}".format(self.text))

    def ultimaAlteracaoNaData(self, date):
        return self.end == date
        


#Escreva aqui a classe Pasta

class Pasta:
    def __init__(self, name, list):
        self.name = name
        self.list = list

    def __str__(self):
        s = ""

#-------- Área de teste da questao 2 --------
print('\n------ Teste da Q2 ------')
'''Retire # das linhas abaixo'''
# print("\n=====================================")
# print("ARQUIVOS CRIADOS")
# print("=====================================")

# arq1=Arquivo('comprasFrutas','fifi',Data(12,4,2023),'abacate,pera,abacaxi,manga')
# print(arq1)
# print("Texto do arquivo: ")
# arq1.exibeTexto()

# '''Adicionando texto'''
# dtAlteracao=Data(19,4,2023)
# arq1.adicionaTexto(',banana,laranja',dtAlteracao)
# print("\n")
# print(arq1)
# print("Texto do arquivo: ")
# arq1.exibeTexto()

# '''Teste da data da última alteração'''
# if arq1.ultimaAlteracaoNaData(dtAlteracao):
#     print("\n\n-->A última alteração do arquivo FOI em {}".format(dtAlteracao))
# else:
#     print("\n\n-->A última alteração do arquivo NÃO foi em {}}".format(dtAlteracao))

# print("--------------------------------")
# print("--------------------------------")

# arq2=Arquivo('comprasBebidas','guga',Data(10,4,2023))
# print(arq2)
# print("Texto do arquivo: ")
# arq2.exibeTexto()

# '''Substituindo texto'''
# arq2.substituiTexto('suco,água',Data(21,4,2023))
# print("\n")
# print(arq2)
# print("Texto do arquivo: ")
# arq2.exibeTexto()

# print("--------------------------------")
# print("--------------------------------")

# '''Juntando dois arquivos'''
# arq3=arq1+arq2
# print(arq3)
# print("Texto do arquivo: ")
# arq3.exibeTexto()

# '''Teste da data da última alteração'''
# hoje=Data()
# if arq2.ultimaAlteracaoNaData(hoje):
#     print("\n\n-->A última alteração do arquivo FOI em {}".format(hoje))
# else:
#     print("\n\n-->A última alteração do arquivo NÃO foi em {}".format(hoje))



# print("--------------------------------")
# print("--------------------------------")

# arq4=Arquivo('convBibi','bibi',Data(1,4,2023),'juca,keko,kaka,lilo,mano,mimi,dora,zeze')
# print(arq4)
# print("Texto do arquivo: ")
# arq4.exibeTexto()

# print("--------------------------------")
# print("--------------------------------")

# print("\n======================================")
# print("PASTA CRIADA")
# print("======================================")
# pasta1=Pasta('festaNiver')
# print(pasta1)
# print("--------------------------------")
# print("Arquivos da pasta")
# pasta1.exibeArquivos()


# print("\n======================================")
# print("ARQUIVOS INCLUIDOS NAS PASTAS")
# print("======================================")

# '''Incluindo arquivos na pasta '''
# pasta1.incluiArquivo(arq1)
# pasta1.incluiArquivo(arq2)
# pasta1.incluiArquivo(arq3)
# pasta1.incluiArquivo(arq4)

# '''Exibindo pasta atualizada'''
# print(pasta1)
# print("Arquivos da pasta")
# pasta1.exibeArquivos()
# print("--------------------------------")

# '''Exibindo arquivos modificados em determinada data'''
# print("Arquivos alterado hoje na pasta {}\n".format(pasta1))
# pasta1.alteradosNaData(Data())


print('\n---- Fim do Teste da Q3 ----')             

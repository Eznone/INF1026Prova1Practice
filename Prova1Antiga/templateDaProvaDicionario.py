# -*- coding: utf-8 -*-
"""
###############################################################################
###############################################################################
# Turma:
# Professor:
# Nome completo:
# Matrícula PUC-Rio:
###############################################################################
###############################################################################
"""

# QUESTÃO 1a: Dicionário do Imposto de Renda.

#-----------Escreva a seguir a funcao exibeTotalRecebidoPorUmCPF ------

def exibeTotalRecebidoPorUmCPF(dic, cpf):
    tot = 0
    for paying, recievers in dic.items():
        for reciveing, amount in recievers.items():
            if reciveing == cpf:
                tot += amount
    print(f"{cpf} recieved the total amount of {tot}")



###################################################################
###################################################################

# QUESTÃO 1b: Dicionário dos tipos (fontes) de energia.

#-----------Escreva a seguir a funcao cria_dic_por_vantagem ------

def cria_dic_por_vantagem(dic):
    newdic = {}
    for type, info in dic.items():
        for vantage in info["vantagens"]:
            l = newdic.get(vantage, [])
            l.append(type)
            newdic[vantage] = l
    return newdic


###################################################################
#                        BLOCO PRINCIPAL
###################################################################
#------------------------------------------------------------------
# -----------------  Area de Teste da questão 1a -------------------

dPorPagador= {'34534522-00': { '67167776-73':3200, '75167776-23':1500,'27197776-78':2200, '58587776-73':3200,
                               '55455324-26':2500, '34167716-32':1000 },
              '75167776-23': {'27197776-78':1500, '58587776-73':1100,'34167716-32':5000, '67167776-73':2400},
              '58587776-73': {'55455324-26':1200, '67167776-73':1000, '34167716-32':2000},
              '34167716-32': {'55455324-26':3000, '75167776-23':1800, '27197776-78':1650},
              '98167716-38': {'62345324-26':1000, '34567776-23':1300, '67167776-73':5000,'27197776-78':650},
              '373537522-00': {'67167776-73':2200, '75167776-23':500,'23237676-78':2100}        
             }


print('\n---------- Teste da questão 1a ----------')
# Tire os # das linhas a seguir
  
# print('---Teste com CPF 67167776-73 ---' )
# exibeTotalRecebidoPorUmCPF(dPorPagador,'67167776-73')

# print('---Teste com CPF 99167776-74 ---' )
# exibeTotalRecebidoPorUmCPF(dPorPagador,'99167776-74')

# print('---Teste com CPF 55455324-26 ---' )
# exibeTotalRecebidoPorUmCPF(dPorPagador,'55455324-26')



###################################################################
#------------------------------------------------------------------
# -----------------  Area de Teste da questão 1b -------------------

dic_energia = {
    "solar": {
        "tecnologia": "Fotovoltaica", "capacidade": 1000,  "geracao": 800,
        "eficiencia": 0.8, "custo_por_kw": 0.12,
        "vantagens": ["renovavel", "limpa", "baixos custos operacionais"]
    },
    "eolica": {
        "tecnologia": "Turbina de vento", "capacidade": 2000, "geracao": 1500,
        "eficiencia": 0.85,  "custo_por_kw": 0.10,
        "vantagens": ["renovavel", "sem emissões", "recurso abundante"]
    },
    "hidreletrica": {
        "tecnologia": "Turbina hidraulica", "capacidade": 3000, "geracao": 2500,
        "eficiencia": 0.75, "custo_por_kw": 0.07,
        "vantagens": ["renovavel", "baixas emissoes", "longa vida util"]
    },
    "geotermica": {
        "tecnologia": "Ciclo binário ou outro", "capacidade": 500, "geracao": 400,
        "eficiencia": 0.9, "custo_por_kw": 0.15,
        "vantagens": ["renovavel", "baixas emissoes", "confiavel"]
    },
    "nuclear": {
        "tecnologia": "Reator nuclear", "capacidade": 4000, "geracao": 3500,
        "eficiencia": 0.95, "custo_por_kw": 0.14,
        "vantagens": ["alta densidade energetica", "baixas emissoes", "confiavel"]
    },
    "biomassa": {
        "tecnologia": "Combustao", "capacidade": 800, "geracao": 600,
        "eficiencia": 0.82, "custo_por_kw": 0.11,
        "vantagens": ["renovavel", "utilizacao de residuos"]
    }
}

print('\n---------- Teste da questão 1b ----------')
# Tire os # das  linhas a seguir
dPorVant= cria_dic_por_vantagem(dic_energia)
print(dPorVant)

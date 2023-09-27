# -*- coding: utf-8 -*-
"""
classe ContaBancaria
Joisa
"""
'''
Uma conta bancaria tem:
    o numero da conta
    a senha
    o nome do titular da conta
    o saldo da conta
    
Uma conta pode ser criada de duas formas:
    - fornecendo numero, senha, nome e saldo
    - fornecendo apenas, numero, senha e nome. Nesse caso o saldo 
    eÂ´ 0.0

Ao ser dado um print numa conta sao exibidos numero, nome e saldo

Uma conta bancaria pode:
    - exibir seu saldo, desde que seja recebida a senha 
      correta da conta. Caso a senha recebida seja incorreta 
      exibir mensagem: SENHA INCORRETA
    - ter um valor depositado, recebendo para isso o valor 
      a ser depositado. O valor deve ser adicionado ao saldo 
      da conta
    - ter um valor sacado, desde que para isso sejam recebidos 
      o valor a ser sacado e a senha da conta.
      Caso a senha seja incorreta, exibir a mensagem  
      SENHA INCORRETA e sinalizar que a operacao nao foi 
      realizada, retornando False.
      Caso o valor a ser sacado seja maior do que o saldo, 
      exibir a mensagem SALDO INSUFICIENTE e sinalizar que a operacao nao foi 
      realizada, retornando False.
      Caso seja possivel realizar o saque, subtrair o valor sacado 
      do saldo da conta e retornar True.
  
    
NOVO:
    Inclua na classe ContaBancaria os metodos magicos para fazer a comparacao 
    entre duas contas com > , < e ==, considerando o valor do saldo das contas.
'''


class ContaBancaria:
    
    def __init__(self, numero, senha, nome,saldo=0.0):
        self.numero=numero
        self.senha = senha
        self.nome = nome
        self.saldo = saldo
        return
    
    def __str__(self):
        s=str(self.numero)+'-'+self.nome+ '-'+ "{:.2f}".format(self.saldo) 
        return s
    
    def __repr__(self):
        s=str(self.numero)+'-'+self.nome+ '-'+ "{:.2f}".format(self.saldo) 
        return s
        
    def __lt__(self,outra):
        return self.saldo < outra.saldo
    
    def __gt__(self,outra):
        return self.saldo > outra.saldo
    
    def __eq__(self,outra):
        return self.saldo == outra.saldo
     
    def exibeSaldo(self, senha):
        if self.senha != senha:
            print('SENHA INCORRETA')
        else:
            print('SALDO EM CONTA: ','{:.2f}'.format(self.saldo))
        return
    
    def deposito(self, valor):
        self.saldo += valor
        
    def saque(self, valor,senha):
        if self.senha != senha:
            print('SENHA INCORRETA')
            return False
        if valor > self.saldo:
            print('SALDO INSUFICIENTE')
            return False
        self.saldo = self.saldo - valor
        return True
        

# #TESTES
# cb = ContaBancaria(111,'a2323','bibi',1500)
# print(cb)
# cb.deposito(200)
# print(cb)
# cb.saque(450,'a2323')
# print(cb)
# cb.saque(450,'oi')

# cx= ContaBancaria(555,'x2323','lala',3500)
# print(cx)
        
# if cb>cx:
#     print(cb, ' maior que ', cx)  
# else:
#     print(cx, ' maior que ', cb)  
     
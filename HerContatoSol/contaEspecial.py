from contaBancaria import ContaBancaria

class ContaEspecial(ContaBancaria):
    def __init__(self, numero, senha, nome, limite, saldo=0.0):
        super().__init__(numero, senha, nome, saldo)
        self.limite = limite

    def __str__(self):
        sup = super().__str__()
        s = "{} {}".format(sup, self.limite)
        return s
    
    def __repr__(self):
        sup = super().__str__()
        r = "{} {}".format(sup, self.limite)
        return r

    def aumentaLimite(self, valor):
        self.saldo += valor


    def saque(self, valor, senha):
        if self.senha != senha:
            print("Senha Incorreta")
            return False
        if valor > (self.saldo + self.limite):
            print("Saldo Insufficiente")
            return False
        self.saldo = self.saldo - valor
        return True

    def __gt__(self, other):
        return self.saldo > other.saldo
    
    def __lt__(self, other):
        return self.saldo < other.saldo


#Tests ----------------------------------------

# ce= ContaEspecial(111,'sxz','TUTI',500,1000)
# print(ce)

# ce.deposito(120)
# print(ce)
# ce.saque(1200,'sxz')
# print(ce)
# ce.aumentaLimite(400)
# print(ce)



# cv= ContaEspecial(544,'aas','Kity',700,900)
# print(cv>ce)
# print(cv<ce)



# lcontas=[]
# lcontas.append(ce)  
# c= ContaBancaria(999,'aba','DADA',8000)
# lcontas.append(c)
# c= ContaBancaria(666,'vvv','LILI',300)
# lcontas.append(c)
# ce= ContaEspecial(444,'uiu','NINA',900,2000)
# lcontas.append(ce)
# print(lcontas)

# print('\nLista de contas ordenada')
# print(sorted(lcontas))  # retorna uma copia da lista ordenada 
# print('\nLista de contas')
# print(lcontas)

# lcontas.sort() # ordena a lista
# print('\nLista de contas')
# print(lcontas)



# l = [35,12,88,4]
# print(l)
# print(sorted(l))
# print(l)
# l.sort()
# print(l)
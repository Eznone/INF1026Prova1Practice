from classeLIVRO import Livro


class LivroDeBiblioteca(Livro):
    def __init__(self, title, topic, authors, pages, list):
        super().__init__(title, topic, authors, pages)
        self.list = list

    def consultarLivro(self):
        return self.list
    
    def acrescentarExemplar(self, num):
        self.list.append([num, 'D'])
    
    def removerExemplar(self, num):
        for pos, item in enumerate(self.list):
            if num in item:
                removed = self.list.pop(pos)
                print(f"Item: {removed} was removed")
                return

    def emprestarExemplar(self):
        for item in self.list:
            if "D" in item:
                item[1] = "E"
                return f"Exemplar {item[0]} emprestado"
            
    def devolverLivro(self, num):
        for item in self.list:
            if num in item:
                item[1] = "D"
                print(f"Exemplar {num} devolvido")
                return 
        





# lb=LivroDeBiblioteca('KAOS','Fisica',['k.Yel','H.Teo'],45,[[342,'D'],[541,'D'],[121,'E'],[464,'D']])
# print(lb)
# print(lb.consultarLivro())
# lb.acrescentarExemplar(666)
# print(lb.consultarLivro())
# lb.removerExemplar(464)
# print(lb.consultarLivro())
# print(lb.emprestarExemplar())
# print(lb.consultarLivro())
# print(lb.emprestarExemplar())
# print(lb.consultarLivro())
# lb.devolverLivro(541)
# print(lb.consultarLivro())
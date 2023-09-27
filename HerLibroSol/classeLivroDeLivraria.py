from classeLIVRO import Livro

class LivroDeLivraria(Livro):
    def __init__(self, title, topic, authors, pages, price, stock):
        super().__init__(title, topic, authors, pages)
        self.price = price
        self.stock = stock

    def __str__(self):
        sup = super().__str__()
        s = "{}, Price: {}, Stock: {}".format(sup, self.price, self.stock)
        return s
    
    def __repr__(self):
        sup = super().__str__()
        r = "{}, Price: {}, Stock: {}".format(sup, self.price, self.stock)
        return r
    
    def consultaPreco(self):
        return self.price
    
    def vendeLivro(self, amount):
        if amount > self.stock:
            print("Not enough books in stock")
            return False
        self.stock -= amount
        tot = self.price * amount
        return f"Total price is: ${tot}"
    
    def __iadd__(self, amount):
        self.stock += amount
        return self
    
    def __imul__(self, amount):
        self.price *= amount
        return self

# ll= LivroDeLivraria('Out','Ficcao',['J.Morgan'],385,50.50,30)
# print(ll)
# print(ll.vendeLivro(2))
# print(ll)


# ll +=22
# print(ll)

# ll *=20
# print(ll)

# print(ll.consultaPreco())

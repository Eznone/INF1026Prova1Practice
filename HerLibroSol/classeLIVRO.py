

class Livro:
    def __init__(self, title, topic, authors, pages):
        self.title = title
        self.topic = topic
        self.authors = authors
        self.pages = pages
    
    def __str__(self):
        s = "Title: {}, Topic: {}, Authors: {}, Num pages: {}".format(self.title, self.topic, self.authors, self.pages)
        return s
    
    def __repr__(self):
        r = "Title: {}, Topic: {}, Authors: {}, Num pages: {}".format(self.title, self.topic, self.authors, self.pages)
        return r

# liv= Livro('Mares','Bio',['F.Moraes','J.Niles'],287)
# print(liv)
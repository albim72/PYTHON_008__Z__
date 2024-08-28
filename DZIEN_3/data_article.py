from dataclasses import dataclass

@dataclass
class Article:
    title:str
    author:str
    content:str
    def __repr__(self):
        return f'{self.title} -> {self.author}: {self.content}'

@dataclass(init=False)
class PythonArticle(Article):
    language:str
    author:str
    price:int = 0
    def __init__(self,title,price):
        self.title = title
        self.price = price
        self.language = "Python 3"
        self.author = "Marcin Albiniak"
        self.content = "Opis wybranych aspektów użycia języka Python"

    def __repr__(self):
        return f'Publikacja {self.title}, autor: {self.author}, cena: {self.price} zł'

    def infoarticle(self):
        return (f'Publikacja: {self.title}, autor: {self.author}, rabat:{0.1*self.price:.2f} zł,'
                f'kwota do zapłaty: {0.9*self.price:.2f} zł')

art = Article("Typowanie w języku Java","Jan Kos","Kilka słów o typach....")
print(art)

artpy = PythonArticle("Algorytmy DL w Pythonie",67.6)
print(artpy)
print(artpy.infoarticle())


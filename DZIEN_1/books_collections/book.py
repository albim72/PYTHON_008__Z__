from abc import ABC,abstractmethod

class Book(ABC):
    def __init__(self,title,author,year,pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        
    @abstractmethod
    def get_info(self):
        pass
    
    @abstractmethod
    def read(self):
        pass

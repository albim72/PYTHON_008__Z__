from bcollections import BookCollections
from books.novel import Novel
from books.novel import Novel
from books.textbook import TextBook


collection = BookCollections()
novel = Novel("1984","George Orwell",1949,328)
textbook = TextBook("Python programming","John Porter",2020,450)

collection.add_book(novel)
collection.add_book(textbook)

collection.display_all_books()

novel.read()
textbook.read()










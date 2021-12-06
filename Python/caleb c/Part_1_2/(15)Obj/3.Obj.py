#in object oriented programming, functions are known as methods

class Book():
    def __init__(self, title,pages):           #every single book is going to have a title
        self.title = title                #whenever we say self we are refering to the object, so we setting the books title to what ever is passed to the method "__init__"
        self.pages = pages
        
    def is_long(self):
        if self.pages >100:
            return "The book is long (has more than 100 pages)"
        else:
            return "This is a short book"
            
            
book = Book("Advanced engineering mathematics.",3000)
print(book.title)
print(book.is_long())

book2 = Book("Test",30)
print(book2.title,book2.is_long())




#the method __init__ is known as the initializer in python (or constructor in another programming language)


#self refers to the object (class) we are invoking it on (i.e self just says "in class Book" we crete a function .... with parameter ....)
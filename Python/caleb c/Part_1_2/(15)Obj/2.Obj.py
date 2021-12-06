#in object oriented programming, functions are known as methods

class Book():
    def __init__(self, title):           #every single book is going to have a title
        self.title = title                #whenever we say self we are refering to the object, so we setting the books title to what ever is passed to the method "__init__"
        
book = Book("Advanced engineering mathematics.")
print(book.title)



#the method __init__ is known as the initializer in python (or constructor in another programming language)

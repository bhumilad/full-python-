

class LibraryManagement:

    def __init__(self,list_of_book,library_name):
        self.lend_data={}
        self.list_of_book=list_of_book
        self.library_name=library_name

        # adding book in library
        for book in self.lend_data:
            # none means no author have land this book
          self.lend_data[book]=None

    # display Book
    def displayer(self,list_of_book):
        for index,book in self.lend_data:
            return f"the display {index} {book}"

    # land book
    def lander(self,book,author):
        if book in self.list_of_book:
            if self.lend_data[book] is None:
                self.lend_data[book]=author
            else:
                print("sorry,this book is lend by",self.lend_data[book])
        else:
            print("sorry!please write a correct name of the book")

    #return book
    def returner(self,book,author):
        if book in self.list_of_book:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("ohh,book is already lend")
        else:
            print("sorry!please write a correct name of the book")

    # adding book
    def adder(self,bname):
        self.list_of_book.append(bname)
        self.lend_data[bname]= None

if __name__ == '__main__':

 library_name="RAINBOW LIBRARY"


print("NAME OF THE LIBRARY : ",library_name)
print("hello guys!welcome in my library")
print("for adding book 'a'")
print("for displaying book 'd'")
print("for lending book 'l'")
print("for returning book 'r")

jerry=LibraryManagement(list_of_book=["self love","art of hindu love","5'clock","rules of brain"],library_name="RAINBOW LIBRARY")

# creating option:
Exit=False
while Exit is not True:
    inp=input("option:")

    if inp == 'q':
        Exit=True

    elif inp=='a':
        inp1=input("BOOK NAME:")
        jerry.adder(inp1)

    elif inp=='d':
        jerry.displayer(list_of_book)

    elif inp=='l':
        inp1=str(input("WHICH BOOK DO YOU WANT TO LENDING:"))
        jerry.lend_data(inp1)
        print(" \n yeah congo !! book lend")

    elif inp=='r':
        inp1=input("WHICH BOOK DO YOU WANT TO REVERSING:")
        jerry.returner(inp1)



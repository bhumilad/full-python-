class LibraryManagment:

    def __init__(self,book,name):
        self.lend_dict={}
        self.libraryname=name
        self.list_of_book=book

    # for displaying book
    def display_book(self, book):
        for book in self.list_of_book:
            print(book)

    # for adding book
    def add_book(self,user,books):
        self.list_of_book.append(user,books)

    # for lending book
    def lend_book(self,book,user):
        print("lending  book")
        self.lend_dict.keys()

    # for returning book
    def return_book(self):
        self.lend_dict.pop()

if __name__ == '__main__':

     library_name = "RAINBOW LIBRARY"
     print("NAME OF THE LIBRARY : ", library_name)

     list_of_book=['python','c++','java','hacking']
     jerry=LibraryManagment(list_of_book,library_name)
     print("1.display book\n2.add book\n3.lend book\n4.return book")
     choice_of_book=int(input("enter your choice:"))


     while(True):

         if choice_of_book==1:
              jerry.display_book(list_of_book)



         elif choice_of_book==2:
              books=input("which book you want to add:")
              user=input("enter your name:")
              book=jerry.add_book(list_of_book[user,books])
              print(book)
              print("your book added")


         elif choice_of_book==3:
             print("lending the book",jerry.lend_book())

         elif choice_of_book==4:
             print("returning the book",jerry.return_book())

         else:
             print("Opps!!!please enter the correct option")

         # q for quit and c for continue
         lastchoice =input(print("'q' for quit and 'c' for continue"))
         if lastchoice=='q':
              print("thank you for visiting my library")
              exit()
         elif lastchoice=='c':
              continue
         else:
              print("you have only 2 option 'q' or 'c'")
              #over



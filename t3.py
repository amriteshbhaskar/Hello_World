class Book:
    '''This is a book class'''
    all_ano = []

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.accession_nos = []
        self.price = {}
        self.issued_books = {}
        
    def add_books(self,*prices):
        for price in prices:
            ano = len(self.all_ano) + 1
            self.accession_nos.append(ano)
            self.price[ano] = price
            self.all_ano.append(ano)

    def issue_book(self,member):
        for ano in self.accession_nos:
            if ano not in self.issued_books.keys():
                self.issued_books[ano] = member
                return ano
                break
        return 'Book not available'

    def return_book(this,ano):
        del(this.issued_books[ano])
        return 'Book returned successfully'

    def __repr__(self):
        return "Book Name: " + self.title.title()
class Member:
    '''This is a member class'''
    all_id = []

    def __init__(self, name):
        self.name = name
        mno = len(self.all_id)+1
        self.all_id.append(mno)
        self.idno = mno
        self.issued_books = {}

    def issue_book(self,book):
        bid = book.issue_book(self)
        if bid != 'Book not available':
            self.issued_books[book]=bid

    def return_book(this,book):
        book.return_book(this.issued_books[book])
        del(this.issued_books[book])

    def __repr__(self):
        return "Member Name: " + self.name.title()

letusc = Book('Let us C','9788183331630')
letusc.add_books(135)
letusc.add_books(138)
letusc.add_books(160)

l_python = Book('Learning Python','9789351102014')
l_python.add_books(1350)
l_python.add_books(1380,1560)

abhi = Member('Abhi')
ram = Member('Ram')
arpit=input()
class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return[contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        related_books = []
        for contract in Contract.all:
            if contract.author == self:
                related_books.append(contract.book)
        return related_books
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        related_royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        return sum(related_royalties)

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return[contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        related_authors = []
        for contract in Contract.all:
            if contract.book == self:
                related_authors.append(contract.author)
        return related_authors
    
    def sign_contract(self, author, date, royalties):
        contract = Contract(author, self, date, royalties)
        return contract
    
class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author should be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book should be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date should be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties should be an integer.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        sorted_contracts = sorted(cls.all, key=lambda x: x.date)
        contracts_with_date = [contract for contract in sorted_contracts if contract.date == date]
        return contracts_with_date



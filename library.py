from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def load_data(self, books_data, members_data):
        self.books = [Book.from_dict(b) for b in books_data]
        self.members = [Member.from_dict(m) for m in members_data]

    def get_data(self):
        return [b.to_dict() for b in self.books], [m.to_dict() for m in self.members]

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def find_book(self, book_id):
        return next((book for book in self.books if book.book_id == book_id), None)

    def find_member(self, member_id):
        return next((m for m in self.members if m.member_id == member_id), None)

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if book and member and not book.is_borrowed:
            book.is_borrowed = True
            member.borrowed_books.append(book.book_id)
            return f"{member.name} borrowed '{book.title}'"
        return "Borrowing failed."

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if book and member and book.book_id in member.borrowed_books:
            book.is_borrowed = False
            member.borrowed_books.remove(book.book_id)
            return f"{member.name} returned '{book.title}'"
        return "Return failed."

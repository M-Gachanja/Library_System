class Member:
    def __init__(self, member_id, name, borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        return Member(data["member_id"], data["name"], data["borrowed_books"])

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"

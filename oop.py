class Book:
    def __init__(self, title, author, genre, pages, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.price = price
        self.current_page = 0

    def read(self, pages):
        if self.current_page + pages <= self.pages:
            self.current_page += pages
            print(f"You read {pages} pages of '{self.title}'. You are now on page {self.current_page}.")
        else:
            print(f"You finished reading '{self.title}'!")
            self.current_page = self.pages

    def get_info(self):
        return (f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, "
                f"Pages: {self.pages}, Price: ${self.price}, Current Page: {self.current_page}")


# Subclass for EBooks
class EBook(Book):
    def __init__(self, title, author, genre, pages, price, file_size, format):
        super().__init__(title, author, genre, pages, price)
        self.file_size = file_size  # in MB
        self.format = format  # e.g., PDF, EPUB

    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size}MB, {self.format})...")

    def get_info(self):
        # Overriding to include eBook-specific attributes
        base_info = super().get_info()
        return f"{base_info}, File Size: {self.file_size}MB, Format: {self.format}"


# Example usage with unique values
book1 = Book("1984", "George Orwell", "Dystopian", 328, 15.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 281, 10.99)
ebook = EBook("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 180, 5.99, 2, "EPUB")

# Display information for each book
print(book1.get_info())
print(book2.get_info())
print(ebook.get_info())

# Perform actions on each book
book1.read(50)
book2.read(300)  # Exceeds total pages
ebook.download()
ebook.read(100)
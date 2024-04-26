#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Book:
    
    def __init__(self):
        self.filename = "books.txt"
        self.books = {}
        self.load_books()
       
    # Get data from file
    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                self.books = {}
                for line in lines:
                    book_id, book_name, author_name, num_copies = line.strip().split(',')
                    self.books[book_id] = {
                        'name': book_name,
                        'author': author_name,
                        'copies': int(num_copies)
                    }
        except FileNotFoundError:
            self.save_books()  
    
    # Save data to file
    def save_books(self):
        with open(self.filename, 'w') as file:
            for book_id, book_info in self.books.items():
                file.write(f"{book_id},{book_info['name']},{book_info['author']},{book_info['copies']}\n")
    
    
    def add_book(self, book_id, book_name, author_name, num_copies):
        if(isinstance(int(num_copies), int) and isinstance(int(book_id), int)):
            self.books[book_id] = {
                'name': book_name,
                'author': author_name,
                'copies': num_copies
            }
            self.save_books()
            print(" ")
            print("Book added successfully.")
        else:
            print("Number of copies/Book ID must be integers.")
            print(" ")
            print("Book not added.")
            return
    
    
    def view_all(self):
            print("""
                            All Books

    Book ID     Book     Auther     No. of Books """)
            for book_id, book_info in self.books.items():
                print(f""" 
    {book_id}          {book_info['name']}     {book_info['author']}      {book_info['copies']}""")
    
    
    def check_book(self, bookId):
        print(" ")
        print("Checking particular book...")
        print(" ")
        if book_id in self.books:
            book_info = self.books[book_id]
            print("""
                            Book found...

    Book ID     Book     Auther     No. of Books """)

            print(f""" 
    {book_id}          {book_info['name']}     {book_info['author']}      {book_info['copies']}""")
        else:
            print("Book ID not found...")
    
    
    def update(self, book_id, field, new_value):
        if field == 'name' or field == 'author':
            self.books[book_id][field] = new_value
        elif field == 'copies':
            try:
                self.books[book_id][field] = int(new_value)
            except ValueError:
                print("Number of copies must be an integer.")
                print(" ")
                print("Book not updated.")
                return
        else:
            print(" ")
            print("Invalid field to update...")
            return
        self.save_books()
        print(" ")
        print("Book updated successfully.")
        
        
    def delete(self, book_id):
        
        if book_id in self.books:
            del self.books[book_id]
            self.save_books()
            print(" ")
            print("Book deleted successfully.")
        else:
            print(" ")
            print("Book ID not found...")


# In[ ]:


book = Book()
while True:
    print("""
                                    Control Panel
    1. Add Book
    2. Display Books
    3. Check Particular Book
    4. Update Book
    5. Delete Book
    6. Exit """)

    # Get user choice
    choice = input("Enter your choice: ")

    if choice == '1':
        c = 'y';

        while(c == 'y'):
            book_id = input("Enter book ID: ")
            book_name = input("Enter book name: ")
            author_name = input("Enter author name: ")
            num_copies = input("Enter number of copies: ")
            book.add_book(book_id, book_name, author_name, num_copies)
            print(" ")
            c = input("Want to add another book? (y/n): ")

    elif choice == '2':
        book.view_all()
        
    elif choice == '3':
        book_id = input("Enter book ID to check: ")
        book.check_book(book_id)
        
    elif choice == '4':
        book_id = input("Enter book ID to update: ")
        
        if book_id in book.books:
            field = input("Enter field to update (name/author/copies): ")
            
            if field == 'name' or field == 'author':
                new_value = input("Enter new value: ")
                book.update(book_id, field, new_value)
            elif field == 'copies':
                new_value = input("Enter new value: ")
                
                if(isinstance(int(new_value), int)):
                    book.update(book_id, field, new_value)
                else:
                    print("Number of copies must be an integer.")
                    print(" ")
                    print("Book not updated.")
            else:
                print(" ")
                print("Invalid field to update...")
        else:
            print(" ")
            print("Book ID not found...")          
            
    elif choice == '5':
        book_id = input("Enter book ID to delete: ")
        book.delete(book_id)
        
    elif choice == '6':
        print("Exiting...")
        print("Bye...")
        break
        
    else:
        print("Invalid choice. Please enter a valid option (1-6).")


# In[ ]:





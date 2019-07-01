# Base Class
class Person:
    # class private variable
    __count = 0

    # default constructor _
    def __init__(self, name, email):
        self.name = name
        self.email = email # usage of self
        Person.__count += 1

    def dispDetails(self):
        print("Name: ", self.name,"Email: ", self.email)

    def displayCount(self):
        print("Total Count:", Person.__count)


# Class inherited
class Student(Person):
    # default constructor __init__
    def __init__(self, name, email, class_id):
        Person.__init__(self, name, email)
        self.class_id = class_id

    def dispDetails(self):
        #Person.dispDetails(self)
        print("Student Name: ",self.name,"Student Email: ",self.email,"Class Id: ",self.class_id)


class Faculty(Person):
    # default constructor __init__
    def __init__(self, name, email, emp_id):
        # use of super call
        super().__init__(name, email)
        self.emp_id = emp_id

    def dispDetails(self):
        print("Faculty_Name: " , self.name, "Faculty_Email: " , self.email ,"Employee ID: ",self.emp_id)


class Book():
    # default constructor __init__
    def __init__(self, name, author, id):
        self.book_name = name
        self.author = author
        self.id = id

    def dispDetails(self):
        print("Book_Name: ", self.book_name,"Author: ", self.author,"Book_ID: ", self.id)

#multiple inheritance
class Library(Student, Book, Faculty):
    def __init__(self, name, email, student_id, bookname, author, id):
        Student.__init__(self, name, email, student_id)
        Book.__init__(self, bookname, author, id)

    def dispDetails(self):
        Student.dispDetails(self)
        Book.dispDetails(self)


# Instances of above classes
student1 = Student('Dwarkamoye', 'abc@gmail.com', 25)
student2 = Student('Bhavaz', 'def@yahoo.com', 1)
student3 = Student('Kruthika', 'ghi@yahoo.com', 3)
faculty1 = Faculty('Sariah', 'sariah@gmail.com', 123)
faculty2 = Faculty('Gharib', 'gharib@yahoo.com', 456)
book1 = Book('Learning Python', 'Python Jr.', 6549)
book2 = Book('Fundamentals of Deep Learning', 'Deep Learning Sr.', 3216)

print('--------- Person Count ---------')
Person.displayCount(Person)

borrow_book1 = Library('Dwarka', 'abc@gmail.com', 25, 'Learning Python','Python Jr.', 6549)

print('--------- Student Details ---------')
student1.dispDetails()
student2.dispDetails()
student3.dispDetails()

print('-------- Faculty Details ---------')
faculty1.dispDetails()

print('-------- Book Details --------------')
book1.dispDetails()
book2.dispDetails()

print('----------Borrowing book details --------------')
borrow_book1.dispDetails()


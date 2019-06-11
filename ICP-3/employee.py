class Employee:
  count = 0
  totalSal = 0

  def __init__(self, name, family, salary, department):
    self.name = name
    self.family = family
    self.salary = salary
    self.department = department
    Employee.count += 1
    Employee.totalSal += salary

  def average(self):
    return self.totalSal/self.count

  def display(self):
    print("Name: ", self.name, " Family :", self.family, " Salary :", self.salary, " Department :",self.department)


class FulltimeEmployee(Employee):
    def __init__(self, n, f, s, d):
        Employee.__init__(self, n, f, s, d)


e1 = Employee("John", "Family", 100, "Finance")
e2 = Employee("Peter", "Family1", 200, "Health")
e3 = FulltimeEmployee("Dwarka", "Family2", 500, "Home")
e4 = FulltimeEmployee("Dwarka1", "Family3", 700, "Home1")
e5 = FulltimeEmployee("Dwarka2", "Family4", 900, "Home2")
print(e3.average())
print(e5.average())
e5.display()


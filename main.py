#############
#tsk1
#######################

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")


account1 = BankAccount("123456", "Alice Smith")
account2 = BankAccount("987654", "Bob Johnson")


account1.deposit(500)
account1.withdraw(200)

account2.deposit(1000)
account2.withdraw(1500)
account2.withdraw(300)


print(f"Final balance for {account1.account_holder}: ${account1.balance:.2f}")
print(f"Final balance for {account2.account_holder}: ${account2.balance:.2f}")

#############
#tsk2
#######################

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} has successfully enrolled in {course}.")
        else:
            print(f"{self.name} is already enrolled in {course}.")

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Enrolled Courses:", ', '.join(self.courses) if self.courses else "No courses enrolled.")

student1 = Student("Alice Brown", "11")
student2 = Student("Daniel Green", "12")

student1.enroll("Mathematics")
student1.enroll("Physics")
student2.enroll("Biology")
student2.enroll("Chemistry")
student2.enroll("Biology")

student1.display_info()
student2.display_info()

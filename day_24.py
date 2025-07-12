""" Day 24: Class Attributes and Methods - Advanced Features """

# =============================================================================
# CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# =============================================================================

class Student:
    """A Student class demonstrating class vs instance attributes"""
    
    # Class attributes (shared by all instances)
    school_name = "Python Learning Academy"
    total_students = 0
    
    def __init__(self, name, age, grade):
        """Initialize a Student with name, age, and grade"""
        # Instance attributes (unique to each object)
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []
        
        # Increment class attribute when new student is created
        Student.total_students += 1
    
    # Instance methods
    def add_course(self, course):
        """Add a course to the student's course list"""
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course}")
        else:
            print(f"{self.name} is already enrolled in {course}")
    
    def get_info(self):
        """Get detailed information about the student"""
        courses_str = ", ".join(self.courses) if self.courses else "No courses yet"
        return f"Student: {self.name} (Age: {self.age}, Grade: {self.grade})\nCourses: {courses_str}"
    
    def study(self, subject):
        """Method for studying a subject"""
        print(f"{self.name} is studying {subject} 📚")
    
    # Class methods (work with class attributes)
    @classmethod
    def get_school_info(cls):
        """Get information about the school"""
        return f"School: {cls.school_name} | Total Students: {cls.total_students}"
    
    @classmethod
    def create_freshman(cls, name, age):
        """Factory method to create a freshman student"""
        return cls(name, age, "9th Grade")
    
    # Static methods (utility functions related to the class)
    @staticmethod
    def calculate_gpa(grades):
        """Calculate GPA from a list of grades"""
        if not grades:
            return 0.0
        
        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        total_points = sum(grade_points.get(grade.upper(), 0.0) for grade in grades)
        return round(total_points / len(grades), 2)
    
    @staticmethod
    def is_passing_grade(grade):
        """Check if a grade is passing"""
        return grade.upper() in ['A', 'B', 'C', 'D']
    
    def __str__(self):
        """String representation of the Student"""
        return f"{self.name} ({self.grade})"


# =============================================================================
# PRACTICAL EXAMPLE: BANK ACCOUNT CLASS
# =============================================================================

class BankAccount:
    """A BankAccount class demonstrating encapsulation and data protection"""
    
    # Class attribute
    bank_name = "Python Bank"
    interest_rate = 0.02  # 2% annual interest
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize a bank account"""
        self.account_holder = account_holder
        self._balance = initial_balance  # Protected attribute (convention)
        self._transaction_history = []   # Protected attribute
        
        # Record initial deposit if any
        if initial_balance > 0:
            self._transaction_history.append(f"Initial deposit: ${initial_balance:.2f}")
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            print("Deposit amount must be positive!")
            return False
        
        self._balance += amount
        self._transaction_history.append(f"Deposit: +${amount:.2f}")
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        
        if amount > self._balance:
            print(f"Insufficient funds! Balance: ${self._balance:.2f}")
            return False
        
        self._balance -= amount
        self._transaction_history.append(f"Withdrawal: -${amount:.2f}")
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True
    
    def get_balance(self):
        """Get current account balance (read-only access)"""
        return self._balance
    
    def get_transaction_history(self):
        """Get transaction history"""
        if not self._transaction_history:
            return "No transactions yet."
        
        history = f"\n=== Transaction History for {self.account_holder} ===\n"
        for i, transaction in enumerate(self._transaction_history, 1):
            history += f"{i}. {transaction}\n"
        history += f"Current Balance: ${self._balance:.2f}"
        return history
    
    @classmethod
    def get_bank_info(cls):
        """Get bank information"""
        return f"Bank: {cls.bank_name} | Interest Rate: {cls.interest_rate * 100}%"
    
    def __str__(self):
        """String representation of the BankAccount"""
        return f"{self.account_holder}'s Account - Balance: ${self._balance:.2f}"


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_advanced_classes():
    """Demonstrate advanced class features"""
    
    print("=== STUDENT CLASS DEMONSTRATION ===")
    
    # Create students using different methods
    alice = Student("Alice Johnson", 16, "10th Grade")
    bob = Student.create_freshman("Bob Smith", 15)  # Using class method
    charlie = Student("Charlie Brown", 17, "11th Grade")
    
    # Add courses
    alice.add_course("Mathematics")
    alice.add_course("Physics")
    alice.add_course("Chemistry")
    
    bob.add_course("English")
    bob.add_course("History")
    
    # Display student information
    print(f"\n{alice.get_info()}")
    print(f"\n{bob.get_info()}")
    
    # Use class method
    print(f"\n{Student.get_school_info()}")
    
    # Use static methods
    alice_grades = ['A', 'B', 'A', 'B']
    bob_grades = ['B', 'C', 'B', 'A']
    
    print(f"\nAlice's GPA: {Student.calculate_gpa(alice_grades)}")
    print(f"Bob's GPA: {Student.calculate_gpa(bob_grades)}")
    print(f"Is 'A' a passing grade? {Student.is_passing_grade('A')}")
    print(f"Is 'F' a passing grade? {Student.is_passing_grade('F')}")
    
    print("\n" + "="*60)
    
    # Bank Account demonstration
    print("\n=== BANK ACCOUNT DEMONSTRATION ===")
    
    # Create accounts
    account1 = BankAccount("Alice Johnson", 1000)
    account2 = BankAccount("Bob Smith", 500)
    
    print(f"\n{BankAccount.get_bank_info()}")
    print(f"\nInitial accounts:")
    print(f"Account 1: {account1}")
    print(f"Account 2: {account2}")
    
    # Perform transactions
    print(f"\n--- Performing Transactions ---")
    account1.deposit(250)
    account1.withdraw(100)
    account1.withdraw(2000)  # This should fail
    
    account2.deposit(300)
    account2.withdraw(150)
    
    # Show final balances and history
    print(f"\nFinal balances:")
    print(f"Account 1: {account1}")
    print(f"Account 2: {account2}")
    
    print(account1.get_transaction_history())


# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================

def print_concepts():
    """Print key concepts learned today"""
    print("\n=== KEY CONCEPTS LEARNED ===")
    print("1. Class Attributes: Shared by all instances of a class")
    print("2. Instance Attributes: Unique to each object")
    print("3. Class Methods (@classmethod): Work with class attributes")
    print("4. Static Methods (@staticmethod): Utility functions related to class")
    print("5. Encapsulation: Using _ prefix for protected attributes")
    print("6. Factory Methods: Class methods that create instances")
    print("7. Data Protection: Controlling access to class data")


# Run the demonstration
if __name__ == "__main__":
    demonstrate_advanced_classes()
    print_concepts()

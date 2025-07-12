""" Day 17: Scope and Global vs Local Variables """

# ========== GLOBAL VARIABLES ==========

global_counter = 0
global_message = "This is a global variable"

print("=== Global Variables ===")
print(f"Global counter: {global_counter}")
print(f"Global message: {global_message}")


# ========== LOCAL SCOPE ==========

def local_scope_demo():
    """Demonstrates local variable scope"""
    local_variable = "This exists only inside the function"
    local_counter = 100
    
    print(f"\nInside function - Local variable: {local_variable}")
    print(f"Inside function - Local counter: {local_counter}")
    print(f"Inside function - Global message: {global_message}")

local_scope_demo()

# This would cause an error if uncommented:
# print(local_variable)  # NameError: name 'local_variable' is not defined


# ========== GLOBAL KEYWORD ==========

def modify_global():
    """Demonstrates using global keyword to modify global variables"""
    global global_counter, global_message
    
    global_counter += 1
    global_message = "Modified by function"
    
    print(f"\nInside modify_global() - Counter: {global_counter}")
    print(f"Inside modify_global() - Message: {global_message}")

print("\n=== Modifying Global Variables ===")
print(f"Before function call - Counter: {global_counter}")
modify_global()
print(f"After function call - Counter: {global_counter}")
print(f"After function call - Message: {global_message}")


# ========== NONLOCAL KEYWORD ==========

def outer_function():
    """Demonstrates nonlocal keyword in nested functions"""
    outer_variable = "I'm in the outer function"
    
    def inner_function():
        nonlocal outer_variable
        outer_variable = "Modified by inner function"
        print(f"Inside inner function: {outer_variable}")
    
    print(f"Before inner function call: {outer_variable}")
    inner_function()
    print(f"After inner function call: {outer_variable}")

print("\n=== Nonlocal Keyword ===")
outer_function()


# ========== SCOPE RESOLUTION (LEGB RULE) ==========
# Local -> Enclosing -> Global -> Built-in

name = "Global Alice"  # Global scope

def enclosing_function():
    name = "Enclosing Bob"  # Enclosing scope
    
    def local_function():
        name = "Local Charlie"  # Local scope
        print(f"Local scope: {name}")
        
        # Accessing built-in function
        print(f"Length of name: {len(name)}")  # len is built-in
    
    def access_enclosing():
        print(f"Enclosing scope: {name}")
    
    def access_global():
        global name
        print(f"Global scope: {name}")
    
    print("\n=== LEGB Rule Demonstration ===")
    local_function()
    access_enclosing()
    access_global()

enclosing_function()


# ========== PRACTICAL EXAMPLES ==========

class Counter:
    """Class demonstrating different types of variables"""
    class_counter = 0  # Class variable (shared among all instances)
    
    def __init__(self):
        Counter.class_counter += 1
        self.instance_counter = 0  # Instance variable
    
    def increment(self):
        self.instance_counter += 1
        return self.instance_counter
    
    @classmethod
    def get_total_instances(cls):
        return cls.class_counter

def banking_example():
    """Practical example of scope in a banking system"""
    bank_name = "Python Bank"  # Local to this function
    
    def create_account(initial_balance=0):
        balance = initial_balance  # Enclosing scope for nested functions
        
        def deposit(amount):
            nonlocal balance
            if amount > 0:
                balance += amount
                print(f"Deposited ${amount}. New balance: ${balance}")
            else:
                print("Invalid deposit amount")
        
        def withdraw(amount):
            nonlocal balance
            if 0 < amount <= balance:
                balance -= amount
                print(f"Withdrew ${amount}. New balance: ${balance}")
            else:
                print("Invalid withdrawal amount or insufficient funds")
        
        def get_balance():
            return balance
        
        def get_bank_info():
            print(f"Bank: {bank_name}")
            print(f"Current balance: ${balance}")
        
        return {
            'deposit': deposit,
            'withdraw': withdraw,
            'balance': get_balance,
            'info': get_bank_info
        }
    
    return create_account

print("\n=== Practical Banking Example ===")
bank = banking_example()
account = bank(1000)  # Create account with $1000

account['info']()
account['deposit'](500)
account['withdraw'](200)
account['info']()


# ========== VARIABLE SHADOWING ==========

x = "Global x"

def shadowing_example():
    x = "Local x"  # This shadows the global x
    print(f"Inside function: {x}")
    
    def nested():
        x = "Nested x"  # This shadows the enclosing x
        print(f"Inside nested function: {x}")
    
    nested()
    print(f"Back in outer function: {x}")

print("\n=== Variable Shadowing ===")
print(f"Global x: {x}")
shadowing_example()
print(f"Global x after function: {x}")
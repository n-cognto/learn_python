""" Day 23: Object-Oriented Programming - Classes & Objects """

# =============================================================================
# BASIC CLASS DEFINITION
# =============================================================================

class Person:
    """A simple Person class to demonstrate basic OOP concepts"""
    
    def __init__(self, name, age):
        """Initialize a Person with name and age"""
        self.name = name
        self.age = age
    
    def greet(self):
        """Method to greet someone"""
        print(f"Hi, my name is {self.name} and I'm {self.age} years old.")
    
    def have_birthday(self):
        """Method to increase age by 1"""
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age} years old.")
    
    def __str__(self):
        """String representation of the Person"""
        return f"Person(name='{self.name}', age={self.age})"


# =============================================================================
# PRACTICAL EXAMPLE: CAR CLASS
# =============================================================================

class Car:
    """A Car class to demonstrate attributes and methods"""
    
    def __init__(self, brand, model, year, price):
        """Initialize a Car with brand, model, year, and price"""
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.is_running = False
    
    def start_engine(self):
        """Start the car engine"""
        if not self.is_running:
            self.is_running = True
            print(f"The {self.brand} {self.model} engine is now running!")
        else:
            print(f"The {self.brand} {self.model} is already running.")
    
    def stop_engine(self):
        """Stop the car engine"""
        if self.is_running:
            self.is_running = False
            print(f"The {self.brand} {self.model} engine has been stopped.")
        else:
            print(f"The {self.brand} {self.model} is already stopped.")
    
    def get_info(self):
        """Get detailed information about the car"""
        status = "running" if self.is_running else "stopped"
        return f"{self.year} {self.brand} {self.model} - ${self.price:,} - Engine: {status}"
    
    def __str__(self):
        """String representation of the Car"""
        return f"{self.year} {self.brand} {self.model}"


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_classes():
    """Demonstrate how to use classes and objects"""
    
    print("=== CREATING AND USING OBJECTS ===")
    
    # Create Person objects
    alice = Person("Alice", 25)
    bob = Person("Bob", 30)
    
    # Use object methods
    alice.greet()
    bob.greet()
    
    # Modify object state
    alice.have_birthday()
    
    print(f"\nAlice: {alice}")
    print(f"Bob: {bob}")
    
    print("\n" + "="*50)
    
    # Create Car objects
    car1 = Car("Toyota", "Camry", 2022, 25000)
    car2 = Car("BMW", "X5", 2023, 65000)
    
    print("\n=== CAR DEMONSTRATION ===")
    print(f"Car 1: {car1.get_info()}")
    print(f"Car 2: {car2.get_info()}")
    
    # Start engines
    car1.start_engine()
    car2.start_engine()
    
    print(f"\nAfter starting engines:")
    print(f"Car 1: {car1.get_info()}")
    print(f"Car 2: {car2.get_info()}")
    
    # Stop one engine
    car1.stop_engine()
    print(f"\nAfter stopping Car 1:")
    print(f"Car 1: {car1.get_info()}")


# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================

def print_concepts():
    """Print key OOP concepts learned today"""
    print("\n=== KEY CONCEPTS LEARNED ===")
    print("1. Class: A blueprint for creating objects")
    print("2. Object: An instance of a class")
    print("3. __init__: Constructor method to initialize objects")
    print("4. Attributes: Variables that store object data")
    print("5. Methods: Functions that belong to a class")
    print("6. self: Reference to the current object instance")
    print("7. __str__: Method to define string representation")


# Run the demonstration
if __name__ == "__main__":
    demonstrate_classes()
    print_concepts()
""" Day 25: Inheritance and Polymorphism """

# =============================================================================
# BASIC INHERITANCE
# =============================================================================

class Animal:
    """Base Animal class demonstrating inheritance concepts"""
    
    def __init__(self, name, species, age):
        """Initialize an Animal with name, species, and age"""
        self.name = name
        self.species = species
        self.age = age
        self.is_sleeping = False
    
    def speak(self):
        """Base method for animal sounds - to be overridden"""
        print(f"{self.name} makes a sound")
    
    def sleep(self):
        """Method for animal sleeping"""
        if not self.is_sleeping:
            self.is_sleeping = True
            print(f"{self.name} is now sleeping 😴")
        else:
            print(f"{self.name} is already sleeping")
    
    def wake_up(self):
        """Method for animal waking up"""
        if self.is_sleeping:
            self.is_sleeping = False
            print(f"{self.name} has woken up!")
        else:
            print(f"{self.name} is already awake")
    
    def get_info(self):
        """Get information about the animal"""
        status = "sleeping" if self.is_sleeping else "awake"
        return f"{self.name} is a {self.age}-year-old {self.species} and is currently {status}"
    
    def __str__(self):
        """String representation of the Animal"""
        return f"{self.name} the {self.species}"


# =============================================================================
# INHERITANCE WITH METHOD OVERRIDING
# =============================================================================

class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, age, breed):
        """Initialize a Dog with name, age, and breed"""
        # Call parent constructor
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.tricks = []
    
    def speak(self):
        """Override the speak method for dogs"""
        print(f"{self.name} barks: Woof! Woof! 🐕")
    
    def learn_trick(self, trick):
        """Method specific to dogs"""
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows {trick}")
    
    def perform_trick(self, trick):
        """Perform a learned trick"""
        if trick in self.tricks:
            print(f"{self.name} performs {trick}! 🎪")
        else:
            print(f"{self.name} doesn't know {trick} yet. Teach them first!")
    
    def get_info(self):
        """Override get_info to include breed and tricks"""
        base_info = super().get_info()
        tricks_info = f"Tricks: {', '.join(self.tricks)}" if self.tricks else "No tricks yet"
        return f"{base_info}\nBreed: {self.breed}\n{tricks_info}"


class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def __init__(self, name, age, color):
        """Initialize a Cat with name, age, and color"""
        super().__init__(name, "Cat", age)
        self.color = color
        self.lives_remaining = 9
    
    def speak(self):
        """Override the speak method for cats"""
        print(f"{self.name} meows: Meow! Meow! 🐱")
    
    def purr(self):
        """Method specific to cats"""
        print(f"{self.name} is purring contentedly... *purr purr* 😺")
    
    def use_life(self):
        """Use one of the cat's nine lives"""
        if self.lives_remaining > 0:
            self.lives_remaining -= 1
            print(f"{self.name} used a life! {self.lives_remaining} lives remaining")
        else:
            print(f"{self.name} has no lives left!")
    
    def get_info(self):
        """Override get_info to include color and lives"""
        base_info = super().get_info()
        return f"{base_info}\nColor: {self.color}\nLives remaining: {self.lives_remaining}"


class Bird(Animal):
    """Bird class inheriting from Animal"""
    
    def __init__(self, name, age, wingspan):
        """Initialize a Bird with name, age, and wingspan"""
        super().__init__(name, "Bird", age)
        self.wingspan = wingspan
        self.can_fly = True
    
    def speak(self):
        """Override the speak method for birds"""
        print(f"{self.name} chirps: Tweet! Tweet! 🐦")
    
    def fly(self):
        """Method specific to birds"""
        if self.can_fly and not self.is_sleeping:
            print(f"{self.name} is flying with a {self.wingspan}cm wingspan! 🕊️")
        elif self.is_sleeping:
            print(f"{self.name} can't fly while sleeping!")
        else:
            print(f"{self.name} cannot fly")
    
    def get_info(self):
        """Override get_info to include wingspan"""
        base_info = super().get_info()
        flight_status = "can fly" if self.can_fly else "cannot fly"
        return f"{base_info}\nWingspan: {self.wingspan}cm\nFlight: {flight_status}"


# =============================================================================
# POLYMORPHISM DEMONSTRATION
# =============================================================================

def animal_care_center(animals):
    """Demonstrate polymorphism with different animal types"""
    print("=== ANIMAL CARE CENTER ===")
    print("Daily routine for all animals:\n")
    
    for animal in animals:
        print(f"--- Caring for {animal} ---")
        
        # Polymorphism: same method call, different behavior
        animal.speak()  # Each animal speaks differently
        
        # Common methods work for all animals
        if animal.is_sleeping:
            animal.wake_up()
        
        # Type-specific actions using isinstance()
        if isinstance(animal, Dog):
            if animal.tricks:
                trick = animal.tricks[0]  # Perform first trick
                animal.perform_trick(trick)
        elif isinstance(animal, Cat):
            animal.purr()
        elif isinstance(animal, Bird):
            animal.fly()
        
        print(f"Info: {animal.get_info()}")
        animal.sleep()
        print()


# =============================================================================
# ADVANCED INHERITANCE EXAMPLE
# =============================================================================

class Vehicle:
    """Base Vehicle class"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        """Start the vehicle"""
        if not self.is_running:
            self.is_running = True
            print(f"The {self.brand} {self.model} has started")
        else:
            print(f"The {self.brand} {self.model} is already running")
    
    def stop(self):
        """Stop the vehicle"""
        if self.is_running:
            self.is_running = False
            print(f"The {self.brand} {self.model} has stopped")
        else:
            print(f"The {self.brand} {self.model} is already stopped")
    
    def honk(self):
        """Base honk method"""
        print("Honk! Honk!")


class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    
    def honk(self):
        """Override honk for cars"""
        print("Beep! Beep! 🚗")
    
    def open_trunk(self):
        """Car-specific method"""
        print(f"Opening trunk of {self.brand} {self.model}")


class Motorcycle(Vehicle):
    """Motorcycle class inheriting from Vehicle"""
    
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
    
    def honk(self):
        """Override honk for motorcycles"""
        print("Beep! Beep! 🏍️")
    
    def wheelie(self):
        """Motorcycle-specific method"""
        if self.is_running:
            print(f"The {self.brand} {self.model} is doing a wheelie!")
        else:
            print("Start the motorcycle first!")


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_inheritance():
    """Demonstrate inheritance and polymorphism concepts"""
    
    print("=== CREATING ANIMALS ===")
    
    # Create different animals
    buddy = Dog("Buddy", 3, "Golden Retriever")
    whiskers = Cat("Whiskers", 2, "Orange")
    tweety = Bird("Tweety", 1, 15)
    
    # Teach the dog some tricks
    buddy.learn_trick("sit")
    buddy.learn_trick("roll over")
    buddy.learn_trick("fetch")
    
    # Display individual animal info
    print("\nIndividual animal demonstrations:")
    print("--- Buddy the Dog ---")
    buddy.speak()
    buddy.perform_trick("sit")
    print(buddy.get_info())
    
    print("\n--- Whiskers the Cat ---")
    whiskers.speak()
    whiskers.purr()
    whiskers.use_life()
    print(whiskers.get_info())
    
    print("\n--- Tweety the Bird ---")
    tweety.speak()
    tweety.fly()
    print(tweety.get_info())
    
    print("\n" + "="*60)
    
    # Demonstrate polymorphism
    animals = [buddy, whiskers, tweety]
    animal_care_center(animals)
    
    print("="*60)
    
    # Vehicle inheritance example
    print("\n=== VEHICLE INHERITANCE ===")
    
    car = Car("Toyota", "Camry", 2023, 4)
    bike = Motorcycle("Harley", "Sportster", 2022, 883)
    
    vehicles = [car, bike]
    
    print("Testing polymorphism with vehicles:")
    for vehicle in vehicles:
        vehicle.start()
        vehicle.honk()  # Different honk sounds
        
        # Type-specific actions
        if isinstance(vehicle, Car):
            vehicle.open_trunk()
        elif isinstance(vehicle, Motorcycle):
            vehicle.wheelie()
        
        vehicle.stop()
        print()


# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================

def print_concepts():
    """Print key inheritance and polymorphism concepts"""
    print("\n=== KEY CONCEPTS LEARNED ===")
    print("1. Inheritance: Child classes inherit from parent classes")
    print("2. super(): Call parent class methods from child classes")
    print("3. Method Overriding: Child classes can redefine parent methods")
    print("4. Polymorphism: Same interface, different implementations")
    print("5. isinstance(): Check if object is instance of specific class")
    print("6. Code Reusability: Inherit common functionality")
    print("7. Method Resolution Order (MRO): How Python finds methods")


# Run the demonstration
if __name__ == "__main__":
    demonstrate_inheritance()
    print_concepts()

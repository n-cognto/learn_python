# # 4. Build a shopping list program that:
# #    - Takes items as comma-separated input
# #    - Displays them as a numbered list
# #    - Calculates total if prices are provided

# def shopping_list():
#     items = input("Enter items (comma-separated): ").split(',')
#     items = [item.strip() for item in items]  # Clean up whitespace
#     print("\nShopping List:")
#     for i, item in enumerate(items, start=1):  #enumarate outputs a list of tuples
#         print(f"{i}. {item}")

#     prices = input("Enter prices for the items (comma-separated, or leave blank): ")
#     if prices:
#         prices = [float(price.strip()) for price in prices.split(',')] #cleaning process
#         total = sum(prices)
#         print(f"Total cost: ${total:.2f}")
#     else:
#         print("No prices provided.")
# # Shopping List Program
# shopping_list()

# # Recursive function
# # def factorial(n):
# #     """Calculate factorial of n using recursion."""
# #     if n < 0:
# #         raise ValueError("Factorial is not defined for negative numbers.")
# #     elif n == 0 or n == 1:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)


# Scope and Global vs Local Variables

# local -> Accessible only within the function where it is defined
# global -> Accessible throughout the module, can be modified using the `global` keyword

# Global Variables
outer_variable = "Outside Outer Variable"

def inner_function():
    global outer_variable 
    outer_variable = "Modified by inner function"
    print(f"Inside inner function: {outer_variable}")


print(f"Before inner function call: {outer_variable}") #global
inner_function() #Modify the outer_variable locally
print(f"After inner function call: {outer_variable}")  #global 
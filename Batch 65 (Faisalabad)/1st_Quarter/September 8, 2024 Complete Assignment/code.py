# Create a function that inserts a value at a specified index in an array and returns the updated array.

def insert_value(arr, index, value):
    arr.insert(index, value)
    return arr

my_array = [1, 2, 3, 5]
updated_array = insert_value(my_array, 3, 4)
print(updated_array)


# Create a shopping cart program with functions to add, remove, and update item quantities. Print the cart contents after each operation.

def add_items(cart, item):
    cart.append(item)
    print(f"\n{item} added to your cart")
    return cart

def remove_items(cart, item):
    if item in cart:
        cart.remove(item)
        print(f"\n{item} removed from your cart")
    else:
        print(f"\n{item} not found in cart")
    return cart

def update_items(cart, new_item, replace_item):
    if replace_item in cart:
        index = cart.index(replace_item)
        cart[index] = new_item
        print(f"\n{replace_item} changed to {new_item}")
    else:
        print(f"\n{replace_item} not found in the cart.")
    return cart

print("\n\n")
print("        =======================")
print("          Online Shopping App")
print("        =======================")

cart = []
pin = 1234

while True:
    print("\n-------------------")
    print("1. Add item")
    print("2. Remove item")
    print("3. Change item")
    print("4. print & payment")
    print("5. Exit")
    print("-------------------")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        item = input("\n--> Enter item to add: ")
        print("__________________________")
        cart = add_items(cart, item)
        print(cart)
        print("__________________________")

    elif choice == "2":
        item = input("\n--> Enter item to remove: ")
        print("__________________________")
        cart = remove_items(cart, item)
        print(cart)
        print("__________________________")

    elif choice == "3":
        replace_item = input("\n--> Enter item to replace: ")
        new_item = input("--> Enter new item: ")
        print("__________________________")
        cart = update_items(cart, new_item, replace_item)
        print(cart)
        print("__________________________")

    elif choice == "4":
        print(cart)
        print("__________________________")
        print("\t\n--> Payment successful received!")
        print("__________________________")

    elif choice == "5":
        print("Exiting...")
        exit()
        break

    else:
        print("Option not found!")


# *Write a program* that uses a while loop to print the first 25 integers.

i = 1
while i <= 25:
    print(i)
    i += 1

# *Write a program* that uses a while loop to print the first 10 even numbers.

    count = 1
    num = 2

    while count <= 10:
        print(num)
        num += 2
        count += 1

# *Create a function* that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number.

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

number = int(input("Enter a positive integer: "))
print("Factorial of", number, "is", factorial(number))

# *Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.

numbers = [10, -3, 7, -1, 0, 5, -6]
positive_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)

print(positive_numbers)

# *Create a function* that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array.

def sum_of_array(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total

numbers = [4, 7, 2, 9, 6]
print("Sum of the array:", sum_of_array(numbers))

# Implement a program* that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.

def celsius_to_fahrenheit(celsius_temps):
    fahrenheit_temps = []
    i = 0
    while i < len(celsius_temps):
        fahrenheit = (celsius_temps[i] * 9/5) + 32
        fahrenheit_temps.append(fahrenheit)
        i += 1
    return fahrenheit_temps

celsius_temps = []

n = int(input("How many temperatures do you want to convert? "))

i = 0
while i < n:
    temp = float(input(f"Enter temperature {i+1} in Celsius: "))
    celsius_temps.append(temp)
    i += 1

fahrenheit_temps = celsius_to_fahrenheit(celsius_temps)
print("Temperatures in Fahrenheit:", fahrenheit_temps)

# *Write a program* to remove all the odd numbers from an array.

def remove_odd_numbers(numbers):
    # Create a new list to store even numbers
    even_numbers = []
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:  # Check if the number is even
            even_numbers.append(numbers[i])
        i += 1
    return even_numbers

# Example usage
numbers = [10, 15, 22, 33, 40, 55, 60]
filtered_numbers = remove_odd_numbers(numbers)
print("Array after removing odd numbers:", filtered_numbers)


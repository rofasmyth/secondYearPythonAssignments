################################################## LISTS,TUPLES & SETS ##################################################################################################

# Lists
my_list = [1, 2, 3, 4, 5]

# Append an element to the list
my_list.append(6)

# Access elements by index
first_element = my_list[0]
last_element = my_list[-1]

# Slice a list
sliced_list = my_list[1:4]

# Check if an element is in the list
element_exists = 5 in my_list

# Find the index of an element
index_of_3 = my_list.index(3)

# Remove an element by value
my_list.remove(4)

# Tuples
my_tuple = (10, 20, 30, 40, 50)

# Access elements by index
first_element = my_tuple[0]
last_element = my_tuple[-1]

# Sets
my_set = {1, 2, 3, 4, 5}

# Add an element to the set
my_set.add(6)

# Remove an element from the set
my_set.remove(3)

# Check if an element is in the set
element_exists = 5 in my_set

# 2-Dimensional Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements in a 2D list
element_at_2_3 = matrix[1][2]

# Enumerate Function
my_list = ["apple", "banana", "cherry"]
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

############################################ DICTIONARIES ########################################################################################################
# Dictionaries
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Access values by keys
name = my_dict["name"]
age = my_dict["age"]

# Modify values
my_dict["age"] = 31

# Add new key-value pairs
my_dict["country"] = "USA"

# Check if a key exists in the dictionary
key_exists = "city" in my_dict

# Remove a key-value pair
if "country" in my_dict:
    del my_dict["country"]

# Dictionary Iteration
# Iterate through keys
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

# Iterate through key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

############################################## ERRORS AND EXCEPTIONS ###############################################################################################################

# 1. Syntax Error
# Uncomment the following line to see a syntax error
# print("Hello, World"

# 2. Indentation Error
# Uncomment the following lines to see an indentation error
# if True:
# print("Indented incorrectly")

# 3. ZeroDivisionError
try:
    result = 5 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# 4. NameError
try:
    print(variable_that_does_not_exist)
except NameError as e:
    print(f"NameError: {e}")

# 5. TypeError
try:
    result = "5" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# 6. ValueError
try:
    number = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# 7. FileNotFoundError
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# 8. Custom Exception
class CustomException(Exception):
    pass

try:
    raise CustomException("This is a custom exception")
except CustomException as e:
    print(f"Custom Exception: {e}")

# 9. Handling Multiple Exceptions
try:
    value = 1 / 0
except (ZeroDivisionError, NameError, TypeError) as e:
    print(f"Multiple Exceptions: {e}")

# 10. Finally Block
try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
finally:
    print("Finally block executed")

# 11. Using 'else' with try-except
try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
else:
    print("No exceptions occurred")

# 12. Raising Exceptions
try:
    number = int(input("Enter a positive integer: "))
    if number < 0:
        raise ValueError("Input must be a positive integer")
except ValueError as e:
    print(f"ValueError: {e}")

# 13. Assertions
age = -5
assert age >= 0, "Age cannot be negative"

print("End of the script")

################################################## JSON & FILE HANDLING ###################################################################################################################
import json

# JSON

# 1. Encoding JSON
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Encode Python dictionary to JSON
json_data = json.dumps(data, indent=4)
print("Encoded JSON:")
print(json_data)

# 2. Decoding JSON
json_string = '{"name": "Alice", "age": 25, "city": "Los Angeles"}'

# Decode JSON string to Python dictionary
parsed_data = json.loads(json_string)
print("\nDecoded JSON:")
print(parsed_data)

# File Handling

# 3. Writing to a File
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.")

# 4. Reading from a File
with open("sample.txt", "r") as file:
    file_contents = file.read()
    print("\nFile Contents:")
    print(file_contents)

# 5. Appending to a File
with open("sample.txt", "a") as file:
    file.write("\nAppending more text.")

# 6. Reading Lines from a File
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("\nLines from File:")
    for line in lines:
        print(line.strip())  # Strip removes the newline character

# String Manipulation: maketrans() and translate()

# 7. Using maketrans() and translate()
text = "Hello, World!"
translation_table = str.maketrans("HW", "hw")

translated_text = text.translate(translation_table)
print("\nTranslated Text:")
print(translated_text)

print("\nEnd of the script")

########################################### SPECIAL OPERATORS AND METHODS ###################################################################################################

# 1. Membership Operators: in and not in
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list.")

if "orange" not in fruits:
    print("Orange is not in the list.")

# 2. Identity Operators: is and is not
x = [1, 2, 3]
y = x

if x is y:
    print("x and y have the same identity.")

# 3. Arithmetic Operators: +, -, *, /, //, %, **
a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
remainder = a % b
exponentiation = a ** b

print(f"\nArithmetic Operators:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")
print(f"Remainder: {remainder}")
print(f"Exponentiation: {exponentiation}")

# 4. Comparison Operators: ==, !=, <, >, <=, >=
if a == b:
    print(f"{a} is equal to {b}")
elif a != b:
    print(f"{a} is not equal to {b}")

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")

# 5. String Concatenation and Repetition
string1 = "Hello"
string2 = "World"

concatenated_string = string1 + " " + string2
repeated_string = string1 * 3

print("\nString Concatenation and Repetition:")
print(f"Concatenated String: {concatenated_string}")
print(f"Repeated String: {repeated_string}")

# 6. Special Methods: len(), type(), str(), int(), float()
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
data_type = type(my_list)
string_representation = str(my_list)
integer_conversion = int("42")
float_conversion = float("3.14")

print("\nSpecial Methods:")
print(f"Length of List: {length}")
print(f"Data Type of List: {data_type}")
print(f"String Representation of List: {string_representation}")
print(f"Integer Conversion: {integer_conversion}")
print(f"Float Conversion: {float_conversion}")

# 7. Tuple Unpacking
coordinates = (5, 8)
x, y = coordinates

print("\nTuple Unpacking:")
print(f"X-coordinate: {x}")
print(f"Y-coordinate: {y}")

print("\nEnd of the script")

########################################################## DUNDER METHODS ###############################################################################################################

# 1. __init__ method for object initialization
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
print(f"Initialized object with value: {obj.value}")

# 2. __str__ method for string representation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

point = Point(3, 5)
print(f"String representation of point: {point}")

# 3. __len__ method to get the length of an object
class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

my_list = MyList([1, 2, 3, 4, 5])
print(f"Length of my_list: {len(my_list)}")

# 4. __getitem__ and __setitem__ methods for indexing and assignment
class MyDictionary:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key, None)

    def __setitem__(self, key, value):
        self.data[key] = value

my_dict = MyDictionary()
my_dict["name"] = "Alice"
print(f"Value for key 'name': {my_dict['name']}")

# 5. __del__ method for object deletion
class MyObject:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Deleting object with name: {self.name}")

obj1 = MyObject("Object 1")
del obj1

# 6. __add__ method for custom addition
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, 2)
result = num1 + num2
print(f"Sum of complex numbers: {result.real} + {result.imag}i")

# 7. __eq__ method for custom equality comparison
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
print(f"Are person1 and person2 equal? {person1 == person2}")

print("\nEnd of the script")

print("Hello, World!")

# var & DataTypes

age = 25
height = 3.5
complex_number = 2 + 3j

name = "john doe"

mylist = [1, 2, 3, 4]

my_tupple = ('apple', 'orange', 'banana')

person = {'name': 'john', 'age': 30}

is_student = True

name = 'riya'

nothing = None

# print(age, type(age))
# print(height, type(height))
# print(complex_number, type(complex_number))
# print(name, type(name))
# print(my_list, type(my_list))
# print(my_tupple, type(my_tupple))
# print(person, type(person))
# print(is_student, type(is_student))
# print(nothing, type(nothing))

# /if-else statement

age = 20 
if age >= 18:
    print("you are adult gadha")
else: 
    print('you are minor gadha')

# for loop


gadhe = ['swapnil','harshal','akshay']

for gadha in gadhe:
    print(gadha)

    # while loop

count = 0
while count < 5:
    print("count:", count)
    count += 1

mylist = [1, 2, 3, 4]

for num in mylist :
    count = 0;
i = 0
while i >= num:

      if num % i == 0 :
        count += 1
        i += 1

if count == 2 :
    print('prime')

num = 7
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")


# functions 

def greetName():
    return "hello, gadhe"

func = greetName()

print(func)

def factorial(n):
    sum=1
    for i in range(1, n+1):
        sum*=i

    return sum      

fact = factorial(5)
print(fact)

numssss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenlist = [x for x in numssss if x % 2 == 0]

print(evenlist)

# OOPS

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} is starting"
    
    def stop(self):
        return f"{self.make} {self.model} is stopping"
    


car1 = Car("Maruti 800", "Your father" , 1004)

print(car1.make)

print(car1.start())



class BankAccount():
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self , amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self , amount):
        self.balance = self.balance - amount
        return self.balance
    
    def get_balance(self ):
        
        return self.balance
    

bA = BankAccount(12345, 600)
print(bA)

bA.deposit(500)

bA.withdraw(400)

print(bA.get_balance())

# fibbonacci
def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]

    if n <= 2:
        return fibonacci_sequence[:n]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Example usage:
n = 10
fib_sequence = generate_fibonacci_sequence(n)
print(fib_sequence)


# Write a program to print the following number pattern using a loop.

def print_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


rows = 5
print_number_pattern(rows)


# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop


def filter_numbers(numbers):
    for num in numbers:
        if num > 500:
            break  
        if num % 5 == 0 and num <= 150:
            print(num)


numbers = [12, 75, 150, 180, 145, 525, 50]


filter_numbers(numbers)



# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.


def append_in_middle(s1, s2):
    middle_index = len(s1) // 2
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3

s1 = "Ault"
s2 = "Kelly"
s3 = append_in_middle(s1, s2)
print(s3)


# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.


def arrange_lowercase_first(s):
    lowercase = ""
    uppercase = ""

    for char in s:
        if char.islower():
            lowercase += char
        else:
            uppercase += char

    arranged_string = lowercase + uppercase
    return arranged_string

str1 = "PyNaTive"
arranged_str = arrange_lowercase_first(str1)
print(arranged_str)




# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.


def add_lists_indexwise(list1, list2):
    combined_list = [x + y for x, y in zip(list1, list2)]
    remaining_items = list1[len(list2):] + list2[len(list1):]
    combined_list += remaining_items
    return combined_list

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result_list = add_lists_indexwise(list1, list2)
print(result_list)



# 6

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

concatenated_list = []

for item1 in list1:
    for item2 in list2:
        concatenated_list.append(item1 + item2)

print(concatenated_list)


# 7

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for item1, item2 in zip(list1, reversed(list2)):
    print(item1, item2)




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

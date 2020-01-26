# Tuples...don't change like in lists
even_numbers = (2, 4, 6, 8, 10, 12)
print(even_numbers[5])

# Functions
def sayhi(name, age) :
    print("Hello " + name + " you are " + age)

sayhi("Nancy", "25")
sayhi("Christine", "27")

# Return Statement
def square(num) :
    return num*num

print(square(8))

def cube(num) :
    return num*num*num  # return breaks out of the function

result = cube(8)   # variable
print(result)


# If Statements
is_single = True

if is_single:
    print("Head on to Tinder app")
else:
    print("Meet your partner")

is_male = False
is_tall = True

if is_male and is_tall:  # or tall
    print("You are either male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are neither male or tall")

# Count number of even and odd numbers from a series of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
count_even = 0
count_odd = 0

for x in numbers:
    if  x % 2 :
        count_even += 1
    else:
        count_odd += 1

print("Number of even numbers is: " + str(count_even))
print("Number of odd numbers is: " + str(count_odd))

def multiplication_or_addition(num1, num2):
    product = num1 * num2
    if (product < 100):
        return product
    else:
        return num1 + num2

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = multiplication_or_addition(number1, number2)
print("The result is ", result)
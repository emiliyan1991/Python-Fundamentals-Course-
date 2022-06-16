def calc(operator, a, b):
    if operator == "multiply":
        return a * b
    if operator == "divide":
        return int(a / b)
    if operator == "add":
        return a + b
    if operator == "subtract":
        return a - b


print(calc(operator=input(), a=int(input()), b=int(input())))


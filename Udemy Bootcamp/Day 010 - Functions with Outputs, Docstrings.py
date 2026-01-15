Functions with Outputs

def my_function():
    return 3 * 2

print(my_function())

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

format_name("terrence", "na")

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formatted_string = format_name("terrence", "na")
print(formatted_string)
# print(format_name("terrence", "na")) 도 가능

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

print(function_2(function_1("tk")))

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't input any values."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("What is your last name?")))

Docstrings

def format_name(f_name, l_name):
    """Take the user name and return it to
    return the title case version."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)


Project - Calculator

# 내답
import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

should_continue = True
first_number = float(input("What's the first number?:  "))
while should_continue == True:
    operation = input("+\n-\n*\n/\nPick an operation:  ")
    next_number = float(input("What's the next number?:  "))

    value = operations[operation](first_number, next_number)
    print(f"{first_number} {operation} {next_number} = {value}")
    more_calculation = input(f"Type 'y' to continue calculating with {value}, or type 'n' to start a new calculation:  ").lower()
    if more_calculation == "y":
        first_number = value
    if more_calculation == "n":
        should_continue = False

# 선생님 답

def calculator():
    print(art.logo)
    first_number = float(input("What's the first number?:  "))

    should_continue = True
    while should_continue == True:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation:  ")
        next_number = float(input("What's the next number?:  "))

        value = operations[operation](first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {value}")
        more_calculation = input(f"Type 'y' to continue calculating with {value}, or type 'n' to start a new calculation:  ").lower()
        if more_calculation == "y":
            first_number = value
        if more_calculation == "n":
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()
# ---------------------------------------------
    while should_continue == True:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation:  ")
# Start - operation symbol input이 dictionary 안에 없으면 다른 메시지 출력하도록 개선
        while operation not in operations:
            for symbol in operations:
                print(symbol)
            operation = input("Input correct operation symbol:  ")
# End - operation symbol input이 dictionary 안에 없으면 다른 메시지 출력하도록 개선
        next_number = float(input("What's the next number?:  "))

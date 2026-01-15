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



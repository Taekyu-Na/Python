Dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

# Add into dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "Bug"
print(programming_dictionary["Bug"])

# Loop through dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])

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

Nesting

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

dictionary = {
    "name": [],
    "price": []
}

more_bidders = True
while more_bidders == True:
    name = input("What is your name?   ")
    bid = int(input("What is your bid?  : $ "))

    dictionary["name"] += [name]
    dictionary["price"] += [bid]

    more_bid = input("Are there are any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bid == "yes":
        print("\n" * 100)
    elif more_bid == "no":
        max_bid = max(dictionary["price"])
        bid_index = dictionary["price"].index(max_bid)
        print(f"The winner is {dictionary["name"][bid_index]} with a bid of ${max_bid}")
        more_bidders = False

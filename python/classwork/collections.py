# Margaret Mary Boyle
# lists
cart = ["apples", "bananas", "cherries"]
print(cart)

    # add elements
cart.append("donuts")
cart.append("eggs")
cart.append("flour")
print(cart)

    # remove elements
cart.remove("cherries")
print(cart)

# cart.remove("pineapple") ERROR because pineapple is not in the list

if "pineapple" in cart:
    cart.remove("pineapple")

cart.pop(3) # removes the third thing in the list
print(cart)

cart.pop() # removes last elements
print(cart)

    # reverse order
cart.reverse()
print(cart)

    # sort alphabetically
cart.sort()
print(cart)

    # add more items
cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

# slice the list
fruit_basket = cart[3:]
print(cart)
print(fruit_basket)

# create an empty list
squares = []

# fill the list
for i in range (1, 10):
    squares.append(i * i)
print(squares)

# list comprehension: more convenient and faster way to produce a list like above
squares = [i * i for i in range (1, 10)]
print(squares)

# picking out things from cart that start with a certain letter
b_items = [item for item in cart if item.startswith("b")]
print(b_items)

# idk what this is but we did it in class
inventory = [0] * len(cart)
print(inventory)
inventory[0] = 100








# sets
number_set = set()
number_set = {1, 1, 2, 3, 4, 0, 10, 5} # sets cannot have duplicates, so this will only print one of the 1's
print(number_set) # prints in ascending order

     # add number to set
number_set.add(-10)
print(number_set)

num_lst = [1, 1, 4, 5, 5, 6, 6]
no_dups = set(num_lst)
print(no_dups)
no_dups = list(no_dups)
print(no_dups)

ns = sorted(number_set)
print(ns)








# dictionary
fav_snacks = {}
fav_snacks = {
    "kathleen" : "tortilla chips",
    "maggie" : "pretzels",
    "emily" : "buffalo chicken dip",
    "ava" : "chocolate"
}
print(fav_snacks)

     # add person to dictionary
fav_snacks["wade"] = "popcorn"
print(fav_snacks)

print("kathleen's favorite snack is " + fav_snacks["kathleen"] + ".")
# print("kathleen's favorite snack is " + fav_snacks["bob"] + ".") # causes an ERROR because we do not have a bob in our list 

if "bob" in fav_snacks:
    print("bob's favorite snack is " + fav_snacks["bob"] + ".")

for key in fav_snacks:
    print(key + "'s favorite food is " + fav_snacks[key])
    print(f"{key}'s favorite food is {fav_snacks[key]}") 
    # two equivalent print statements...matter of preference on which one you use

for key, value in fav_snacks.items():
    print(key, value)

keys = fav_snacks.keys()
values = fav_snacks.values()

    # add a key and value to fav snacks
fav_snacks["alice"] = ["chips", "nuts"]
print(fav_snacks)

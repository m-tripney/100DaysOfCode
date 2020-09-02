# Example...
pybites = {
    "mark": 30,
    "ibi": 20,
    "max": 10,
}

print(pybites)

# Dictionaries are unordered, and made up of keys and values.
# Values, then, are accessed via their corresponding key.

# Create an empty dictionary:
people = {}

# How do we add data to it?
people["mark"] = "scottish"
print(people)

# Add another key/value pair...
people["ibi"] = "german"
print(people)

# We can view keys like so:
print(pybites.keys())
# And, similarly, values:
print(pybites.values())
# What about both?
print(pybites.items())
# And, we can make this last example a bit more readable:
for name, nationality in people.items():
    print(f"{name.title()} is {nationality.title()}.")

for key, value in pybites.items():
    print(f"{key.title()} scored {value}.")

# keys only
for keys in pybites.keys():
    print(keys)

# values only
for values in pybites.values():
    print(values)
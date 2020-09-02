my_string = "mark"

# mutability — the 'changeability' of something
# Thus, mutable = can be changed; immutable = can't be changed

# We were changing the my_string variable in file d7_lists.py. It was a list (mutable).
# A tuple is like a list which can't be changed — it is immutable.

l = list(my_string)
t = tuple(my_string)

print(l)  # ['m', 'a', 'r', 'k']
print(t)  # ('m', 'a', 'r', 'k')

# We can edit the list...
l[0] = "d"
print(l)

# ... but not the tuple (uncomment lines 20-21 to see what happens)
# t[0] = "d"
# print(t)  # TypeError: 'tuple' object does not support item assignment

# We can think of tuples as 'read only'. We can still read from them...
print(t[0])
# ... and iterate over them:
for letter in t:
    print(letter)
# But we can't edit them.

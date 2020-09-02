numlist = [x for x in range(1,6)]
print(numlist)

# Very easy to reverse
numlist.reverse()
print(numlist)

# We could reverse this back, or... we can sort()
numlist.sort()
print(numlist)

# Print all the values in numlist
for num in numlist:
    print(num)
    # print(str(num))

# We can call list against a string
my_string = "mark"
print(list(my_string))  # Each character is a string value in a list
# Of course, we can assign this to a variable...
l = list(my_string)
# ... and work with it:

print(l[0])  # Print the 1st item
print(l[-1])  # Print the last item
l.pop()  # sans argument, returns last item in the list; can be assigned to var
print(l)
l.insert(3, "k")  # Insert "k" at index position 3
print(l)
l[0] = "d"  # Replace item at index position 0 with "d"
print(l)
del l[0]  # Delete item at index position 0 — it is not returned, just deleted
print(l)
l.insert(0, "m")  # Insert "m" at index position 0
print(l)
first = l.pop(0)  # pop() returns an item, so we can save it to a variable
print(first)
l.append("s")  # append() adds an item to the end of the list
print(l)

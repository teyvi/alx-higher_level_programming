#!/usr/bin/python3

# Use a separator variable to control the formatting
separator = ""
for num in range(0, 100):
    print("{}{:02d}".format(separator, num), end='')
    separator = ", "

# Print a new line at the end
print()

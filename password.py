import random

// Defining the variables
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "`~!@#$%^&*()_-+={[]}<>,./?"

// Combining the string
string = lower + upper + number + symbol
length = 20

// Joining String
password = "".join(random.sample(string, length))

// Print Statement
print("Your Password is : " + password)

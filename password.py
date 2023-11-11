import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "`~!@#$%^&*()_-+={[]}<>,./?"

string = lower + upper + number + symbol
length = 20

password = "".join(random.sample(string, length))

print("Your Password is : " + password)
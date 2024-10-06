# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("hello")
    print("my name is")
    print("luis")


greet()


# the parameter: is the name of the data we use to refer to and do things with it inside our function, in this case "name" (in other words is the name of the variable the function uses)
def greet_with_name(name):
    print("hello", name)
    print(f"how do you do {name}?")
    print("i like coconut")


# the argument: is the actual piece of data that is passed over to the function when it's called, in this case "eduardo" (in other words is the data inside the variable our function uses)
greet_with_name("eduardo")


# functions with 2 or more inputs, they are separated by a coma
def greet_with(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}?")


# with code editors you can highlight a word and then press open ",(,[,{,' keys to add that symbol to both sides of the ([{"'word'"}])

# positional argument: the function assigns the arguments in the order the parameters are written
greet_with("luis", "guadalajara")
greet_with("guadalajara", "luis")
# keyword argument: we assign the arguments to the parameters manually, it is used to be more clear when you call the function, but it makes the code longer
# keep the names of the arguments and parameters different to avoid confusion
greet_with(location="guadalajara", name="luis")
# ceil () function rounds up a number
import math

print(math.ceil(3.3))
# floor function rounds down a number
print(math.floor(3.7))
# this for loop doesn't activate cause of its specified range
num = 2
for i in range(2, num):
    print(num / i)
# help() function is a way of getting useful information
help([1, 2, 3, 4, 5])
help(greet)
help(num)
help()
# dir() function: Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.
print(dir())
print(dir(num))
print(dir(greet))
print(dir(greet()))

# https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number
# https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
# https://www.w3schools.com/python/ref_list_index.asp

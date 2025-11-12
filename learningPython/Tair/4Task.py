# my_string = "Hello world"

# print("Hello" in my_string)

# my_string = "Alice"
# print(my_string.upper())

# my_string = "ALICE"
# print(my_string.lower())


# my_string = "     Hello world        "
# print(len(my_string))
# print(len(my_string.strip()))
# print(my_string.replace("world", "Python"))
# print(my_string.count("l"))

# my_string = "10d"
# print(my_string.isdigit())

# integer = input("Enter a number:")
# if integer.isdigit():
#    integer = int(integer)

# print(integer)


# name = "Alice"
# age = 25 
# print(f"Hello, my name is {name} and I'm {age} years old")

# x = 10 
# y = 5
# print(f"summary is {x + y}, multiplication is {x * y}")

# my_string = input("Enter a number: ")

# if my_string.isdigit():
#    my_integer = int(my_string)
#    print(my_integer)
# else:
#    print("is not a digit")


print("mr. %s, the total is %.2f." % ("jekyll", 15.53))
print("mr. %d, the total is %s." % (32, "okay"))
print("The character after %c is %c." % ("B", "C"))
place = "New York"
print("Welcome to %s!" % place)
year = 2019
print("%i will be a perfect year." % year)
number = 15
print("%i in octal is %o" % (number, number))
print("%i is hex is %02x" % (number, number))
print("%i in hex is %04X" % (number, number))

price = 15.05
print("the price is %.2f" % price)
place = "London"
print ("%10s is not a place in France" % place)
print ("%-10s is not a place in France" % place)
print                               ("The postcode is %10d." % 25000) 
print ("The postcode is %-10d." % 25000)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
print(f"{txt.format(price = 40) +  " hi"}") 
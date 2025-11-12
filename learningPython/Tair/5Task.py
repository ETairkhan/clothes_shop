my_list = list()
print(my_list)

check = ["apple", 1, 1.5, True , [ 1, 3, 2]] # very bad
print(check)

a1 = [1,2,3]
a2 = [1,3,2]
a3 = [1,2,3]
print(a1 == a3)
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(len(fruits))

fruits = ["apple", "banana"]

print("banana" in fruits)
print("smth" in fruits)


elem1 = "apple"
elem2 = "banana"
elem3 = "cherry"
fruits = [elem1, elem2, elem3]
print(fruits)

word = "hello"
my_list = list(word)
print(my_list)

my_list1 = [1,2,3]
my_list2 = [4,5,6]
my_list3 = my_list1 + my_list2
print(my_list3)

fruits = ["apple", "banana", "cheery"]
fruits.append("watermelon")
print(fruits)

my_string = "hello, world"
new_string = my_string.replace("world", "python")
print(my_string)
print(new_string)

fruits = ["apple", "banana", "cheery"]
fruit = fruits.pop()
print(fruit)
print(fruits)
fruits = ["apple", "banana", "cheery"]
fruits2 = ["apple", "fig", "cheery"]
fruits.extend(fruits2)
print(fruits)

fruits.reverse()
print(fruits)


my_list = [5,4,8,10,1,2,14,4]
my_list.sort(reverse=True)
print(my_list)

my_string = "My name is Tair"
my_list = my_string.split(" ")

print(my_list)

joined_string = " ".join(my_list)
print(joined_string)

my_list = [5,4,8,10,1,2,14,4]
print(max(my_list))
print(min(my_list))
print(sum(my_list))
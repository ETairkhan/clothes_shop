user_roles = ("admin", "editor", "viewer")

print(user_roles)
print(len(user_roles))

for role in user_roles:
   print(role)


print("admin" in user_roles)
print("write" in user_roles)

print(user_roles[0])


not_tuple = ("admin")

print(type(not_tuple))

my_tuple = ("admin", )
print(type(my_tuple))


# person = {
#    "name" : "Tair",
#    "age" : 30,
#    "city" : "Astana"
# }

# other_person = {
#     "age" : 30,
#      "city" : "Astana",
#         "name" : "Tair",
#         "ala" : "ugu"
# }

# print(person == other_person)

# person["job"] = "Programmer"

# print(person)


# person = {}

# person["name"] = "Aya"
# person["age"] = 18
# person["city"] = "Astana"

# print(person.get("country", "USA"))

# print(person.get("name", "YEBAT"))

# for p in person:
#    print(person[p])

# for key, value in person.items():
#    print(key, value, sep=", " , end="!\n")
   
# for key in person.keys():
#    print(key)



# for value in person.values():
#    print(value)   


# person = {
#     "city": "New York",
#     "age": 30,
#     "name": "John",
# }
# additional_person_info = {
#     "job": "Engineer",
#     "married": True,
#     "city": "London"
# }

# person.update(additional_person_info)
#OR
# person = person | additional_person_info
# print(person)


# задание
# Есть список словарей со студентами `students`. В каждом объекте есть имя и фамилия студента,
# а также список оценок (целых чисел). Нужно написать функцию get_best_students, которая берёт студентов и находит того,
# у кого средний балл наибольший. Возвращает функция список студентов с лучшим баллом. У некоторых студентов в оценках
# есть None: их среднюю оценку мы считаем равной 0.


students = [
    {"name": "John", "surname": "Doe", "grades": [5, 5, 4, 4]},
    {"name": "Jane", "surname": "Doe", "grades": [4, 3, 4, 3, 5]},
    {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]},
    {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 3, 3, 5]},
    {"name": "Guido", "surname": "Van Rossum", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
    {"name": "Elon", "surname": "Musk", "grades": None}
]


# решение

# def get_best_students(*, students: list[dict]):
   #without knowledge i did it like *, students: list when it suppose to be list[dict]
   # index_of_the_best = 0
   # max = 0 
   # list_of_grades = list()
   # for dic in range(len(students)):
   #    for key, value in students[dic].items():
   #       if key == "grades":
   #          list_of_grades.append(value)

   # print(list_of_grades)
   # count =0 
   # for  lists in list_of_grades:
   #    print(count)
   #    print(lists)
   #    count+=1
   # for list in list_of_grades:
   #    sum = 0
   #    print(i)
   #    lisss = list(i)
   #    # print(list_of_grades)
   #    # print(list_of_grades[i])
   #    for grade in lisss:
   #       sum += grade 
   #       average =  sum / len(list_of_grades)
   #       if average > max:
   #          index_of_the_best = i
   #          max = average

   # print(index_of_the_best)


   
def get_best_students(*, students: list[dict]):
   best_student = []
   best_average_grade = 0
   for student in students:
      grade = student["grades"]
      if grade is None:
         average_grade = 0
      else:
         average_grade = sum(grade) / len(grade)
      if average_grade > best_average_grade:
         best_average_grade = average_grade
         best_student.append(student)
      elif average_grade == best_average_grade:
         best_student.append(student)
   return best_student


print(get_best_students(students=students))
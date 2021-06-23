# Dictionaries and Sets both are Data collections in Python

# Dict are another way to manage data but can be more Dynamic
# Dict work as a KEY AND VALUE
# KEY = REFERENCE OF THE OBJECT
# VALUE = DATA STORAGE MECHANISM YOU WANT TO USE
# Dynamic as Lists and another dict inside a dict
# Syntax - name = {KEY: VALUE, ...}

student_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["data types", "git and github", "operators", "Lists and Tuples"]
}
#         INDEX:                       0            1                2              3

print(student_1)
print(type(student_1))
print(student_1["stream"])  # Fetch VALUE from "stream" KEY
print(student_1["completed_lesson_names"][1])
# Print the second last index of key completed_lesson_names
print(student_1["completed_lesson_names"][-2])

# Can we apply CRUD on a Dict
# Update
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])
# Delete
student_1["completed_lesson_names"].remove("operators")
print(student_1["completed_lesson_names"])

# Built in methods to use in dicts
print(student_1.keys())  # keys() gets all the key names
print(student_1.values())  # values() gets all the values inside each key

# Sets are also a Data collection
# Syntax - name = {"", "", ""}
# Sets are ordered
shopping_list = ["eggs", "tea", "milk"]
#                   0      1       2
print(shopping_list)
car_part = {"Engine", "Wheels", "Windows"}
print(car_part)
# CRUD with sets
car_part.add("Seats")
print(car_part)
car_part.discard("Wheels")
print(car_part)

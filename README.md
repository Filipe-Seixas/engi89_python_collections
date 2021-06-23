# Python Data Collections

- Lists
- Tuples
- Dict
- Sets

## Lists (AKA array in other languages)

- Shopping list - multiple items
- Add, delete, edit, update
- CRUD: `Create`, `Read`, `Update` and `Delete`


### Let's create a shopping list
`Syntax [] - name_of_list = ["", "", ""]`
```python
shopping_list = ["apples", "eggs", "dark chocolate", "tea", "bread"]
print(shopping_list)
# Checking the type of this data with type()
print(type(shopping_list))

# How can I access list items using the same concept that we learned yesterday INDEXING
print(shopping_list[1]) # will display eggs
print(shopping_list[-1]) # will display the last item (bread)

# How can I replace an item in the list
shopping_list[0] = "mango"
print(shopping_list)
# How can I add an item to our list
shopping_list.append("tuna")
print(shopping_list)

# Search python docs and find out how to delete an item from list on index 3
shopping_list.pop(3)
print(shopping_list)

# We can have multiple data types in the same list
mix_list = [1, 2, 3, "one", "two", "three"]
print(mix_list)
```
## What are tuples and what is the difference between lists and tuples
` Tuple syntax () name_of_tuple = ("", "", "")`
```python
essentials = ("paracetamol", "milk", "butter")
print(essentials)
print(type(essentials))
# Lists are MUTABLE and Tuples are IMMUTABLE
essentials.pop(3)   # This would throw an error
```

## Dictionaries and Sets both are Data collections in Python

- Dict are another way to manage data but can be more Dynamic
- Dict work as a KEY AND VALUE
- KEY = REFERENCE OF THE OBJECT
- VALUE = DATA STORAGE MECHANISM YOU WANT TO USE
- Dynamic as Lists and another dict inside a dict
- Syntax - name = {KEY: VALUE, ...}

```python
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
```

## Sets are also a Data collection
- Syntax - name = {"", "", ""}
- Sets are ordered
```python
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
```

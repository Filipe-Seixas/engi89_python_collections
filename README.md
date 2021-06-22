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

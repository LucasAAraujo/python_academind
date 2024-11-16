persons = [
    {"name": "Alice", "age": 25, "hobbies": ["reading", "cycling", "painting"]},
    {"name": "Bob", "age": 30, "hobbies": ["gaming", "hiking", "coding"]},
    {"name": "Charlie", "age": 22, "hobbies": ["cooking", "traveling", "photography"]},
    {"name": "Diana", "age": 18, "hobbies": ["drawing", "swimming", "dancing"]}
]

names = [person["name"] for person in persons]
print(names)  # Output: ['Alice', 'Bob', 'Charlie', 'Diana']

all_older_than_20 = all(person["age"] > 20 for person in persons)
print(all_older_than_20)  # Output: False (Diana is 18)


import copy

copied_persons = copy.deepcopy(persons)
copied_persons[0]["name"] = "Alexandra"
print(copied_persons[0]["name"])  # Output: Alexandra
print(persons[0]["name"])         # Output: Alice (original remains unchanged)

person1, person2, person3, person4 = persons
print(person1)  # Output: {'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'cycling', 'painting']}
print(person2)  # Output: {'name': 'Bob', 'age': 30, 'hobbies': ['gaming', 'hiking', 'coding']}
print(person3)  # Output: {'name': 'Charlie', 'age': 22, 'hobbies': ['cooking', 'traveling', 'photography']}
print(person4)  # Output: {'name': 'Diana', 'age': 18, 'hobbies': ['drawing', 'swimming', 'dancing']}

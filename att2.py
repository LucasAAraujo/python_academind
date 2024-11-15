names = ["Jonathan", "Alice", "Bob", "Catherine", "Daniel", "Eve", "John"]

print("Names longer than 5 characters:")
for name in names:
    if len(name) > 5:  
        print(f"{name} (Length: {len(name)})")

print("\nNames that include 'n' or 'N' and are longer than 5 characters:")
for name in names:
    if len(name) > 5 and ("n" in name.lower()):
        print(f"{name} (Length: {len(name)})")

print("\nRemoving names from the list:")
while names:
    removed_name = names.pop()
    print(f"Removed: {removed_name}")

print("\nFinal names list:", names)

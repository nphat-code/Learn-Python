# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA"))
# capitals.update({"Germany": "Berlin"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
keys = capitals.keys()
values = capitals.values()
items = capitals.items()
print(capitals)
print(keys)
print(values)
print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")
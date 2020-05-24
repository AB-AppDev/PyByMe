items = ["bread", "milk", "tomatoes", "toast"]

print(items[3])
print(len(items))

items.insert(4, "apples")
print(items)

items.remove("tomatoes")
print(items)

print(items.index("apples"))

items.sort()
print(items)

items.reverse()
print(items)

print(items.count("apples"))


items.clear()
print(items)



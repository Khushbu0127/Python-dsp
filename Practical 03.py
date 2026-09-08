lst = [10, 20, 30, 40, 50]
print("List:", lst)

lst.append(60)
lst.insert(1, 15)
lst.remove(30)
print("After append, insert, remove:", lst)

print("Length:", len(lst))
print("Max:", max(lst))
print("Sum:", sum(lst))
print("Sort:", sorted(lst))
print("Reverse:", lst[::-1])
print("Slicing [1:4]:", lst[1:4])

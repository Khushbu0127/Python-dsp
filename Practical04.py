tup = (10, 20, 30, 20)
print("Tuple:", tup)
print("Count of 20:", tup.count(20))
print("Index of 30:", tup.index(30))

# Set
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print("\nSet s1:", s1, " s2:", s2)
print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference:", s1 - s2)

# Dictionary
student = {"name": "Khushbu", "roll": "BT25003009S", "branch": "DS A"}
print("\nDictionary:", student)
print("Name:", student["name"])
student["city"] = "Rajura"
print("After adding city:", student)
print("All keys:", student.keys())
print("All values:", student.values())

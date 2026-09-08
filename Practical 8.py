# Practical 8: File Handling with Exception Handling

print("--- Practical 8 ---")

# File me likhna + Exception handle karna sab ek sath
try:
    # Step 1: File me data likhna
    with open("student.txt", "w") as f:
        f.write("Name: Sakshi\n")
        f.write("Branch: Data Science\n")
        f.write("Year: 2nd\n")
    print("File me data likh diya!")

    # Step 2: File se data padhna
    with open("student.txt", "r") as f:
        data = f.read()
    
    print("\nFile ka data:")
    print(data)

    # Step 3: Jo file hai hi nahi usko kholna (exception check)
    print("Ab ek aisi file khol rahe hai jo hai hi nahi...")
    with open("not_exist.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("Error: File nahi mili!")

except Exception as e:
    print("Kuch error aaya:", e)

else:
    print("\nSab kuch sahi chala!")

finally:
    print("Practical Complete!")

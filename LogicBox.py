print("Welcome to the Pattern Generator and Number Analyzer!")

choice = int(input("Choose an option:\n1. Generate Patterns \n2. Analyze Numbers \n3. Exit \nEnter your choice: "))

if choice == 1:
    print("Pattern:")
    for i in range(1, 6):
        for j in range(i):
            print("*", end="")
        print()
elif choice == 2:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")
        sum += num
    print("Sum of all numbers from", start, "to", end, "is:", sum)
elif choice == 3:
        print("Exiting the program. Goodbye!")
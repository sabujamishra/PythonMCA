def menu():
    my_list = []

    while True:
        print("\n--- List Operations Menu ---")
        print("1. Create list")
        print("2. Display list")
        print("3. Insert element")
        print("4. Delete element")
        print("5. Search element")
        print("6. Sort list")
        print("7. Reverse list")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of elements: "))
            my_list = []
            for i in range(n):
                val = int(input(f"Enter element {i+1}: "))
                my_list.append(val)
            print("List created successfully!")

        elif choice == 2:
            print("Current List:", my_list)

        elif choice == 3:
            val = int(input("Enter element to insert: "))
            pos = int(input("Enter position (0-based index): "))
            if 0 <= pos <= len(my_list):
                my_list.insert(pos, val)
                print("Element inserted successfully!")
            else:
                print("Invalid position!")

        elif choice == 4:
            val = int(input("Enter element to delete: "))
            if val in my_list:
                my_list.remove(val)
                print("Element deleted successfully!")
            else:
                print("Element not found!")

        elif choice == 5:
            val = int(input("Enter element to search: "))
            if val in my_list:
                print(f"Element {val} found at position {my_list.index(val)}")
            else:
                print("Element not found!")

        elif choice == 6:
            my_list.sort()
            print("List sorted successfully!")

        elif choice == 7:
            my_list.reverse()
            print("List reversed successfully!")

        elif choice == 8:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the program
menu()

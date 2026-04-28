import random

array = []


def create_array():
    global array
    array = [random.randint(-100, 100) for _ in range(200)]
    print("Array created.")


def show_array():
    if not array:
        print("Please create the array first.")
        return

    print("Array:")
    print(array)


def filter_positive():
    if not array:
        print("Please create the array first.")
        return

    positives = [x for x in array if x > 0]

    print("Positive numbers:")
    print(positives)


def replace_negative():
    global array

    if not array:
        print("Please create the array first.")
        return

    array = [x if x >= 0 else 0 for x in array]

    print("Negative values replaced with zeros.")
    print(array)


def calculate_average():
    if not array:
        print("Please create the array first.")
        return

    average = sum(array) / len(array)

    print(f"Average value: {average:.2f}")


while True:
    print("\n========== MENU ==========")
    print("1 - Create array")
    print("2 - Show array")
    print("3 - Filter positive numbers")
    print("4 - Replace negative values with zeros")
    print("5 - Calculate average value")
    print("0 - Exit")
    print("==========================")

    choice = input("Choose an option: ")

    if choice == "1":
        create_array()
    elif choice == "2":
        show_array()
    elif choice == "3":
        filter_positive()
    elif choice == "4":
        replace_negative()
    elif choice == "5":
        calculate_average()
    elif choice == "0":
        print("Program finished.")
        break
    else:
        print("Invalid choice. Try again.")
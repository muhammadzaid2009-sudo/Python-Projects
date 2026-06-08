def food_manager():
    foods = {}
    while True:
        print("1. Add Food")
        print("2. View Food")
        print("3. Exit Food")

        choices = input("Enter your choice (1 , 2, or 3): ")

        if choices == '1':
            name = input("Enter the name of the food ")
            qty = input("Enter the quantity of the food ")
            foods[name]  = qty
            print(f"{name} added with quantity {qty}")

        elif choices == '2':
            for name in foods:
                print(f"name: {name}, quantity: {foods[name]}")

        elif choices == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

food_manager()
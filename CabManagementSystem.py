cabs = []

print("--- Setup Your Cab System ---")
number_of_cabs = input("How many cabs do you want to add? ")
number_of_cabs = int(number_of_cabs)

for i in range(number_of_cabs):
    print("\nEnter details for Cab #", i + 1)
    
    cab_id = input("Enter Cab ID: ")
    driver_name = input("Enter Driver Name: ")
    cab_route = input("Enter Route: ")
    
    new_cab = {
        "id": cab_id,
        "driver": driver_name,
        "route": cab_route,
        "available": "Yes"
    }
    
    cabs.append(new_cab)

print("\nSystem setup complete! Moving to the main menu...")

while True:
    print("\n--- CAB MANAGEMENT SYSTEM ---")
    print("1. View All Cabs")
    print("2. Book a Cab")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        print("\n--- Current Cabs ---")
        if len(cabs) == 0:
            print("No cabs in the system.")
        else:
            for cab in cabs:
                print("ID:", cab["id"], "| Driver:", cab["driver"], "| Route:", cab["route"], "| Available:", cab["available"])
            
    elif choice == "2":
        print("\n--- Book a Cab ---")
        user_route = input("Enter your destination route: ")
        
        found = False
        for cab in cabs:
            if cab["route"] == user_route:
                if cab["available"] == "Yes":
                    cab["available"] = "No"
                    print("Success! Cab", cab["id"], "with driver", cab["driver"], "is booked.")
                    found = True
                    break
        
        if found == False:
            print("Sorry, no available cabs found for that route.")
            
    elif choice == "3":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice! Please pick 1, 2, or 3.")
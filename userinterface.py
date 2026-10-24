#User interface for orbit7 booking menu 

print("="*55)
print("Welcome to Orbit7 space tavel booking system")
print("="*55)
print(" ORBIT7 SPACE TRAVEL BOOKING SYSTEM - YEAR 2050")
print("1. Book a Space Flight")
print("2. View All Bookings")
print("3. View Fare and Training Guide")
print("4. Exit")
print("="*55)

if choice == "1":
  print("\n--- BOOK A FLIGHT ---")
  name = input("Enter Primary passenger name: ")
  passengers = int(input("Enter number of passengers: "))

elif choice == "2":
        print("\n=== ALL CONFIRMED BOOKINGS ===")
        if len(bookings) == 0:
            print("No bookings found.")
        else:
            for i, b in enumerate(bookings, 1):
                print(f"{i}. {b}")

        # Destination selection
  print("Destinations: 1. Moon | 2. Mars | 3. Europa")
  dest_choice = input("Choose destination (1/2/3): ")
  if dest_choice == "1":
    destination = "Moon"
    base_fare = 150000
  elif dest_choice == "2":
    destination = "Mars"
    base_fare = 450000
  else:
    destination = "Europa"
    base_fare = 900000


   # 3. View Fare and Training Guide
    elif choice == "3":
        print("\n=== FARE & TRAINING GUIDE ===")
        print("Destinations (One-Way / Round-Trip):")
        print("  - Moon   : RM150,000 / RM270,000")
        print("  - Mars   : RM450,000 / RM810,000")
        print("  - Europa : RM900,000 / RM1,620,000")
        print("Pre-Flight Training (Per Pessanger):")
        print("  - Mandatory Safety Clearance : RM15,000 (Required)")
        print("  - Zero-Gravity Orientation   : RM25,000 (Optional)")
        print("  - Spacesuit Fitting          : RM35,000 (Optional)")

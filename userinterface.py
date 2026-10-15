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

print("test")

print("Nisa' code")
ptint("Test")

print("Nisa'code")
print ("Ashiqur Rahman")
if choice == "1":
  print("\n--- BOOK A FLIGHT ---")
  name = input("Enter Primary passenger name: ")
  passengers = int(input("Enter number of passengers: "))

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

moon_fare = 35000
mars_fare = 45000
venus_fare = 50000

safety_fee = 5000
zero_gravity_fee = 12000
spacesuit_fee = 8000

destinations = ["Moon", "Mars", "Venus"]
ticket_types = ("One-way", "Round-trip")

#User interface for orbit7 booking menu 
def display_menu():
    print("=" * 50)
    print("              ORBIT7 SPACE TRAVEL")
    print("          BOOKING SYSTEM - YEAR 2050")
    print("=" * 50)
    print("  Your journey beyond Earth starts here!")
    print("-" * 50)
    print("  1. Book a Space Flight")
    print("  2. View Fare and Training Guide")
    print("  3. Exit")
    print("=" * 50)

#This section is to display the price menu for tickets & pre-flight training options
def fare_guide():
    print("=== Ticket Fees ===")
    print("\nMOON FARE: RM", moon_fare)
    print("MARS FARE: RM", mars_fare)
    print("VENUS FARE: RM", venus_fare)
    
    print("\n === Pre-flight training Fees ===")
    print("\nSAFETY CLEARANCE: RM", safety_fee)
    print("ZERO-GRAVITY: RM", zero_gravity_fee)
    print("SPACESUIT FITTING: RM", spacesuit_fee)
#This section is to get user's (name, destination,ticket type, no. passengers, pre-flight training options) and also give summary at the end 
def book_flight():
    name = input("\nEnter passenger name: ")
    
    print("\nAvailable Destinations:")
    print("1.", destinations[0])
    print("2.", destinations[1])
    print("3.", destinations[2])

    destination_choice = input("Choose destination: ")
    if destination_choice == "1":
        destination = destinations[0]
        fare = moon_fare
    elif destination_choice == "2":
        destination = destinations[1]
        fare = mars_fare
    elif destination_choice == "3":
        destination = destinations[2]
        fare = venus_fare
    else:
        print("Invalid destination.")
        return
    # Ticket type
    print("\nAvailable Ticket Types:")
    print("1.", ticket_types[0])
    print("2.", ticket_types[1])

    ticket = int(input("Choose ticket type (1/2) : "))
    
    if ticket == 1:
        ticket_type = ticket_types[0]
    elif ticket == 2:
        ticket_type = ticket_types[1]
        fare = fare * 2
    else:
        print("Invalid ticket type.")
        return

    # Number of passengers
    passengers = int(input("Number of passengers: "))

    if passengers <= 0:
        print("Invalid number of passengers.")
        return

    # Calculate flight fare
    flight_total = fare * passengers

    print("\n=== Pre-flight Training ===")

    safety_total = 0
    zero_gravity_total = 0
    suit_total = 0

    # Safety clearance
    safety = input("Include safety clearance? (Yes/No): ").title()

    if safety == "Yes":
        if passengers > 0:
            safety_total = safety_fee * passengers
    elif safety == "No":
        safety_total = 0
    else:
        print("Invalid answer. Safety clearance set to No.")

    # Zero-gravity training
    zero_gravity = input("Include zero-gravity training? (Yes/No): ").title()

    if zero_gravity == "Yes":
        zero_gravity_total = zero_gravity_fee * passengers
    elif zero_gravity == "No":
        zero_gravity_total = 0
    else:
        print("Invalid answer. Zero-gravity set to No.")

    # Spacesuit fitting
    suit = input("Include spacesuit fitting? (Yes/No): ").title()

    if suit == "Yes":
        suit_total = spacesuit_fee * passengers
    elif suit == "No":
        suit_total = 0
    else:
        print("Invalid answer. Spacesuit fitting set to No.")
    # Calculate total booking cost
    total_cost = flight_total + safety_total + zero_gravity_total + suit_total

    print("\n=== BOOKING SUMMARY ===")
    print("Passenger:", name)
    print("Destination:", destination)
    print("Ticket:", ticket_type)
    print("Passengers:", passengers)
    print("Flight fare: RM", flight_total)
    print("Safety clearance: RM", safety_total)
    print("Zero-gravity: RM", zero_gravity_total)
    print("Spacesuit fitting: RM", suit_total)
    print("TOTAL: RM", total_cost)

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_flight()

    elif choice == 2 :
        fare_guide()

    elif choice == 3:
        print("Thank you for using ORBIT7!")
        break

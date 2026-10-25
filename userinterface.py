moon_fare = 35000
mars_fare = 45000
venus_fare = 50000

safety_fee = 5000
zero_fee = 12000
spacesuit_fee = 8000

#User interface for orbit7 booking menu 
def display_menu():
    print("=" * 55)
    print("              ORBIT7 SPACE TRAVEL")
    print("          BOOKING SYSTEM - YEAR 2050")
    print("=" * 55)
    print("  Your journey beyond Earth starts here!")
    print("-" * 55)
    print("  1. Book a Space Flight")
    print("  2. View All Bookings")
    print("  3. View Fare and Training Guide")
    print("  4. Exit")
    print("=" * 55)

# Part 3: Fare guide

def fare_guide():
    print("\nMOON FARE: RM", moon_fare)
    print("MARS FARE: RM", mars_fare)
    print("VENUS FARE: RM", venus_fare)

    print("\nSAFETY CLEARANCE: RM", safety_fee)
    print("ZERO-GRAVITY: RM", zero_fee)
    print("SPACESUIT FITTING: RM", spacesuit_fee)
    print("\nPassenger details recorded.")
    print("Name:", passenger_name)
    print("Destination:", destination)
    print("Ticket type:", ticket_type)
    print("Number of passengers:", passenger_count)


def book_flight():
    name = input("\nEnter passenger name: ")

    print("\n1. Moon")
    print("2. Mars")
    print("3. Venus")

    destination_choice = input("Choose destination: ")

    if destination_choice == "1":
        destination = "Moon"
        fare = moon_fare
    elif destination_choice == "2":
        destination = "Mars"
        fare = mars_fare
    elif destination_choice == "3":
        destination = "venus"
        fare = venus_fare
    else:
        print("Invalid destination.")
        return

    print("\n1. One-way")
    print("2. Round-trip")

    ticket = int(input("Choose ticket type (1/2) : "))

    if ticket == "1":
        ticket_type = "One-way"
    elif ticket == "2":
        ticket_type = "Round-trip"
        fare = fare * 2
    else:
        print("Invalid ticket type.")
        return

    passengers = int(input("Number of passengers: "))

    if passengers <= 0:
        print("Invalid number of passengers.")
        return

    flight_total = fare * passengers

    # Mandatory safety clearance
    safety_total = safety_fee * passengers

    # Optional training
    zero = input("Include zero-gravity training? (Y/N): ").upper()

    if zero == "Y":
        zero_total = zero_fee * passengers
    else:
        zero_total = 0

    suit = input("Include spacesuit fitting? (Y/N): ").upper()

    if suit == "Y":
        suit_total = spacesuit_fee * passengers
    else:
        suit_total = 0

    total = flight_total + safety_total + zero_total + suit_total

    # Booking summary
    print("\n--- BOOKING SUMMARY ---")
    print("Passenger:", name)
    print("Destination:", destination)
    print("Ticket:", ticket_type)
    print("Passengers:", passengers)
    print("Flight fare: RM", flight_total)
    print("Safety clearance: RM", safety_total)
    print("Zero-gravity: RM", zero_total)
    print("Spacesuit fitting: RM", suit_total)
    print("TOTAL: RM", total)

    confirm = input("Confirm booking? (Y/N): ").upper()

    if confirm == "Y":
        booking = (name, destination, ticket_type, passengers,flight_total, safety_total, zero_total, suit_total, total)
        bookings = bookings + [booking]
        print("Booking confirmed!")
    
    else:
        print("Booking cancelled.")



def view_bookings():
     if len(bookings) == 0:
        print("No confirmed bookings.")
    else:
        for booking in bookings:
            print("\nPassenger:", booking[0])
            print("Destination:", booking[1])
            print("Ticket:", booking[2])
            print("Passengers:", booking[3])
            print("Flight fare: RM", booking[4])
            print("Safety clearance: RM", booking[5])
            print("Zero-gravity: RM", booking[6])
            print("Spacesuit fitting: RM", booking[7])
            print("TOTAL: RM", booking[8])


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        book_flight()
    elif choice == "2":
        view_bookings()
    elif choice == "3":
        fare_guide()
    elif choice == "4":
        print("Thank you for using ORBIT7!")
        break
    else:
        print("Invalid choice. Try again.")

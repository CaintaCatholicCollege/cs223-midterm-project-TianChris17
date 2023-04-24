#Bernardino, Christian M.
#BSCS 2A
#Final Project

price = 7

print("   ** OPEN 8:00AM - 10:00PM **   ")
print()

print("*** Welcome to SM Ticket Outlet ***")
print()

print("How can I help you!...")
print()

print("(1) Buying Ticket.")
print("(2) Reservation.")
print("(3) Cancel.")
print()

choose = int(input("Choose: "))

if choose == 1:
    print("------------------------------")
    print()

    print("*** SM Ticket Outlet ***")
    print()

    print("Available Movie:              Price:")
    print()

    print("1. John Wick Chapter 4         $",price)
    print("2. Lone Survivor               $",price)
    print("3. Avatar The Way of Water     $",price)
    print("4. Quantumania                 $",price)
    print("5. Black Adam                  $",price)
    print()

    print("Fill up the form!...")
    print()

    name = str(input("Name: "))
    print()
    print("! Minimum of 2 movies. !")
    movie = str(input("Movie: "))
    ticket = int(input("Ticekt: "))
    seat = str(input("Seat Numbers: "))
    print()

    total = ticket * price
    
    print("------------------------------")
    print()
    print("*** SM Ticket Outlet ***")
    print()
    print("Buying Ticket")
    print()
    print("Reciept")
    print()

    print("Name: ", name)
    print("Movie: ", movie)
    print("Number of Ticket: ", ticket)
    print("Total Price: $", total)
    print("Seat Number: ", seat)
    print()
    print("Thank you, have a nice day...")

elif choose == 2:
    print("------------------------------")
    print()

    print("*** SM Ticket Outlet ***")
    print()

    print("Available Movie:              Price:")
    print()

    print("1. John Wick Chapter 4         $",price)
    print("2. Lone Survivor               $",price)
    print("3. Avatar The Way of Water     $",price)
    print("4. Quantumania                 $",price)
    print("5. Black Adam                  $",price)
    print()

    print("Fill up the form!...")
    print()

    name = str(input("Name: "))
    email = str(input("Email Address: "))
    contact = str(input("Contact No.: "))
    print()
    print("! Minimum of 2 movies. !")
    movie = str(input("Movie: "))
    ticket = int(input("Ticekt: "))
    date = str(input("Date: "))
    time = str(input("Time: "))
    print()
    print("! Maximum of 20 seats can reserve. !")
    seat = str(input("Seat Numbers: "))
    print()

    total = ticket * price
    
    print("------------------------------")
    print()
    print("*** SM Ticket Outlet ***")
    print()
    print("Reservation")
    print()
    print("Reciept")
    print()

    print("Name: ", name)
    print("Email: ", email)
    print("Contact No.: ", contact)
    print("Movie: ", movie)
    print("Number of Ticket: ", ticket)
    print("Date: ", date)
    print("Time: ", time)
    print("Total Price: $", total)
    print("Seat Number: ", seat)
    print()
    print("Thank you, have a nice day...")

elif choose == 3:
    print("------------------------------")
    print()
    print("Thank you, have a nice day...")
else:
    print("------------------------------")
    print()
    print("Choose 1, 2, and 3 only.")

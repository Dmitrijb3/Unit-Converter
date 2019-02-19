print("Welcome to unit converter. Here you can convert kilometers into miles.")
while True:
    km = input("Enter amount of kilometers you want to convert: ")
    km = float(km)
    conversion = 0.621371
    miles = km * conversion
    print("Distance in miles are: ", "%.2F" % miles)
    choice = input("Would you like to start another conversion? ")
    if choice.lower() != "y" and choice.lower() != "yes":
        break



# Prompt the user to enter the destination city
while True:
    city_flight = input("Which is your destination: Berlin, London, Paris, or Vienna? ")
    if city_flight.lower() == "berlin":
        break
    elif city_flight.lower() == "london":
        break
    elif city_flight.lower() == "paris":
        break
    elif city_flight.lower() == "vienna":
        break
    else:
        print("Please enter a correct city name")
        continue

# Prompt the user to enter the number of nights staying
while True:
    try:
        num_nights = int(input("How many nights will you be staying? "))
        break
    except ValueError:
        print("Please enter an integer")
    continue
        

# Prompt the user to enter the number of rental days
while True:
    try:
        rental_days = int(input("How many days you will rent a car? "))
        break
    except ValueError:
        print("Please enter an integer")
    continue

# Calculate the hotel cost based on the number of nights
def hotel_cost(num_nights):
    hotel_cost = num_nights * 100
    return hotel_cost

# Calculate the hotel cost
hotel = hotel_cost(num_nights)
print(f"Hotel cost: {hotel}")

# Calculate the plane cost based on the destination city
def plane_cost(city_flight):
    if city_flight.lower() == "berlin":
        plane_cost = 200
    elif city_flight.lower() == "london":
        plane_cost = 100
    elif city_flight.lower() == "paris":
        plane_cost = 150
    elif city_flight.lower() == "vienna":
        plane_cost = 125
    return plane_cost

# Calculate the plane cost
plane = plane_cost(city_flight)
print(f"Flight cost: {plane}")

# Calculate the car rental cost based on the number of rental days
def car_rental(rental_days):
    rental_cost = rental_days * 30
    return rental_cost

# Calculate the car rental cost
car = car_rental(rental_days)
print(f"Car rental price: {car}")

# Calculate the total holiday cost by adding up the costs
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total = plane_cost + car_rental + hotel_cost
    return total

# Calculate the total holiday cost
total_cost = holiday_cost(hotel, plane, car)
print(f"Total holiday cost: {total_cost}")
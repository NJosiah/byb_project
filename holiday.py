'''
This code will be asking the user where they will be flying between 3 cities.
It will then calculte the cost of the holiday based on hotel prices, flight tickets and how long they will be renting a car for.

The following are the destinations for the holiday: Paris, Dubai or Milan
'''

print("\n")
city_destinations = ["paris", "dubai", "milan"]
while True:
    city_flight = input("What city will you be flying to? Paris, Dubai or Milan? ").lower()
    if city_flight in city_destinations:
        break

num_nights = int(input("Enter num of nights at the hotel: "))

rental_days = int(input("Enter num of days the car would be hired: "))

''' 
cost of the hotel per night is £250
cost of the car rental per day is £75
'''

def hotel_cost(nights, num=250):
    total = nights * num
    return total

print("The total cost of the hotel is £" + str(hotel_cost(num_nights)))

'''
city flight ticket prices: Paris is £500, Dubai = £700, Milan is £300
'''

def plane_cost(destination):
    if destination == "paris":
       return 500
    elif destination == "dubai":
        return 700
    elif destination == "milan":
        return 300

print("The cost of the flight is £" + str(plane_cost(city_flight)))

def car_rental(car_days, num=75):
    total = car_days * num
    return total

print("The total cost of the car rental £" + str(car_rental(rental_days, 75)))

'''
adding each cost together for whole holiday total
'''

def holiday_cost(destination, hotel_stay, car_days):
     return hotel_cost(hotel_stay) + plane_cost(destination) + car_rental(car_days)

print("The total cost of the whole holiday is £" + str(holiday_cost(city_flight, num_nights, rental_days)))
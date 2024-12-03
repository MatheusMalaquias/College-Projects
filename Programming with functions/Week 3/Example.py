def main():
    print("This program computes the fuel efficiency")
    print("of your vehicle in miles per gallon.")

    prev_odom = float(input("Enter the previous odometer reading in miles: "))
    curr_odom = float(input("Enter the current odometer reading in miles: "))
    fuel_amount = float(input("Enter the amount of fuel in U.S. gallons: "))

    efficiency = miles_per_gallon(prev_odom, curr_odom, fuel_amount)

    print(f"{efficiency} miles per gallon")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    distance = end_miles - start_miles
    mpg = distance / amount_gallons
    return mpg

if __name__ == "__main__":
    main()

# COT 4930  Python Programming
# name: Guan Huang
# id  : ghuang2013
# lab : 01

def mile_to_km(miles):
    return 1.609 * miles

def check_input_range(input):
    if input<0: raise RuntimeError("Your input cannot be negative")

def main():
    try:
        distance_in_miles = float(input("Enter a distance in mile: "))
        check_input_range(distance_in_miles)
        distance_in_km = mile_to_km(distance_in_miles)
        print("The distance in km is {}".format(distance_in_km))
    except (ValueError, RuntimeError) as e:
        print(e)

if __name__ == "__main__":
    main()
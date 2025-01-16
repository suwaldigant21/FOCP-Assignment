"""3. Write a program that manages a list of countries and their capital cities. It should
 prompt the user to enter the name of a country. If the program already "knows"
 the name of the capital city, it should display it. Otherwise it should ask the user to
 enter it. This should carry on until the user terminates the program (how this
 happens is up to you).
 Note: A good solution to this task will be able to cope with the country being entered
 variously as, for example, "Wales", "wales", "WALES" and so on."""

def country_capital():
    countries = {
        "USA": "Washington D.C.",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid"
    }
    
    while True:
        country = input("Enter the name of a country: ").title()
        if country in countries:
            print(f"The capital city of {country} is {countries[country]}")
        else:
            capital = input(f"Enter the capital city of {country}: ").title()
            countries[country] = capital
        print("Press 'a' to quit or any other key to continue.")
        if input().lower() == 'a':
            break

country_capital()
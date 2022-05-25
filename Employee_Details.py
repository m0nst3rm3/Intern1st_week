from datetime import date
import Location
import Lunch
from Location import *
from Lunch import *

name = str(input("Enter Admin Name:\t ")), print("\n")
admin_detail = {
    "Name": name,
    "today": str(date.today()),
    "Lunch": meal(),
    "Location": location(),
}
print(admin_detail, '\n')


while True:
    print("Please place your order\n")
    name = str(input("Enter your name:\t ")), print("\n")
    user_detail = {
        "Name": name,
        "Date": str(date.today()),
        "Lunch": Lunch.food_selected(),
        "Location": Location.selected_location()
    }

    print(user_detail, "\n")

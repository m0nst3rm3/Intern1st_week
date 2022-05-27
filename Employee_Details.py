from datetime import date
import Location
import Lunch

admin_name = str(input("Enter Admin Name:\t "))
admin_detail = {
    "Name": admin_name,
    "today": str(date.today()),
    "Lunch": Lunch.meal(),
    "Location": Location.location(),
}
print(admin_detail, '\n')

while True:
    print("Please place your order\n")
    username = str(input("Enter your name:\t ")), print("\n")
    user_detail = {
        "Name": username,
        "Date": str(date.today()),
        "Lunch": Lunch.food_selected(),
        "Location": Location.selected_location()
    }

    print(user_detail, "\n")

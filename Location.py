print("-------------    PLEASE CREATE YOUR LOCATION LIST    -----------------\n")
restaurant_menu_options = {
    1: 'Create Restaurant List',
    2: 'Read Restaurant',
    3: 'Update Restaurant',
    4: 'Delete Restaurant',
    5: 'Select and Exit Restaurant Section\n',
}

location_list = []


def print_menu():
    for key in restaurant_menu_options.keys():
        print(key, '--', restaurant_menu_options[key])


def create():
    x = [x for x in input("Enter location name:").upper().split()]
    location_list.extend(x)
    print('\n', location_list, '\n')


def read():
    if len(location_list) == 0:
        print("""\n\t THERE ARE NO LOCATIONS. ADD SOME LOCATIONS !!!!!\t \n""")
    else:
        print('\n', location_list, '\n')


def update():
    while True:
        try:
            location_list[int(input("Enter the number:  "))-1] = input("Enter the Location:  ").upper()
            print('\n', location_list, '\n')
            break
        except ValueError:
            print('Please Enter number then after name')
            continue


def delete():
    try:
        user_input_delete = str(input("Please Enter the location you want to remove: ").upper())
        location_list.remove(user_input_delete)
        print(location_list)
    except ValueError:
        print("The location you want to remove is not in menu\n")


def selected_location():
    selected = ''
    try:
        print("Please choose your meal:")
        for idx, food in enumerate(location_list):
            print("{}) {}".format(idx + 1, food))
        use_input = int(input("\nEnter the number for food:      "))
        limit = len(location_list)
        if use_input > limit:
            print("Please Select from the list.")
            return selected_location()
        elif use_input <= 0:
            print("2) Please select from the list. ")
            return selected_location()
        else:
            selected = location_list[use_input - 1]
    except ValueError:
        print("Please provide a number. \n")
        return selected_location()
    except IndexError:
        print("Select from the list\n")
    return selected


def location():
    while True:
        print_menu()
        try:
            option = int(input('Enter your choice: '))
            if option not in range(1, 6):
                print('Invalid option. Please enter a number between 1 and 5.\n')
                continue
        except ValueError:
            print('Invalid option. Please enter a number between 1 and 5.\n')
            continue

        # Check what choice was entered and act accordingly
        if option == 1:
            create()

        elif option == 2:
            read()

        elif option == 3:
            if len(location_list) == 0:
                print("""\n\t \t There are no locations.
                 Please Create List First. \n""")
            else:
                update()

        elif option == 4:
            if len(location_list) == 0:
                print("""\n\t \t There are no locations in the list.
                 Please Create List First. \n""")
            else:
                delete()

        elif option == 5:
            if len(location_list) == 0:
                print("""\n\t \t There are no locations in the list.
                 Please Create List First. \n""")
            else:
                return selected_location()
    print("\n Your place: " + selected_location() + " has been selected.\n")

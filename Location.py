print("-------------    PLEASE CREATE YOUR LOCATION LIST    -----------------\n")
food_menu_options = {
    1: 'Create Restaurant List',
    2: 'Read Restaurant',
    3: 'Update Restaurant',
    4: 'Delete Restaurant',
    5: 'Select and Exit Restaurant Section\n',
}

location_list = []


def print_menu():
    for key in food_menu_options.keys():
        print(key, '--', food_menu_options[key])


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
    try:
        print("Please choose your location:")
        for idx, restaurant in enumerate(location_list):
            print("{}) {}".format(idx + 1, restaurant))
        selected = location_list[int(input("\n Enter the number to select location:    "))-1]
        if selected in location_list:
            print("Your location has been selected.\n")
            return selected
        else:
            print("The location you chose is not feasible. ")
            return selected

    except IndexError:
        print("Select from the list\n")
    except UnboundLocalError:
        print("Select from the list\n")


def location():
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
            print("\n")
        except ValueError:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
            create()

        elif option == 2:
            read()

        elif option == 3:
            update()

        elif option == 4:
            delete()

        elif option == 5:
            return selected_location()

        else:
            print('Invalid option. Please enter a number between 1 and 4.\n')
            break

    print(selected_location())

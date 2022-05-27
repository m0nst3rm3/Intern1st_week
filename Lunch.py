print("-------------      PLEASE CREATE YOUR FOOD MENU     -----------------\n")
food_menu_options = {
    1: 'Create Food List',
    2: 'Read Food available',
    3: 'Update',
    4: 'Delete Food',
    5: 'Select and Exit Food\n',
}

food_list = []


def print_menu():
    for key in food_menu_options.keys():
        print(key, '--', food_menu_options[key])


def create():
    x = [x for x in input("Enter Food name:\t").upper().split()]
    food_list.extend(x)
    print('\n', food_list, '\n')


def read():
    if len(food_list) == 0:
        print("""\n\t YOUR MENU IS EMPTY. ADD SOME ITEMS !!!!!!!!\t \n""")
    else:
        print('\n', food_list, '\n')


def update():
    while True:
        try:
            food_list[int(input("Enter the S.Number:  "))-1] = input("Enter the Food name:  ").upper()
            print("\n", food_list, "\n")
            break
        except IndexError:
            print('Please Select exact number: \n')
            continue


def delete():
    try:
        user_input_delete = str(input("Please Enter food you want to remove: ").upper())
        food_list.remove(user_input_delete)
        print(food_list)
    except ValueError:
        print("The food you want to remove is not in menu\n")


def food_selected():
    selected = ''
    try:
        print("Please choose your meal:")
        for idx, food in enumerate(food_list):
            print("{}) {}".format(idx + 1, food))
        use_input = int(input("\nEnter the number for food:      "))
        limit = len(food_list)
        if use_input > limit:
            print("Please Select from the list.")
            return food_selected()
        elif use_input <= 0:
            print("2) Please select from the list. ")
            return food_selected()
        else:
            selected = food_list[use_input - 1]
    except ValueError:
        print("Please provide a number. \n")
        return food_selected()
    except IndexError:
        print("Select from the list\n")
    return selected


def meal():
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
            if len(food_list) == 0:
                print("""\n\t \t There is no food in menu.
                 Please Create Menu First. \n""")
            else:
                update()

        elif option == 4:
            if len(food_list) == 0:
                print("""\n\t \t There is no food in menu.
                 Please Create Menu First. \n""")
            else:
                delete()

        elif option == 5:
            if len(food_list) == 0:
                print("""\n\t \t There is no food in menu.
                 Please Create Menu First. \n""")
            else:
                return food_selected()
    print("\n Your order: " + food_selected() + " has been placed\n")

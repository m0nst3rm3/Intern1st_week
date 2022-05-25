print("-------------      PLEASE CREATE YOUR FOOD MENU     -----------------\n")
restu_menu_options = {
    1: 'Create Food List',
    2: 'Read Food available',
    3: 'Update',
    4: 'Delete Food',
    5: 'Select and Exit Food\n',
}

food_list = []


def print_menu():
    for key in restu_menu_options.keys():
        print(key, '--', restu_menu_options[key])


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
    try:
        print("Please choose your meal:")
        for idx, food in enumerate(food_list):
            print("{}) {}".format(idx + 1, food))
        selected = food_list[int(input("\n Enter the number for food:   "))-1]

        if selected not in food_list:
            print("The food is not in menu. ")
        elif selected not in food_list:
            print("Your food has been selected.\n")
    except IndexError:
        print("Select from the list\n")
    except UnboundLocalError:
        print("Select from the list\n")

    return selected


def meal():
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print('Wrong input. Please enter a number ...')

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
                return food_selected(), print("Meal Confirmed", food_selected(),"\n")

        else:
            print('Invalid option. Please enter a number between 1 and 4.\n')
            break

    print(food_selected())
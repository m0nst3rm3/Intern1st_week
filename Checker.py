
food_list = ['MOMO', 'Chiya', 'Khaja', 'Samosa']

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
        elif use_input <=0:
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


print("Your order " + food_selected() + " has been placed")
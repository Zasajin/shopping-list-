section_priority = {
    'miscelaneous': 1
    'kitchen_utensils': 2
    'gardening': 3
    'spices': 4
    'meat': 5
    'vegetarian': 6
    'fish': 7
    'fruit_veggies': 8
    'oil': 9
    'frozen': 10
    'bakery': 11
    'asian': 12
    'pasta': 13
    'rice': 14
    'dairy': 15
    'drinks': 16
    'cleaning': 17
    'writing_material': 18
    'snacks': 19
}

    
grocery_items = [
    {}
]

def main_menu():

    while True:

        print('Welcome! Please choose an option'
              '1. Add item to list'
              '2. Adjust Categories'
              '3. Show List')

        choice = input('Please enter you choice: ')

        if choice == 1:
            add_item()
            break
        elif choice == 2:
            adjust_categories()
            break
        elif choice == 3:
            show_list()
            break
        else:
            print('Invalid input, please enter one of the given numbers')

def adjust_categories():

    while True:()
        print(f'{section_priority}')
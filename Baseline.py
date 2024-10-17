category_priorities = {
    'miscelaneous': 1,
    'kitchen_utensils': 2,
    'gardening': 3,
    'spices': 4,
    'meat': 5,
    'vegetarian': 6,
    'fish': 7,
    'fruit/veggies': 8,
    'oil': 9,
    'frozen': 10,
    'bakery': 11,
    'asian': 12,
    'pasta': 13,
    'rice': 14,
    'dairy': 15,
    'drinks': 16,
    'cleaning': 17,
    'writing_material': 18,
    'snacks': 19,
}

    
grocery_items = []

def main_menu():

    while True:

        print('Welcome! Please choose an option'
              '\n1. Add item to list'
              '\n2. Adjust Categories'
              '\n3. Show List')

        choice = input('Please enter you choice: ')

        if choice == '1':
            add_item(grocery_items)
            break
        elif choice == '2':
            adjust_categories(category_priorities)
            break
        elif choice == '3':
            sort_list(grocery_items)
            print(grocery_items)
            break
        else:
            print('Invalid input, please enter one of the given numbers')


def adjust_categories(a):

    print(a)
    print('Please select what you want to do:'
              '\n1. Rename categories'
              '\n2. Reorganize priorities'
              '\n3. Add category'
              '\n4. Delete category')
        
    adjust_choice = input('Enter the number of your desired action: ')

    if adjust_choice == '1':
        rename_categories(a)
    elif adjust_choice == '2':
        reorganize_priorities(a)
    elif adjust_choice == '3':
        add_category(a)
    elif adjust_choice == '4':
        delete_category(a)
    else:
        print('Invalid input, please enter one of the given numbers.')

    def rename_categories(a):
        old_c_name = input('Enter the category you want to rename or 0 to exit: ').strip()

        while old_c_name != '0':
            if old_c_name not in a:
                print('Category not found.')
            else:
                new_c_name = input('Enter the new name: ').strip()
                a[new_c_name] = a.pop(old_c_name)
                print(f'"{old_c_name}" renamed to "{new_c_name}".')

            old_c_name = input('Enter the category you want to rename or 0 to exit: ').strip()

    def reorganize_priorities(a):
        current_priorities = list(a.values())
        print(a)
        category_name = input('\nEnter the category of which you would like to change priority or 0 to exit: ')
        
        while category_name != '0':
            if category_name not in a:
                print('Category not found.')
            else:
                try:
                    new_priority = int(input('Enter the new priority (1 being highest priority, higher number = lower priority): '))
                    if new_priority == 0:
                        return
                    elif new_priority in current_priorities:
                        print('Priority already in use, reassigning priorities.'
                              'Please wait...')
                        reassign_priorities(a, new_priority)
                        current_priorities = list(a.values())
                        print('Priorities have been reassigned.')
                        print(a)
                    else:
                        a[category_name] = new_priority
                        current_priorities = list(a.values())
                        print(f'{category_name} has been assigned the priority {new_priority}\n')
                        print(a)
                except ValueError:
                    print('Invalid input, please enter an integer (0 to exit)')

            category_name = input('\n Enter the category of which you would like to change priority or 0 to exit: ')
                
    def reassign_priorities(a, new_priority):

        for category, priority in a.items():
            if priority >= new_priority:
                a[category] += 1

    def add_category(a):
        print('Current categories: ', list(a))
        new_category = input('Enter the name of the category you wish to add (or 0 to exit): ')

        while new_category != '0':
            if new_category in a:
                print('Category already in the list.')
            else:
                try:
                    new_priority = int(input('Please assign a priority (1 being the highest): '))
                    a[new_category] = new_priority
                    if new_priority in a.values():
                        print('Priority value already used, reassigning priorities...')
                        reassign_priorities(a, new_priority)
                        print('Priorities reassigned')
                        print(a)
                except ValueError:
                    print('Invalid input, please enter a positive integer.')

            new_category = input('Enter the name of the category you wish to add (or 0 to exit): ')

    def delete_category(a):
        print(a)
        choice = input('Enter the category you wish to remove (or 0 to exit): ')

        while choice != '0':
            if choice in a:
                a.pop(choice)
                print(f'{choice} has been removed from your categories')
                print(a)
            else:
                print('Category not found, please enter an existing category to remove.')

            choice = input('Enter the category you wish to remove (or 0 to exit): ')

def add_item(a):
    print(category_priorities)
    new_item = input('Enter an item you wish to add to your shopping list (or 0 to return to the main menu) ')

    while new_item != '0':
        category = input('Enter a category from the above you wish to assign the item to (or 0 to exit): ')
        while category != '0':
            if category not in category_priorities:
                print('Category not found, please enter a category of the above list')
            else:
                grocery_items.append((new_item, category))
                break
        new_item = input('Enter an item you wish to add to your shopping list (or 0 to return to the main menu) ')
    
    print('Your shopping list, right now: ')
    print(grocery_items)
        
def sort_list(a):
	a.sort(key=lambda item: (category_priorities[item[1]], item[0]))
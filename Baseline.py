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

    print(list(f'{category_priorities}'))
    print('Please select what you want to do:'
              '1. Rename categories'
              '2. Reorganize priorities'
              '3. Add category'
              '4. Delete category')
        
    adjust_choice = Input('Enter the number of your desired action: ')

    if adjust_choice == 1:
        rename_categories(category_priorities)
    elif adjust_choice == 2:
        reorganize_priorities(category_priorities)
    elif adjust_choice == 3:
        add_category(category_priorities)
    elif adjust_choice == 4:
        delete_category(category_priorities)
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
                    if new_priority in current_priorities:
                        print('Priority already in use, reassigning priorities.'
                              'Please wait...')
                        reassign_priorities(a)
                        current_priorities = list(a.values())
                        print(a)
                    elif new_priority == 0:
                        return
                    else:
                        a[category_name] = new_priority
                        current_priorities = list(a.values())
                        print(f'{category_name} has been assigned the priority {new_priority}\n')
                        print(a)
                except ValueError:
                    print('Invalid input, please enter an integer (0 to exit)')

            category_name = input('\n Enter the category of which you would like to change priority or 0 to exit: ')
                
def reassign_priorities(category_prioritys, new_priority, category_name):
    sorted_categories = sorted(category_priorities, key=category_priorities.get)

    for priority in sorted_categories:
        if category_priority[priority] >= new_priority:
            category_priority[priority] +=P
def add_data():
    self.first_name = input('First name: ')
    self.last_name = input('Last name: ')
    self.title= input('Title: ')
    


def print_data():
    return Person.people

while True:
    print('Hello what would you like to do?')
    command = input('commands are LIST or ADD: ')

    if command == 'LIST':
        if Person.user_id > 0:
            print_data()
        else:
            print('Sorry there are no contacts')

    elif command == 'ADD':
        add_data()


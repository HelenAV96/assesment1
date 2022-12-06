class Person(object):
    people = []
    user_id = 0

    def __init__(self, first_name, last_name,title):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        Person.user_id += 1
        Person.people.append(self) 

    def __str__(self):
        return 'First name: {}\n last name: {}\n title: {}'.format(self.first_name,self.last_name, self.title)


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


def options():
    print('\nContact Agenda')
    print('1. Add new contact')
    print('2. Delete a existing contact')
    print('3. Search contact')
    print('4. List contacts')
    print('5. Exit')
    print('\n')

def addContact(agenda):
    name = input('Enter a name: ')
    phone = input('Enter a phone number: ')
    email = input('Enter an email address: ')
    agenda[name] = {'phone':phone, 'email':email}
    print(f'This contact "{name}" has been added.')

def removeContact(agenda):
    name = input('Enter a name to delete: ')
    if name in agenda:
        del agenda[name]
        print(f'The contact "{name}" has been deleted.')
    else:
        print(f'Contact "{name}" not found.')

def searchContact(agenda):
    name = input('Enter a name to search: ')
    if name in agenda:
        print(f'Name: {name}')
        print(f'Phone: {agenda[name]['phone']}')
        print(f'Email: {agenda[name]['email']}')
    else:
        print(f'The contact {name} was not found.')

def listContacts(agenda):
    if agenda:
        print('\nList of contacts')
        for name,info in agenda.items():
            print(f'Name: {name}')
            print(f'Phone: {info['phone']}')
            print(f'Email: {info['email']}')
            print('-' * 20)
    else:
        print('The agenda is empty.')

def agendaContacts():
    agenda = {}

    while True:
        options()
        option = input('Choose an option: ')
        print('\n')
        if option == '1':
            addContact(agenda)
        elif option == '2':
            removeContact(agenda)
        elif option == '3':
            searchContact(agenda)
        elif option == '4':
            listContacts(agenda)
        elif option == '5':
            print('Exiting the agenda. Goodbye!')
            break
        else:
            print('Please choose a valid option.')

agendaContacts()
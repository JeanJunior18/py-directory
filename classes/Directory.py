from .Contact import Contact

class Directory():
    def add_contact(name, phone):
            return Contact(name, phone)

    def get_all_contacts(contactList):
        for contact in contactList:
            print(contact)
        print('-------------')

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        self.contacts[name] = phone_number
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for name, phone_number in self.contacts.items():
                print(f"Name: {name}, Phone Number: {phone_number}")

    def search_contact(self):
        name = input("Enter name to search: ")
        if name in self.contacts:
            print(f"Name: {name}, Phone Number: {self.contacts[name]}")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    def update_contact(self):
        name = input("Enter name to update: ")
        if name in self.contacts:
            new_phone_number = input("Enter new phone number: ")
            self.contacts[name] = new_phone_number
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.delete_contact()
        elif choice == '5':
            contact_book.update_contact()
        elif choice == '6':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
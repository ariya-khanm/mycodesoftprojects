contacts = {}

def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("This contact already exists.")
        return
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
    print("Contact added successfully.")

def view_contact_list():
    if not contacts:
        print("No contacts found.")
        return
    print("Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone_number']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ").lower()
    found_contacts = [name for name, details in contacts.items() if keyword in name.lower() or keyword in details['phone_number']]
    if found_contacts:
        print("Search Results:")
        for name in found_contacts:
            details = contacts[name]
            print(f"Name: {name}, Phone: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("No matching contacts found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.")
        return
    print("Enter new details (leave blank to keep current value):")
    phone_number = input(f"New phone number (current: {contacts[name]['phone_number']}): ") or contacts[name]['phone_number']
    email = input(f"New email (current: {contacts[name]['email']}): ") or contacts[name]['email']
    address = input(f"New address (current: {contacts[name]['address']}): ") or contacts[name]['address']
    contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
    print("Contact updated successfully.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Information Program")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__== "__main__":
    main()
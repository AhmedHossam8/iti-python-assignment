import csv
import os
FILE_PATH = './contacts.csv'

def add_contact():

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email'])
        print("contacts.csv file created")
        contacts = []
    
    with open(FILE_PATH, 'r', newline='') as file:
        reader = csv.reader(file)
        contacts = list(reader)[1:]

    while True:
        name = input("Name: ").strip()
        if not name.isalpha():
            print("Enter a valid name")
            continue
        if any(c[0].lower() == name.lower() for c in contacts):
            print("A contact with this name already exists.")
            continue
        break
    
    while True:
        phone = input("Phone: ").strip()
        if not phone.isnumeric():
            print("Enter a valid phone number")
            continue
        if any(c[1] == phone for c in contacts):
            print("A contact with this phone number already exists.")
            continue
        break
    
    while True:
        email = input("Email: ").strip()
        if '@' not in email or '.' not in email:
            print("Enter a valid email address.")
            continue
        if any(c[2].lower() == email.lower() for c in contacts):
            print("A contact with this email already exists.")
            continue
        break

    with open(FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print(f"Contact '{name}' added successfully!")

def view_all_contacts():
    
    if not os.path.exists(FILE_PATH):
        print("The contact file doesn't exist")
        return
    
    with open(FILE_PATH, 'r', newline='') as file:
        reader = csv.reader(file)
        contacts = list(reader)
        
        if len(contacts) <= 1:
            print("No contacts found.")
            return
        
        print("Contacts:")
        for i, contact in enumerate(contacts[1:], start=1):
            print(f"{i}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

def search_contact():
    while True:
        name = input("Name: ").strip()
        if name.isalpha():
            break
        else:
            print("Enter a valid name")
    
    if not os.path.exists(FILE_PATH):
        print("The contact file doesn't exist")
        return
    
    with open(FILE_PATH, 'r', newline='') as file:
        reader = csv.reader(file)
        contacts = list(reader)
        
        if len(contacts) <= 1:
            print("No contacts found.")
            return
        
        found = [c for c in contacts[1:] if c[0].lower() == name.lower()]
    
    if found:
        print("Contacts:")
        for contact in found:
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
    else:
        print("No contact found with that name.")
    
def delete_contact():
    while True:
        name = input("Name: ").strip().lower()
        if name.isalpha():
            break
        else:
            print("Enter a valid name")
    
    if not os.path.exists(FILE_PATH):
        print("The contact file doesn't exist")
        return
    
    with open(FILE_PATH, 'r', newline='') as file:
        reader = csv.reader(file)
        contacts = list(reader)
        
        if len(contacts) <= 1:
            print("No contacts found.")
            return
        
        header = contacts[0]
        found = [c for c in contacts[1:] if c[0].lower() == name]
    
        if not found:
            print("No contact found with that name.")
            return
        
        filtered = [c for c in contacts if c[0].lower() != name]
        
    if filtered:
        des = input("Are you sure you want to delete this contact? (yes/no): ")
        if des.lower() == "yes":
            with open(FILE_PATH, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(filtered)
            print(f"Contact '{name}' deleted successfully.")
        else:
            print("Deletion cancelled")
    else:
        print("No contact found with that name.")

def update_contact():
    
    if not os.path.exists(FILE_PATH):
        print("The contact file doesn't exist")
        return
    
    while True:
        name = input("Name: ").strip()
        if name.isalpha():
            break
        else:
            print("Enter a valid name")
    
    with open(FILE_PATH, 'r', newline='') as file:
        reader = csv.reader(file)
        contacts = list(reader)

        if len(contacts) <= 1:
            print("No contacts found.")
            return

        found_index = None
        for i, c in enumerate(contacts[1:], start=1):
            if c[0].lower() == name.lower():
                found_index = i
                break

    if found_index:
        old_name, old_phone, old_email = contacts[found_index]

        new_name = input(f"New Name (Leave empty to keep '{old_name}'): ").strip()
        if not new_name:
            new_name = old_name
        elif not new_name.isalpha():
            print("Invalid name.")
            return

        new_phone = input(f"New Phone (Leave empty to keep '{old_phone}'): ").strip()
        if not new_phone:
            new_phone = old_phone
        elif not new_phone.isnumeric():
            print("Invalid phone number.")
            return

        new_email = input(f"New Email (Leave empty to keep '{old_email}'): ").strip()
        if not new_email:
            new_email = old_email
        elif '@' not in new_email or '.' not in new_email:
            print("Invalid email address.")
            return

        contacts[found_index] = [new_name, new_phone, new_email]

        with open(FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print(f"Contact '{name}' updated successfully!")
    else:
        print("No contact found with that name.")

def main():
    print("Contact Book Manager")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")
    
    while True:
        choice = int(input("Choice: "))
        
        if choice == 1:
            add_contact()
        
        elif choice == 2:
            view_all_contacts()
        
        elif choice == 3:
            search_contact()
        
        elif choice == 4:
            delete_contact()
        
        elif choice == 5:
            update_contact()
        
        elif choice == 6:
            break
        
        else:
            print("Invalid choice")
            
main()
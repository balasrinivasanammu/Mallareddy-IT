import datetime

class PhoneContactManager:
    def __init__(self):
        self.contacts = {}
        self.call_history = {}

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        self.contacts[name] = phone
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("\nContacts List:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    def update_contact(self):
        name = input("Enter the contact name you want to update: ")
        if name in self.contacts:
            new_phone = input(f"Enter new phone number for {name}: ")
            self.contacts[name] = new_phone
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self):
        name = input("Enter the contact name you want to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

    def log_call(self):
        name = input("Enter contact name you want to log a call for: ")
        if name in self.contacts:
            duration = input("Enter call duration (in minutes): ")
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if name not in self.call_history:
                self.call_history[name] = []
            self.call_history[name].append({"date": date, "duration": duration})
            print(f"Call logged for {name} on {date} with duration {duration} minutes.")
        else:
            print(f"Contact {name} not found.")

    def view_call_history(self):
        name = input("Enter contact name to view call history: ")
        if name in self.call_history:
            print(f"\nCall History for {name}:")
            for call in self.call_history[name]:
                print(f"Date: {call['date']}, Duration: {call['duration']} minutes")
        else:
            print(f"No call history found for {name}.")

    def view_all_call_history(self):
        if self.call_history:
            print("\nAll Call History:")
            for name, calls in self.call_history.items():
                print(f"\n{name}:")
                for call in calls:
                    print(f"  Date: {call['date']}, Duration: {call['duration']} minutes")
        else:
            print("No call history available.")

    def run(self):
        while True:
            print("\nPhone Contact and Call History Management System")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Log Call")
            print("6. View Call History for Contact")
            print("7. View All Call History")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.update_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                self.log_call()
            elif choice == '6':
                self.view_call_history()
            elif choice == '7':
                self.view_all_call_history()
            elif choice == '8':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = PhoneContactManager()
    manager.run()

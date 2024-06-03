def main():
    donor_list = []
    receiver_list = []
    blood_types = ["O -", "O +", "A -", "A +", "B -", "B +", "AB -", "AB +"]

    while True:
        print("\nBlood Bank Management System")
        print("1. Add Donor")
        print("2. Display Donor List")
        print("3. Search Donor by Blood Type")
        print("4. Add Receiver")
        print("5. Display Receiver List")
        print("6. Search Receiver by Blood Type")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_donor(donor_list)
        elif choice == '2':
            display_donor_list(donor_list)
        elif choice == '3':
            search_donor_by_blood_type(donor_list)
        elif choice == '4':
            add_receiver(receiver_list)
        elif choice == '5':
            display_receiver_list(receiver_list)
        elif choice == '6':
            search_receiver_by_blood_type(receiver_list)
        elif choice == '7':
            print("Exiting the Blood Bank Management System. Goodbye!")
            break
        else:
            print("SORRY\nInvalid choice. Please enter a number between 1 and 7.")

def add_donor(donor_list):
    name = input("Enter donor's name: ")
    father_name = input("Enter donor's father's name: ")
    contact_no = input("Enter donor's contact number: ")
    any_disease = input("Enter if donor has any disease (yes/no): ")
    if any_disease.lower() == 'yes':
        print("Sorry, you are not eligible to donate blood.")
        return
    blood_type = input("Enter blood type: ")
    donor_list.append({
        "Name": name,
        "FatherName": father_name,
        "Contact No": contact_no,
        "Any Disease": any_disease,
        "Blood Type": blood_type,
    })
    print("Donor added successfully! \n       Thank you!")

def display_donor_list(donor_list):
    print("\nDonor List:")
    if not donor_list:
        print("No donors available.")
    for donor in donor_list:
        print(f"Name: {donor['Name']},\nFather's Name: {donor['FatherName']},\nContact No: {donor['Contact No']},\nAny Disease: {donor['Any Disease']},\nBlood Type: {donor['Blood Type']}")

def search_donor_by_blood_type(donor_list):
    search_blood_type = input("Enter blood type to search: ").upper()
    matching_donors = [donor for donor in donor_list if donor['Blood Type'].upper() == search_blood_type]

    if not matching_donors:
        print("No donors found with the specified blood type.")
    else:
        print(f"\nDonors with Blood Type {search_blood_type}:")
        for donor in matching_donors:
            print(f"Name: {donor['Name']},\nFather's Name: {donor['FatherName']},\nContact No: {donor['Contact No']},\nAny Disease: {donor['Any Disease']},\nBlood Type: {donor['Blood Type']}")

def add_receiver(receiver_list):
    name = input("Enter receiver's name: ")
    father_name = input("Enter recevier's father's name: ")
    contact_no = input("Enter recevier's contact number: ")
    blood_type = input("Enter blood type: ")
    receiver_list.append({
        "Name": name,
        "Blood Type": blood_type,
        "FatherName": father_name,
        "Contact No": contact_no,
       
    })
    print("Receiver added successfully!\n        THANK YOU!")

def display_receiver_list(receiver_list):
    print("\nReceiver List:")
    for receiver in receiver_list:
        print(f"Name: {receiver['Name']},\nFather's Name: {receiver['FatherName']},\nContact No: {receiver['Contact No']},\nBlood Type: {receiver['Blood Type']}")

def search_receiver_by_blood_type(receiver_list):
    search_blood_type = input("Enter blood type to search: ")
    matching_receivers = [receiver for receiver in receiver_list if receiver['Blood Type'] == search_blood_type]

    if not matching_receivers:
        print("No receivers found with the specified blood type.")
    else:
        print(f"\nReceivers with Blood Type {search_blood_type}:")
        for receiver in matching_receivers:
            print(f"Name: {receiver['Name']},\nFather's Name: {receiver['FatherName']},\nContact No: {receiver['Contact No']}, \nBlood Type: {receiver['Blood Type']}")

if __name__ == "__main__":
    main()
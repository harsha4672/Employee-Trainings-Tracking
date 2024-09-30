# importing required libraries
import json
from datetime import datetime, timedelta

# Helper function to load the data from the JSON file 
def load_data(file_name):
    with open(file_name, 'r') as data_file:
        return json.load(data_file)

# Helper function to convert dates from string to date type
def convert_to_date(date_strng):
    if date_strng:
        return datetime.strptime(date_strng, '%m/%d/%Y')
    return None

# Helper function to filter out the most recent completions of a person from their training record
def get_latest_completions(completions):
    #intializing latest dictionary to store all the latest training entries from a person record
    latest = {}
    
    for completion in completions:
        training_name = completion['name']
        completion_date = convert_to_date(completion['timestamp'])
        if training_name not in latest or completion_date > convert_to_date(latest[training_name]['timestamp']):
            latest[training_name] = completion
            
    return list(latest.values())

# Task 1: To count number of people completed each distinct training available
def count_completed_trainings(training_records):
    #intializing training count as an ouput dictionary
    training_count = {}
    
    for person_record in training_records:
        # Considering latest completions as there can be duplicate training entries in a person record
        completions = get_latest_completions(person_record['completions'])
        for completion in completions:
            training_name = completion['name']
            if training_name in training_count:
                training_count[training_name] += 1
            else:
                training_count[training_name] = 1
                
    return training_count


# Task 2: List of all people who completed a training from the list of trainings given in the specified fiscal year
def trainings_completed_in_fiscal_year(training_records, trainings_to_check, year):
    start_date = datetime(year - 1, 7, 1)
    end_date = datetime(year, 6, 30)
    
    #intializing trainings_by_year dictionary to store the output
    trainings_by_year = {training: [] for training in trainings_to_check}

    for person_record in training_records:
        # Considering latest completions as there can be duplicate training entries in a person record
        completions = get_latest_completions(person_record['completions'])
        
        # Filter the completions that match the given trainings and are within the fiscal year
        for completion in completions:
            if completion['name'] in trainings_to_check:
                completion_date = convert_to_date(completion['timestamp'])
                if start_date <= completion_date <= end_date:
                    trainings_by_year[completion['name']].append(person_record['name'])
    
    return trainings_by_year


# Task 3: List of all people with expired or soon-to-expire trainings by specified date
def find_expired_trainings(training_records, date_to_check):
    
    # Intialzing output dictionary to store all the expired or soon to expire trainings
    output = {}
    
    target_date = convert_to_date(date_to_check)
    warning_date = target_date + timedelta(days=30)

    for person_record in training_records:
        
        # Considering latest completions as there can be duplicate training entries in a person record
        completions = get_latest_completions(person_record['completions'])

        # Intializing expiring_trainings in each iteration to store if the person has any expired or soon to expire trainings 
        expiring_trainings = []
        
        for completion in completions:
            expires_on_date = convert_to_date(completion['expires'])
            
            # condition to check if the training has an expiration date
            if expires_on_date:
                # condition to check if the training has expired
                if expires_on_date < target_date:
                    expiring_trainings.append({
                        'training_name': completion['name'],
                        'expiration_status': 'expired'
                    })
                # condition to check if the training is going to expire within a month of specified date
                elif target_date <= expires_on_date <= warning_date:
                    expiring_trainings.append({
                        'training_name': completion['name'],
                        'expiration_status': 'expires soon'
                    })
        
        # condition to check if expiring_trainings is not null to append if there are any values
        if expiring_trainings:
            output[person_record['name']] = expiring_trainings
    
    return output




# defining main function
if __name__ == '__main__':

    print("Hello! Welcome to the Training Tracker Console Application")

    
    # Ask the user for a file choice
    print("Would you like to provide a JSON file for training records?")
    print("1: Yes, I will provide my own JSON file")
    print("2: No, use the default 'trainings.txt'")
    
    file_choice = input("Enter your choice (1/2): ").strip()
    
    if file_choice == '1':
        file_path = input("Enter the full path of the JSON file (e.g., 'C:/path/to/your/trainings.json'): ")
        try:
            training_records = load_data(file_path)
            print(f"Loaded training records from {file_path}.")
        except FileNotFoundError:
            print(f"File not found: {file_path}. Using default training records.")
            training_records = load_data('trainings.txt')
            print("Loaded default training records from 'trainings.txt'.")
        except json.JSONDecodeError:
            print(f"The file '{file_path}' is not in a readable JSON format. Using default training records.")
            training_records = load_data('trainings.txt')
            print("Loaded default training records from 'trainings.txt'.")
    elif file_choice == '2':
        training_records = load_data('trainings.txt')
        print("Using default training records from 'trainings.txt'.")
    else:
        print("Invalid choice. Using default training records.")
        training_records = load_data('trainings.txt')
    
    
    while True:
        # Interactive task selection
        print("\nPlease select a task to perform:")
        print("1: Count number of people who completed each training")
        print("2: List people who completed specified trainings in a fiscal year")
        print("3: List people with expired or soon-to-expire trainings")
        print("4: Exit")

        # Get user input for task choice
        choice = input("Enter the task number (1/2/3/4): ")
        
        if choice == '1':
            # Task 1: Count completions
            completed_counts = count_completed_trainings(training_records)
            print("\nTraining Completion Count:")
            print(json.dumps(completed_counts, indent=4))

        elif choice == '2':
            # Task 2: Fiscal year-based training completions
            print("\nWould you like to use the default list of trainings?")
            print("1: Yes, use default list (Electrical Safety for Labs, X-Ray Safety, Laboratory Safety Training)")
            print("2: No, I will provide my own list of trainings")

            # User choice for default or custom list
            list_choice = input("Enter your choice (1/2): ")

            if list_choice == '1':
                # Use default list of trainings
                trainings_to_check = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
            elif list_choice == '2':
                # User provides custom list of trainings
                custom_trainings = input("Enter the trainings separated by commas: ")
                trainings_to_check = [training.strip() for training in custom_trainings.split(',')]
            else:
                print("Invalid choice. Using default list of trainings.")
                trainings_to_check = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]

            # Prompt for fiscal year input
            fiscal_year = int(input("\nEnter the fiscal year (e.g., 2024): "))
            trainings_in_fiscal_year = trainings_completed_in_fiscal_year(training_records, trainings_to_check, fiscal_year)
            
            # Display the result
            print(f"\nPeople who completed the specified trainings in fiscal year {fiscal_year}:")
            print(json.dumps(trainings_in_fiscal_year, indent=4))


        elif choice == '3':
            # Task 3: Find expired or expiring trainings
            date_to_check = input("\nEnter the date to check (MM/DD/YYYY, e.g., 10/01/2023): ")
            expired_trainings = find_expired_trainings(training_records, date_to_check)
            print(f"\nPeople with expired or expiring trainings by {date_to_check}:")
            print(json.dumps(expired_trainings, indent=4))

        elif choice == '4':
            # Exit the application
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid task number")

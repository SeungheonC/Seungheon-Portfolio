# data_processing.py
import csv

def load_csv(file_path):
    # Step 1: Initializing an empty list to store data
    data = []

    # Step 2: Opening the CSV file and creating a CSV reader
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)

        # Step 3: Reading the header and converting it to lowercase
        header = next(csv_reader)
        header_lower = [col.lower() for col in header]
        print("Loaded columns:", header_lower)  # Add this line for debugging

        # Step 4: Reading each row and appending it to the data list
        for row in csv_reader:
            data.append(row)

    # Step 5: Returning the loaded data and lowercase header
    return data, header_lower

def search_data(data, header_lower, search_column, user_input):
    # Step 1: Initializing an empty list to store filtered data
    filtered_data = []

    # Step 2: Converting search_column to lowercase
    search_column_lower = search_column.lower()

    # Step 3: Finding possible matches for the search column
    possible_matches = [col for col in header_lower if search_column_lower in col]

    # Step 4: Handling column not found or multiple matches
    if not possible_matches:
        print(f"Error: Column '{search_column}' not found.")
        return filtered_data

    if len(possible_matches) > 1:
        print(f"Multiple possible matches for '{search_column}': {possible_matches}")
        return filtered_data

    # Step 5: Getting the index of the search column
    index = header_lower.index(possible_matches[0])

    # Step 6: Searching for user input in the specified column
    for record in data:
        if user_input == record[index]:
            filtered_data.append(record)

    # Step 7: Returning the filtered data
    return filtered_data

def display_summary(filtered_data):
    # Step 1: Displaying the number of records found
    print(f"Number of records found: {len(filtered_data)}")

def export_to_csv(filtered_data, output_file):
    # Step 1: Getting fieldnames from the first row of filtered data
    fieldnames = filtered_data[0]

    # Step 2: Opening the output file and creating a CSV writer
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Step 3: Writing the header to the output file
        writer.writerow(fieldnames)

        # Step 4: Writing the filtered data to the output file
        writer.writerows(filtered_data)

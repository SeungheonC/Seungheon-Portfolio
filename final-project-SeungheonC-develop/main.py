# main.py
from data_processing import load_csv, search_data, display_summary, export_to_csv

def display_menu():
    print("\nMenu:")
    print("1. Search by specific column")
    print("2. Export filtered data to CSV")
    print("3. Exit")

def main():
    # Step 1: Loading Data
    file_path = "//Users//seungheon//final-project-SeungheonC//NS_Same_Sex_Marriages_by_Age_Group_20231207.csv"
    data, header_lower = load_csv(file_path)  # Receive header_lower

    filtered_data = []

    while True:
        # Step 2: Displaying Menu and User Choice
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            # Step 3: Searching Data
            print("Available columns:")
            print(", ".join(header_lower))
            column = input("Enter the column to search: ").strip()
            user_input = input(f"Enter the value for {column}: ")
            filtered_data = search_data(data, header_lower, column, user_input)
            display_summary(filtered_data)

        elif choice == '2':
            # Step 4: Exporting Data
            if not filtered_data:
                print("Please perform a search before exporting.")
            else:
                export_file = input("Enter the name for the exported CSV file: ")
                export_to_csv(filtered_data, export_file)
                print(f"Filtered data exported to {export_file}")

        elif choice == '3':
            # Step 5: Exiting the Program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()

try:
    # Specify the full path to the CSV file
    csv_file_path = 'C:\\Users\\yehya\\OneDrive\\Desktop\\lab1\\task 6\\books-en.csv'
    
    # Attempt to open the file
    with open(csv_file_path, 'r') as file:
        print("File opened successfully!")
except FileNotFoundError:
    print("File not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")

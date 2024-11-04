from csv import reader
from datetime import datetime
search = input('Author name: ')
limit = int(input('Maximum number of results to display: '))  
target_year = [2014, 2016, 2017]
matching_books = []
with open('books.csv', 'r', encoding='windows-1251', newline='') as csvfile:
    table = reader(csvfile, delimiter=';')
    headers = next(table)
    
    for row in table:
        date_string = row[6]
        
        try:
            date = datetime.strptime(date_string, "%d.%m.%Y %H:%M")  
            year = date.year
        except ValueError:
            print(f"Invalid date format: {date_string}")
            continue  
        if row[3] == search and year in target_year:
            matching_books.append(row)
        
        if len(matching_books) >= limit:
            break

if matching_books:
    print(f'\nBooks by {search} published in 2014, 2016, or 2017 (up to {limit} results):')
    for row in matching_books:
        print(f'{row[1]} \t ({row[6]})')
else:
    print(f'No books by {search} found in 2014, 2016, or 2017.')

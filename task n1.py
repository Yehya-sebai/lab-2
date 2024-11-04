from csv import reader
bold = '\u001b[1m'
underline = '\u001b[4m'
reversed = '\u001b[7m'
reset = '\u001b[0m'
count = 0
with open('books-en.csv', 'r', encoding='windows-1251', newline='') as csvfile:
    table = reader(csvfile, delimiter=';')
    headers = next(table)
    title_index = headers.index('Название')  
    for row in table:
        if len(row[title_index]) > 30:
            count += 1
print(f'{bold}The number of records with a string in the "Название" field longer than 30 characters is{reset}: {bold}{underline}{reversed}{count}{reset}')

import random
from csv import reader
def generate_bibliographic_references():
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = list(reader(csvfile, delimiter=';'))
        random_rows = random.sample(table[1:], 20)

        for i, row in enumerate(random_rows, start=1):
            author = row[3]
            name = row[1]
            year = row[6]
            reference = f"{i}. {author}. {name} - {year}"
            yield reference

with open('bibliographic_references.txt', 'w', encoding='utf-8') as output:
    for reference in generate_bibliographic_references():
        output.write(f'{reference}\n')

print("Bibliographic references generated and saved to 'bibliographic_references.txt'.")

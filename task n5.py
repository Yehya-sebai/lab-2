import csv
csv_file_path = 'books-en.csv'
unique_tags = set()
with open(csv_file_path, 'r', encoding='windows-1251', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tag = row.get('tag', None)
        if tag:
            unique_tags.add(tag)

unique_tags_list = list(unique_tags)

for tag in unique_tags_list:
    print(tag)

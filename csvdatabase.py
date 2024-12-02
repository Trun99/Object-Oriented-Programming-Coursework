import csv

with open('./song_data/datasong.csv', mode='r') as file:
    db = csv.reader(file)
    next(db)

print(db)
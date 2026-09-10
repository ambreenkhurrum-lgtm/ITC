#Build a student grade tracker using a list of dicts — 
# each dict holds name, scores (list), and computed average; 
# sort the list by average descending and print the leaderboard.

students = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [92, 88, 95]},
    {"name": "Charlie", "scores": [76, 82, 80]}
]

for student in students:
    student["average"] = sum(student["scores"]) / len(student["scores"])

students.sort(key=lambda x: x["average"], reverse=True)

for student in students:
    print(f"{student["name"]}, {student["average"]:.2f}")

print('-----------------------------')
# Write a list comprehension that filters even numbers from 
# a range and squares them, then write an equivalent dict 
# comprehension mapping each word in a sentence to its length.

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
word_lengths = {word: len(word) for word in "The quick brown fox jumps over the lazy dog".split()}
print("Even squares:", even_squares)
print("Word lengths:", word_lengths)



#  Read a CSV file with the csv module, parse every row into
#  a dict, compute column averages, and write a summary 
# CSV with the results.

print('-----------------------------')
import csv
data = [
    ['Name', 'Age', 'Gender'],
    ['Anna', 25, 'F'],
    ['Susan', 35, 'F'],
    ['Mark', 42, 'M'],
    ['Alan', 40, 'M']
]

with open('public.csv','w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(data)


with open('public.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Use the os and pathlib modules to walk a directory tree,
#  list all .txt files, and print their sizes in a formatted
#  table.
import os
from pathlib import Path

import os
from pathlib import Path

def show_me_the_path(start_path='./'):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith('.txt'):
                path = Path(root) / file
                size = path.stat().st_size

                print(path, size, "bytes")

print('files in the current directory and subdirectories:')
directory_path = './'
show_me_the_path(directory_path)

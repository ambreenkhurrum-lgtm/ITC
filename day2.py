import json

df = [
    {'Name':'Anna', 'Age':25, 'Gender':'F'},
    {'Name':'John', 'Age':35, 'Gender':'M'},
    {'Name':'Jack', 'Age':45, 'Gender':'M'},
    {'Name':'Susan', 'Age':55, 'Gender':'F'}
]

with open('people.json', 'w') as file:
    json.dump(df,file, indent = 2)

with open('people.json', 'r') as file:
    new_data = json.load(file)

# print(new_data)

print(new_data[0]['Name'])
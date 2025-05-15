import csv

data=[
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25",  "San Francisco"],
    ["Charlie", "35" , "Chicago"]
]

with open("output.csv" , "w", newline="") as file:
    csv_writer = csv.writer(file)
    for row in data:
        csv_writer.writerow(row)


dict_data= [
    ["Name": "Alice" ,"Age":"30", "City": "New York"],
    ["Name": "Bob" ,"Age":"25", "City": "San Francisco"],
    ["Name": "Charline" ,"Age":"35", "City": "Chicago"]
]

with open("output.csv" , "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(dict_data)
with open('output.txt', 'w') as file:
    file.write("Hello World")

with open("log.txt", "r") as file:
    file.write("New Log Entry \n")


with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line input_file:
        output_file.write
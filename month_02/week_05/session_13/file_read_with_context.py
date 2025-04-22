with open("log.txt", "r") as file:
    content = file.read()
    print(content)
with open("log.txt", "r") as file:
    for line in file:
        print(line.rstrip())
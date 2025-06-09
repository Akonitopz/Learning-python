#Read line number 4 from the following file

with open("Test1.txt", "w") as f:
    for x in range(8):
        f.write(f"Line{x+1}\n")


with open("Test1.txt", "r") as f:
    print("Original file contents: ")
    print(f.read())


line_numbers = [3]  
lines = []

with open("Test1.txt", "r") as fp:
    for i, line in enumerate(fp):
        if i in line_numbers:
            lines.append(line.strip())

print(lines)
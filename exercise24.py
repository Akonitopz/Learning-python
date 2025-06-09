#Write a program to check if the given file is empty or not

size = os.stat("test.exe").st_size
if size == 0:
    print("File is empty!")
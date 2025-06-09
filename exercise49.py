# Assign a different name to function and call it through the new name.

def displayStudent(name, age):
    print(name , age)

show_student = displayStudent
main = show_student("Ami", 23)


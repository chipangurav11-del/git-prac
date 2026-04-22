grade = int(input("Enter your marks:"))

def get_grade(grade):
    if grade >= 90 and grade <= 100:
        return "A"
    elif grade >= 60 and grade <= 69:
        return "D"
    elif grade >= 50 and grade <= 59:
        return "E"
    elif grade >= 40 and grade <= 49:
        return "F"
    else:
        return "U"
        
print(str(get_grade(grade)))
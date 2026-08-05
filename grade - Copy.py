def grade(marks):
    total = sum(marks)
    percentage = total / len(marks)
    if percentage >=90:
        grade = "A+"
    elif percentage >=80:
        grade = "A"
    elif percentage >=70:
        grade = "B+"
    elif percentage >=60:
        grade = "B"
    elif percentage >=50:
        grade = "C+"
    elif percentage >=40:
        grade = "C"
    elif percentage >=30:
         grade = "fail"
    return total,percentage,grade
marks = []
for i in range(5):
    mark = int(input(f"enter marks of subject {i+1}:"))
    marks.append(mark)
total, percentage, grade = grade(marks)
print("\n------result-------")
print("total marks:",total)
print("percentage:",percentage)
print("grade:",grade)
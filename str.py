class student:
   def __init__(self, name, marks):
       self.name = name
       self.marks = marks
   def __str__(self):
        return f"student name:{self.name}, marks:{self.marks}"
s = student("sravani",90)
print(s)
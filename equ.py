class student:
  def __init__(self, name):
      self.name = name
  def __eq__(self , other):
      return self.name == other.name
s1 = student("sravani")
s2 = student("sravani")
s3 = student("sravs")
print(s1 == s2)
print(s1 == s3)
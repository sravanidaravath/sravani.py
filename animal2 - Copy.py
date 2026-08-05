class animal:
   def sound(self):
       print("animal make sounds")
class dog(animal):
    def sound(self):
        print("dog barks")
d = dog()
d.sound()
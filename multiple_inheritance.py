class father :
    def gardening(self):
        print("i enjoy gardening")
    def skills(self):
        print("programming,gardening")


class mother:
    def cooking(self):
        print("i love cooking")
    def skills(self):
        print("arts")


class child(father,mother):
    def __init__(self,n):
        self.name=n
        print("i am child ")
    def sport(self):
        print("enjoy sports")
    def display(self):
        print(self.name)
    def skills(self):
        father.skills(self) #without calling these it will only dispaly the child skill only
        mother.skills(self)
        print("cricket")

#child object
ch=child("ihsan Ullah")
ch.display()
ch.gardening()
ch.cooking()
ch.sport()
ch.skills()
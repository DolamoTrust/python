class person:
    def __init__(self, name, age, gender, race):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
    def getname(self):
        print("Name:",self.name)
    def getage(self):
        print("Age:",self.age)
    def getgender(self):
        print("Gender:",self.gender)  
    def getrace(self):
        print("Race:", self.race)  
        pass     
p1 = person("Trust","20","Male","African")   
p2 = person("Jacob","35","Male","African")
i = input("Enter name: ")
if i == "Trust" or "trust":
        p1.getname()
        p1.getage()
        p1.getgender()
        p1.getrace()
print("")
 
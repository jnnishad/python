class student:
    school = "jai school"
    def __init__(self,name,age,m1):
        self.name = name
        self.age = age
        self.m1=m1

    def avg(self):
        return (self.name + self.age + self.m1)/3

s1 = student(541,9,41)
s2 = student(65,62,46)
#c1=computer()
#c2=computer()
#print((s1.name), (s2.name))

print(s2.avg())

class AgeSet:
    square = 2025.0
    birth = 1980.0
    age = 45.0
    def description(self):
        desc_str="People born in %d will be %d years old in %d, %d=%d^%.3f."%(self.birth,self.age,self.square,self.square,self.age,power)
        return desc_str

print('Please enter the age you would like to use.')
a=int(input())
print('Please enter the power you would like to use.')
power=float(input())
c=a**power
b=c-a
outcomes=[a,b,c]
high = AgeSet()
high.age = a
high.birth = b
high.square = c
print(high.description())


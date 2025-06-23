'''
#Write a Python Program to create a SquareShape Class & declare the property as 
#length,breadth.height
#1)Calculate the Area of Square(a*a)
#2)Check Whether the Sides of Square's are equal or not using Instance Methods
#3)Calculate the Perimeter of Square using Instance Methods(4*a)
#4)Find the Diagonals of Square usng Instance Methods(root-2 a)
#5)Find the side length of Square using Instance Methods(perimeter/4)
'''
class SquareShape:
    def __init__(self,length):
        self.length=length
    def area(self):
        print("Area of Square is: ",self.length*self.length)
    def equalside(self):
        self.l1=int(input("Enter the value of 1st side: "))
        self.l2=int(input("Enter the value of 2nd side: "))
        self.l3=int(input("Enter the value of 3rd side: "))
        self.l4=int(input("Enter the value of 4th side: "))
        if(self.l1==self.l2 and self.l1==self.l3 and self.l1==self.l4):
            print("All sides are equal.")
        else:
            print("Not equal.")
    def peri(self):
        print("Perimeter of the Square is: ",4*self.length)
    def diag(self):
        print("The Diagnol Length of the ",1.414*self.length)
    def sidelen(self):
        print("The Side Length of Square is ",(4*self.length)/4)
L=int(input("Enter length of side of Square: "))
Squa=SquareShape(L)
Squa.area()
Squa.equalside()
Squa.peri()
Squa.diag()
Squa.sidelen()
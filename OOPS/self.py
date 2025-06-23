class student:
    def __init__(self):
        pass
    def display(self):
        print(self)
s1=student()
s1.display()
s2=student()
s2.display()
s3=student()
s3.display()


class employ():
    def __init__(self,employname,employID,designation,salary):
        print("object is created")
        self.Employname=employname
        self.EmplyoID=employID
        self.Designation=designation
        self.Salary=salary
    def display_details(self):
        print(self.Employname)
        print(self.EmplyoID)
        print(self.Designation)
        print(self.Salary)
e1=employ('Lalasa','14046','data analyst','20000')
e1.display_details()

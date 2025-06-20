class employ():
    def __init__(self,employname,employID,designation,salary):
        print("object is created")
        self.Employname=employname
        self.EmplyoID=employID
        self.Designation=designation
        self.Salary=salary
def display_details(self):
    print("employ name is : ",(self.Employname))
    print("employ ID is  : ",(self.EmplyoID))
    print("employ designation is :",(self.Designation))
    print("employ salary is : ",(self.Salary))
e1=employ('Lalasa','14046','data analyst','20000')
e2=employ('jhon','1444','developer',30000)
display_details(e1)
display_details(e2)
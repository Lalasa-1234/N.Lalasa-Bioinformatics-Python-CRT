class rectangle:
    def init(self,l,b):
        self.Lenght=l
        self.Breadth=b
        print("Object creation called")
    def Set_Details(self):
        self.Length = self.Lenght
        print(f"Length : {self.Lenght}")
        self.Breadth = self.Breadth
        print(f"Breadth : {self.Breadth}")
R=rectangle(20,19)
R.Set_Details()
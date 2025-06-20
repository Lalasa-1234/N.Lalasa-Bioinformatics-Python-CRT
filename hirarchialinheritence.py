class Graduation():
    def _init_(self):
        print("hehe")
    #@staticmethod
    def Graduate(self):
        print("Congratulations! You are now a Graduate")
#First Sub Class
class CSE(Graduation):
    def _init_(self):
        super()._init_()
        print("haha")
    @staticmethod
    def Graduate():
        print("Congratulations! You are now a Computer Science Graduate")
#Second sub class
class BI(Graduation):
    def _init_(self):
        super()._init_()
        pass
    @staticmethod
    def Graduate():
        print("Congratulations! You are now a Bioinformatician Graduate")
#Third sub class
class ECE(Graduation):
    def _init_(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations! You are now a ECE Graduate")
CSE.Graduate()
BI.Graduate()
ECE.Graduate()
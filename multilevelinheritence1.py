class GrandFather():
    def _init_(self):
        pass
    @staticmethod
    def Properties():
        print("100 Acres of Land")
class Father(GrandFather):
    def _init_(self):
        super()._init_()
    @staticmethod
    def Properties():
        print("50 Acres of Land")
class Yourself(Father):
    def _init_(self):
        super()._init_()
    def Properties():
        print("A Btech Degree🤦‍♂️")
GrandFather.Properties()
Father.Properties()
Yourself.Properties()
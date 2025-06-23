class Father:
    def _init_(self):
        pass
    @staticmethod
    def Work():
        print("Working moather and father")
class Son(Father):
    def _init_(self):
        super()._init_()
    @staticmethod
    def Work():
        print("Enjoying Daughter")
Father.Work()
Son.Work()
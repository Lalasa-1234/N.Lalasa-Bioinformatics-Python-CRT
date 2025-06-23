class mobile:
    def __init__(self):
        print("mobile constructor called")
samsung=mobile()




class mobile:
    def __init__(self):
        self.model = "samsung"
    def show_model(self):
        print("model:",self.model)
samsung=mobile()
samsung.show_model()



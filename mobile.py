class mobile():
    def __init__(self,colour,prize,brand,series,version,features,storage,battery_capacity,processor):
        print("object is created")
        self.Colour=colour
        self.Prize=prize
        self.Brand=brand
        self.Series=series
        self.Version=version
        self.Features=features
        self.Storage=storage
        self.Battery_capacity=battery_capacity
        self.processor=processor
    def set_Colour(self):
        self.Colour='black'
    def display_details(self):
        print("mobile colour :",(self.Colour))
        print("mobile prize :",(self.Prize))
        print("brand : ",(self.Brand))
        print("mobile series :",(self.Series))
        print("version :",(self.Version))
        print("fratures :",(self.Features))
        print("mobile storage:",(self.Storage))
        print("mobile battery capacity :",(self.Battery_capacity))
        print("processor :",(self.processor))
e1=mobile('ice blue','28,000','samsung','A55','a','kjskdjsk','256GB','10hrs','123')
e1.display_details()
print("after updating the colour :")
e1.set_Colour()
e1.display_details()
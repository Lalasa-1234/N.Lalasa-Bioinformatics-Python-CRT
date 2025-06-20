class Duck:
    def walk(self):
        print("quak quak quak ")
class Horse:
    def walk(self):
        print("thabdak thabdak thabdak")
def myfunction(obj):
    obj.walk()
d = Duck()
myfunction(d)
h = Horse()
myfunction(h)
'''  W.A.P.P to simulate the behaviour of a web page  ,back button when a user visits a new page push it to 
the stack when the user clicks back pop the top page and go back to the previous page (implement using a stack)'''

class browser:
    def __init__(self):
        self.history=[]
    def visit(self,page):
        self.history.append(page)
        print(f"visited {page}")
    def undo(self):
        if len(self.history)>1:
            self.history.pop()
            print(f"back to {self.history[-1]}")
        else:
            print("no pages to come back")
browser=browser()
browser.visit('google.com')
browser.visit('linkdin.com')
browser.visit('github.com')
browser.undo()
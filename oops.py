class ok:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    
class done(ok):
    def sm(self):
        print(self.x + self.y)

obj = done(12, 15)

obj.sm()
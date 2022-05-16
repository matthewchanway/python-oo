"""Python serial number generator."""

class SerialGenerator:
    
    def __init__(self,start):
        self.start = start
        self.curr = start
    
    def generate(self):
        print(self.curr+1)
        self.curr = self.curr + 1
        

    def reset(self):
        self.curr = self.start
    
    def __repr__(self):
        print(f"SerialGenerator start={self.start} next={self.curr+1}")
        
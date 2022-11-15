class fruit:
    def __init__(self, type, size):
        """constructor for the class"""
        self.type = type
        self.size = size
    
    def __gt__(self,other):
        if self.size > other.size:
            return True
        else:
            return False
    

orange = fruit("orange", 8)
apple = fruit("apple", 9)

print(orange < apple)

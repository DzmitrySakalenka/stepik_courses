class Buffer:
    def __init__(self):
        self.buff = []


    def add(self, *a):
        self.buff.extend(a)
        
        for _ in range(len(self.buff)//5):
            print(sum(self.buff[0:5]))
            del self.buff[0:5]


    def get_current_part(self):
        return self.buff
    
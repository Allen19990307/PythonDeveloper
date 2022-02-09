from random import randint
class Die:
    """创建一个骰子类"""
    def __init__(self,num_sides = 6):
        """骰子一般就有六个面"""
        self.num_sides = num_sides
    def roll(self):
        """返回一个1和骰子面数之间的随机值"""
        return randint(1,self.num_sides)

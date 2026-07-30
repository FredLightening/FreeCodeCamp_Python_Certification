from math import *

class Rectangle:

    def __init__(self,width:int,height:int):
        self.width=width
        self.height=height

    def set_width(self,new_width):
        if new_width>0:
            self.width=new_width

    def set_height(self,new_height):
        if new_height>0:
            self.height=new_height

    def get_area(self):
        return self.height*self.width

    def get_perimeter(self):
        return 2*(self.width+self.height)

    def get_diagonal(self):
        return sqrt(pow(self.width,2)+pow(self.height,2))

    def get_picture(self):
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        width_rep=self.width*'*'
        # height_rep=self.height+1
        pict_list=[]
        for i in range(self.height):
            pict_list.append(f"{width_rep}")
        pict='\n'.join(pict_list)
        return f"{pict}\n"
        # return '\n'.join(pict_list)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_amount_inside(self,shape):
        height_rep=self.height//shape.height
        width_rep=self.width//shape.width
        return height_rep*width_rep
        

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.side=side
        

    def set_width(self,new_width):
        if new_width>0:
            self.side=new_width

    def set_height(self,new_height):
        if new_height>0:
            self.side=new_height

    def set_side(self,new_side):
        self.height=new_side
        self.width=new_side
        self.side=new_side

    def __str__(self):
        return f"Square(side={self.side})"
    


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

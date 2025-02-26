from point import Point
import math

class Circle:
    #write a docstring here!
    def __init__(self, c=None, r=1):
        #WRITE ME
        pass
    def __str__(self):
        #WRITE ME
        return ""
    def __repr__(self):
        return "Circle"+str(self)
    def move(self, dx, dy):
        #WRITE ME
        #hint: you should be calling move(dx,dy)
        #on the Point that is the center of the circle
        pass
    def intersection_area(self, other_circle):
        #WRITE ME
        #first check if no overlap
        #   if no overlap, return 0
        #next check for total overlap
        #   if so, return area of smaller circle
        #otherwise, use Wolfram formula for partial overlap
        return 0
    pass


if __name__ == "__main__":
    c1=Circle()
    #note that c2 just touches, but does not intersect c1
    c2=Circle(Point(3,4),5)
    c3=Circle(Point(),2)
    c4=Circle(Point(4,5),6)
    c5=Circle(Point(-2,-2),3)
    c6=Circle(Point(3,-3),2)
    circles=[c1, c2, c3, c4, c5, c6]
    for ca in circles:
        print("---")
        print(str(ca))
        print(repr(ca))
        for cb in circles:
            print("{:.8f}".format(ca.intersection_area(cb)))
            pass
        pass
    c1.move(-1,0)
    c2.move(1,1)
    c3.move(2,-4)
    for ca in circles:
        print("---")
        print(str(ca))
        print(repr(ca))
        for cb in circles:
            print("{:.8f}".format(ca.intersection_area(cb)))
            pass
        pass
    pass

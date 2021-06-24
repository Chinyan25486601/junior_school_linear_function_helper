from decimal import Decimal
from typing import Tuple
from sympy import Abs,sqrt,Number,simplify

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

O = Point(0,0)

def get_length_of_segment_from_two_points(p1: Point, p2: Point) :
    return simplify(sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2))

def get_analytic_expression_of_directly_proportional_function_from_one_point(p: Point) :
    return simplify(p.y/p.x)

def get_analytic_expression_of_linear_function_from_two_points(p1: Point, p2: Point):
    k=simplify(Abs(p1.y-p2.y)/Abs(p1.x-p2.x))
    b=simplify(p1.y-k*p1.x)
    return (k,b)

def get_area_of_triangle_from_three_sides(s1, s2, s3) :
    p=simplify((s1+s2+s3)/2)
    return simplify(sqrt(p*(p-s1)*(p-s2)*(p-s3)))

def get_area_of_triangle_from_three_points(p1: Point, p2: Point, p3: Point) :
    p1p2 = get_length_of_segment_from_two_points(p1,p2)
    p2p3 = get_length_of_segment_from_two_points(p2,p3)
    p1p3 = get_length_of_segment_from_two_points(p1,p3)
    return simplify(get_area_of_triangle_from_three_sides(p1p2,p2p3,p1p3))

if __name__=="__main__":
    print(get_length_of_segment_from_two_points(O, Point(1,1)))
    print(get_analytic_expression_of_directly_proportional_function_from_one_point(Point(1,1)))
    print(get_analytic_expression_of_linear_function_from_two_points(Point(0,1),Point(1,2)))
    print(get_area_of_triangle_from_three_sides(1,1, Decimal(2).sqrt()))
    print(get_area_of_triangle_from_three_points(O,Point(0,1),Point(1,1)))
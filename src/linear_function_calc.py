from decimal import Decimal
import numbers
from typing import Tuple



class Point(object):
    def __init__(self, x: numbers.Rational, y: numbers.Rational):
        self.x = Decimal(x)
        self.y = Decimal(y)

O = Point(0,0)

def get_length_of_segment_from_two_points(p1: Point, p2: Point) -> Decimal:
    return ((p1.x-p2.x)**2+(p1.y-p2.y)**2).sqrt()

def get_analytic_expression_of_directly_proportional_function_from_one_point(p: Point) -> Decimal:
    return p.y/p.x

def get_analytic_expression_of_linear_function_from_two_points(p1: Point, p2: Point) -> Tuple[Decimal,Decimal]:
    k=(abs(p1.y-p2.y)/abs(p1.x-p2.x))
    b=p1.y-k*p1.x
    return (k,b)

def get_area_of_triangle_from_three_sides(s1: Decimal, s2: Decimal, s3: Decimal) -> Decimal:
    p=(s1+s2+s3)/Decimal(2)
    return (p*(p-s1)*(p-s2)*(p-s3)).sqrt()

def get_area_of_triangle_from_three_points(p1: Point, p2: Point, p3: Point) -> Decimal:
    p1p2 = get_length_of_segment_from_two_points(p1,p2)
    p2p3 = get_length_of_segment_from_two_points(p2,p3)
    p1p3 = get_length_of_segment_from_two_points(p1,p3)
    return get_area_of_triangle_from_three_sides(p1p2,p2p3,p1p3)

if __name__=="__main__":
    sqrt5=(Decimal(5).sqrt())
    # TODO:去掉误差
    print(Decimal(2).sqrt()**2)

    print(get_length_of_segment_from_two_points(O, Point(3,4)))
    print(get_analytic_expression_of_directly_proportional_function_from_one_point(Point(1,1)))
    print(get_analytic_expression_of_linear_function_from_two_points(Point(0,1),Point(1,2)))
    print(get_area_of_triangle_from_three_sides(1,1, Decimal(2).sqrt()))
    print(get_area_of_triangle_from_three_points(O,Point(0,1),Point(1,1)))
def equilateral(sides):
    if sides[0] == 0:
        return False
    
    is_triangle = sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]
    return is_triangle and (sides[0] == sides[1] and sides[0] == sides[2])


def isosceles(sides):
    is_triangle = sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]
    return is_triangle and (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2])


def scalene(sides):
    is_triangle = sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]
    return is_triangle and (sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2])


def equilateral(sides):
    if not is_a_triangle(sides):
        return False

    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    
    return False


def isosceles(sides):
    if not is_a_triangle(sides):
        return False
    
    if equilateral(sides):
        return True
    elif not scalene(sides):
        return True

    return False


def scalene(sides):
    if not is_a_triangle(sides):
        return False
    
    if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        return True

    return False

def is_a_triangle(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False

    if sides[0] + sides[1] >= sides[2]:
        if sides[1] + sides[2] >= sides[0]:
            if sides[0] + sides[2] >= sides[1]:
                return True
    
    return False
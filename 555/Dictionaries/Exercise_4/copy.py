import math


def circ_area(**kwd):
    """
    Returns the area of the specified circle, defined by the keywords in kwd

    The area of a circle is PI r*r where r is the radius

    The circle may be specified by 'radius' or 'diameter', but not both.  This function
    should intentionally crash (with an AssertionError) if neither 'radius' nor 'diameter'
    are specified, or if they both are.

    Any keyword arguments other than 'radius' or 'diameter' are ignored.

    """
    area = 0

    if 'radius' in kwd:
        assert 'diameter' not in kwd, 'Radius and Diameter cannot both be present'
        area = kwd['radius'] * kwd['radius'] * math.pi
    elif 'diameter' in kwd:
        assert 'radius' not in kwd, 'Radius and Diameter cannot both be present'
        radius = kwd['diameter']/2
        area = radius * radius * math.pi
    assert 'radius' or 'diameter' in kwd, 'Radius or Diameter is required'  # THIS ASSERTION IS NOT WORKING
    assert kwd != {}, 'must have at least one parameter of either Radius or Diameter'
    return area


# result = circ_area(radius=3) #  (28.27433, result)
# print(result)
# result = circ_area(diameter=4) #  returns approx 12.56637
# print(result)
# result = circ_area(radius=3,foo=20) #  returns approx 28.27433
# print(result)
# result = circ_area() #  crashes with AssertionError
# print(result)
result = circ_area(**{'foo': 20, 'bar': 10})
print(result)
#  result = circ_area(radius=2,diameter=4) #  crashes with AssertionError
d = {'radius':3,'foo':20,'bar':10}
result = circ_area(**d)
print(result)
result = circ_area(bar=3,foo=20) #  returns approx 28.27433
print(result)
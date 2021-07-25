import math

def get_sine_angle(o, h):
	return math.degrees(math.asin(o/h))
	
def get_cosine_angle(a, h):
	return math.degrees(math.acos(a/h))

def get_tangent_angle(o, a):
	return math.degrees(math.atan(o/a))
	
def get_opposite_from_sine(h, ang):
	return math.degrees(math.sin(ang))*h
	
def get_hypotenuse_from_sine(o, ang):
	return o/math.degrees(math.sin(ang))
	
def get_adjacent_from_cosine(h, ang):
	return math.degrees(math.cos(ang))*h
	
def get_hypotenuse_from_cosine(a, ang):
	return a/math.degrees(math.cos(ang))
	
def get_opposite_from_tangent(a, ang):
	return math.degrees(math.tan(ang))*a
	
def get_adjacent_from_tangent(o, ang):
	return o/math.degrees(math.tan(ang))
	
print(get_sine_angle(4,5))
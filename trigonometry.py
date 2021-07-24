import math

def get_sine_angle(o, h):
	return math.deg(math.asin(o/h))
	
def get_cosine_angle(a, h):
	return math.deg(math.acos(a/h))

def get_tangent_angle(o, a):
	return math.deg(math.atan(o/a))
	
def get_opposite_from_sine(h, ang):
	return math.deg(math.sin(ang))*h
	
def get_hypotenuse_from_sine(o, ang):
	return o/math.deg(math.sin(ang))
	
def get_adjacent_from_cosine(h, ang):
	return math.deg(math.cos(ang))*h
	
def get_hypotenuse_from_cosine(a, ang):
	return a/math.deg(math.cos(ang))
	
def get_opposite_from_tangent(a, ang):
	return math.deg(math.tan(ang))*a
	
def get_adjacent_from_tangent(o, ang):
	return o/math.deg(math.tan(ang))
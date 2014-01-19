#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
class TriangleError(RuntimeError):
	pass

def triangle(a,b,c):
	x,y,z = sorted([a,b,c])
	if ((a <= 0 or b <= 0 or c <= 0) or (x+y<=z)):
		raise TriangleError('Triangle ', a, b, c, ' is no good!')

	if (a == b == c):
		return 'equilateral'
	elif ((a == b) or (a == c) or (b == c)):
		return 'isosceles'
	else:
		return 'scalene'
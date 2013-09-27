"""Solution to an exercise in Think Python.

Author: Hayley Hansson
"""

def draw_grid2(w,l):
	corner = "+"
	vert_wall = "|    "*w
	edge = "|"
	vertical = "\n"+vert_wall+edge
	h_wall = "+----"*w
	top = h_wall+corner
	quad = vertical*4+"\n"+h_wall+corner
	done = top+quad*l
	print done
w = 2
l = 2
draw_grid2(w,l)
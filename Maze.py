import turtle, random
import turtle
import random

# --- Configuration ---
length = 300
height = 300
scale = 15
strange = False
solve = True

# --- Global variables ---
grid_list = []
visit = []
visited = []
rows = length // scale
heights = height // scale
total = rows * heights


for counter in range(total):
    grid_list.append(counter)
    visit.append(0)
    visited.append(0)
def tset():
    global t, wn
    wn = turtle.Screen()
    wn.bgcolor("black")
    t = turtle.Turtle()

    t.speed(3)
    t.pensize(int(scale * 0.7))
    t.color("grey")



def main():
    tset()

main()


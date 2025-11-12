
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

def NESW(current):
    global strange
    cords = [current + rows, current + 1, current - rows, current - 1]
    stats = []

    for i in cords:
        if i < 0 or i >= total or (i // rows != current // rows and i % rows != current % rows):
            stats.append(3)  # impossible move
        else:
            stats.append(visit[i])

    if visit[current] <= min(stats):
        return visited[current]

    min_count = stats.count(min(stats))
    options = [1, 3]
    choice = options[random.randint(0, 1)]

    if strange and min_count == choice:
        return visited[current]

    NESW_choice = random.randint(0, min_count - 1)
    counter = 0
    for idx, val in enumerate(stats):
        if val == min(stats):
            if counter == NESW_choice:
                visit[cords[idx]] += 1
                visited[cords[idx]] = current
                return cords[idx]
            counter += 1

# --- Turtle setup ---
def tset():
    global t, wn
    wn = turtle.Screen()
    wn.bgcolor("black")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(int(scale * 0.7))
    t.color("grey")
    t.up()
    t.goto((-.5 * rows) * scale, (-.5 * heights) * scale)
    t.down()

# --- Maze generation ---
def generate():
    visit[0] = 1
    previous = 0
    while min(visit) == 0:
        previous = NESW(previous)
        t.goto(((previous % rows) - .5 * rows) * scale, ((previous // rows) - .5 * heights) * scale)

def StartStop():
    t.pensize(int(scale * 0.6))
    t.up()
    t.goto((-.5 * rows) * scale, (-.5 * heights) * scale)
    t.down()
    t.seth(180)
    t.color("green")
    t.forward(scale)
    t.up()

    path = grid_list[-1]
    t.goto(((path % rows) - .5 * rows) * scale,
           ((path // rows) - .5 * heights) * scale)
    t.down()
    t.color("red")
    t.seth(0)
    t.forward(scale)
    t.up()
    t.backward(scale)

def solver():
    path = grid_list[- 1]
    t.down()
    t.color("red")
    while path != 0:
        path = visited[path]
        t.goto(((path % rows) - .5 * rows) * scale, ((path // rows) - .5 * heights) * scale)


def main():
    tset()
    generate()
    StartStop()
    if solve:
        solver()
    wn.exitonclick()
main()

# --- Maze solver ---

# --- Main ---

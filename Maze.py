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

# --- Maze directions (NESW) ---
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


def main():

main()


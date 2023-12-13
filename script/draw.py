import matplotlib.pyplot as plt
import math
import time

def parse(file_path):
    movement = []
    angle = 0
    with open(file_path, 'r') as file:
        for line in file:
            if "Tourne gauche" in line:
                angle += int(line.split(" ")[3])
            if "Tourne droite" in line:
                angle -= int(line.split(" ")[3])
            if "Avance" in line:
                distance = int(line.split(" ")[1])
                movement.append((angle, distance))
            if "Recule" in line:
                distance = int(line.split(" ")[1])
                movement.append((angle, -distance))
    return movement

def cal_pos(movement):
    x, y = 0, 0
    positions = []

    for angle, distance in movement:
        # Convert angle to radians and calculate new position
        rad = math.radians(angle)
        x += distance * math.cos(rad)
        y += distance * math.sin(rad)
        positions.append((x, y))

    return positions

def plot_path(file_path):
    """ Plot the path based on instructions in the given file. """
    movements = parse(file_path)
    positions = cal_pos(movements)
    x_vals, y_vals = zip(*positions)
    plt.plot(x_vals, y_vals, marker='.')
    plt.grid(True)
    plt.show()
plot_path('turtle')
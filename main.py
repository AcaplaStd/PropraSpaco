# Open-source universe simulator
# by Alex von Sup & Acapla Studios


import turtle
from time import sleep


class Star:  # Class for stars, planets, moons, etc.
    def __init__(self, radius: int=10, mass: int=1, x: int=0, y: int=0, vx: int=0, vy: int=0):
        self.radius = radius  # visual radius
        self.mass = mass  # relative mass in fictional units
        self.x = x  # coordinates
        self.y = y
        self.vx = vx  # velocity (horizontal&vertical components)
        self.vy = vy


stars = [Star()]  # list of all stars in the universe
vel_k = 1  # velocity coefficient
frame = 1 / 60  # duration of a frame


def recount():
    global stars
    for i in range(len(stars)):
        this = stars[i]
        this.vx, this.vy = 0, 0
        for j in range(len(stars)):
            if j == i:
                continue
            sec = stars[j]
            dx = sec.x-this.x
            dy = sec.y-this.y
            r = (dx**2 + dy**2) ** 0.5  # distance between 2 stars (R)
            g = sec.mass * vel_k // r  # gravity!
            this.vx += dx * g
            this.vy += dy * g


def redraw():
    global stars
    for i in range(len(stars)):  # clear old stars
        turtle.undo()
    for i in range(len(stars)):  # visits new star position
        this = stars[i]
        turtle.setpos(this.x, this.y)
        turtle.setheading(0)
        turtle.fd(this.vx)
        turtle.setheading(90)
        turtle.fd(this.vy)
        this.x, this.y = turtle.pos()
    for i in range(len(stars)):  # draws stars
        this = stars[i]
        turtle.setpos(this.x, this.y)
        turtle.dot(this.radius * 2)


def init():  # input data & save it
    global stars
    e = ''
    while True:
        e = input()
        if e == 'start':
            break
        e = e.split()  # example of inputted line: 0 mass 10; means that mass of 1st star is 10
        i = int(e[0])
        prop = e[1]
        val = int(e[2])
        stars += [Star()] * (i - len(stars)+1)  # add new elements to the list if i is very big
        if prop == 'radius':
            stars[i].radius = val
        elif prop == 'mass':
            stars[i].mass = val
        elif prop == 'x':
            stars[i].x = val
        elif prop == 'y':
            stars[i].y = val
        elif prop == 'vx':
            stars[i].vx = val
        elif prop == 'vy':
            stars[i].vy = val
    turtle.speed(0)


if __name__ == '__main__':
    init()
    while True:
        recount()
        redraw()
        turtle.setpos(0, 0)
        sleep(frame)

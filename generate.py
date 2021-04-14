from draw import *
from matrix import *
from math import radians


def string(edges):
    ans = ''
    for i in range(0, len(edges), 2):
        ans += 'line\n'
        ans += ' '.join(list(map(lambda x: str(int(x)), edges[i][:-1] + edges[i + 1][:-1]))) + '\n'
    return ans


def dOnuT():
    for i in range(0, 360, TURN):
        matrix_mult(make_rotY(radians(TURN)), edges)
        matrix_mult(make_rotX(radians(20)), edges)
        matrix_mult(make_rotZ(radians(20)), edges)
        matrix_mult(make_translate(325, 0, 0), edges)
        file.write(string(edges))
        matrix_mult(make_translate(-325, -0, 0), edges)
        matrix_mult(make_rotZ(radians(-20)), edges)
        matrix_mult(make_rotX(radians(-20)), edges)


TURN = 4
file = open('script2.txt', 'w')
edges = []
add_circle(edges, 150, 250, 0, 100, 0.01)
dOnuT()
edges = []
add_circle(edges, 150, 250, 0, 65, 0.01)
dOnuT()
edges = []
add_circle(edges, 150, 250, 0, 30, 0.01)
dOnuT()


file.write('display\n')
file.write('save\n04.png\n')
file.write('quit\n')
file.close()

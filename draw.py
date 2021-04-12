from display import *
from matrix import *
from math import cos, sin, pi

def add_circle( points, cx, cy, cz, r, step ):
    t=0
    while t<1:
        x = r*cos(t*2*pi)+cx
        y = r*sin(t*2*pi)+cy
        z = cz
        x2 = r * cos((t+step) * 2 * pi) + cx
        y2 = r * sin((t+step) * 2 * pi) + cy
        z2 = cz
        add_edge(points,x,y,z,x2,y2,z2)
        t += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    ax,bx,cx,dx = 0,0,0,0
    ay,by,cy,dy = 0,0,0,0
    if curve_type=='hermite':
        ax = 2*x0 - 2*x1 + x2 + x3
        ay = 2 * y0 - 2 * y1 + y2 + y3
        bx = -3 * x0 + 3 * x1 - 2*x2 - x3
        by = -3 * y0 + 3 * y1 - 2 * y2 - y3
        cx = x2
        cy = y2
        dx = x0
        dy = y0
    else:
        ax = -x0+3*x1-3*x2+x3
        ay = -y0 + 3 * y1 - 3 * y2 + y3
        bx = 3*x0 - 6*x1 + 3*x2
        by = 3 * y0 - 6 * y1 + 3 * y2
        cx = -3*x0 + 3*x1
        cy = -3 * y0 + 3 * y1
        dx = x0
        dy = y0

    cubic = lambda: (ax*t**3 + bx*t**2 + cx*t + dx, ay*t**3 + by*t**2 + cy*t + dy)
    t=0
    while t<1:
        x, y = cubic()
        t+=step
        x2, y2 = cubic()
        add_edge(points,x,y,0,x2,y2,0)
    pass


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line

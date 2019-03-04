from display import *
from draw import *
from parser import *
from matrix import *
def parse_file( fname, points, transform, screen, color ):
    a=open(fname,'r')
    p=a.readlines()
    i=0
    while i<len(p):
        comp=p[i].strip('\n')
        if comp=='line':
            point=p[i+1].strip('\n').split(' ')
            b=[int(z) for z in point]
            add_edge(points,b[0],b[1],b[2],b[3],b[4],b[5])
            i+=1
        elif comp=='color':
            color=[int(y) for y in p[i+1].strip('\n').split(' ')]
            i+=1
        elif comp=='ident':
            ident(transform)
        elif comp=='translate':
            trn=p[i+1].strip('/n').split(' ')
            trns=[int(z) for z in trn]
            matrix_mult(make_translate(trns[0],trns[1],trns[2]),transform)
            i+=1
        elif comp=='scale':
            trn=p[i+1].strip('/n').split(' ')
            trns=[int(z) for z in trn]
            matrix_mult(make_scale(trns[0],trns[1],trns[2]),transform)
            i+=1
        elif comp=='rotate':
            b=p[i+1].strip('\n').split(' ')
            theta=b[1]
            if b[0]=='x':
                matrix_mult(make_rotX(float(theta)),transform)
            elif b[0]=='y':
                matrix_mult(make_rotY(float(theta)),transform)
            elif b[0]=='z':
                matrix_mult(make_rotZ(float(theta)),transform)
            i+=1
        elif comp=='apply':
            matrix_mult(transform,points)
        elif comp=='display':
            screen=new_screen()
            print(points)
            draw_lines(points, screen, color)
            #display(screen)
        elif comp=='save':
            sav=p[i+1].strip('\n')
            screen=new_screen()
            draw_lines(points, screen, color)
            save_ppm(screen,sav)
            print('saved')
            i+=1
        elif comp=='quit':
            print(points)
            break
        i+=1
    a.close()
            
screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
parse_file('script', edges, transform, screen, color)

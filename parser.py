from display import *
from matrix import *
from draw import *
def foo():
    print('g')
def parse_file( fname, points, transform, screen, color ):
    a=open(fname,'r')
    p=a.readlines()
    i=0
    while i<len(a.readlines()):
        comp=p[i].strip('\n')
        print(comp)
        if comp=='line':
            point=p[i+1].split(',')
            points.append(line(a[0],a[1],a[2],a[3],a[4],a[5]))
            print('line made')
            i+=1
        elif comp=='ident':
            ident(transform)
        elif comp=='translate':
            trns=p[i+1].split(',')
            transform=matrix_mult(make_translate(trns[0],trns[1],trns[2]),transform)
            i+=1
        elif comp=='rotate':
            b=p[i+1].split(',')
            theta=b[1]
            if b[0]=='x':
                transform=matrix_mult(make_rotX(theta),transform)
            elif b[0]=='y':
                transform=matrix_mult(make_rotY(theta),transform)
            elif b[0]=='z':
                transform=matrix_mult(make_rotZ(theta),transform)
            i+=1
        elif comp=='apply':
            points=matrix_mult(transform,points)
        elif comp=='display':
            screen=new_screen()
            draw_lines(points, screen, color)
            display(screen)
        elif comp=='save':
            save=p[i+1]
            screen=new_screen()
            draw_lines(points, screen, color)
            save(screen,save)
            print('saved')
            i+=1
        elif comp=='quit':
            break
        i+=1
    a.close()
            
        

import pygame, math
import pygame.draw


pygame.init()
taille_fenetre = (1505,700)
screen_surface = pygame.display.set_mode(taille_fenetre)
x=800
y=544
angle=65

rebond=False
screen_surface.fill((255,255,255))
screen_surface.fill((255, 255, 255))
continuer=True


def quit_o(continuer):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        else:
            continuer= True
    return(continuer)


def changeangle(angle,teta):

    angle=angle+180-2*teta

    #if angle>=360:
     #   while angle >=360:
      #      angle=abs(angle-360)
    #if angle <=0:
     #  angle=angle+360

    print(angle)
    return (angle)


def angle_(x,y,angle,rebond):
    rad=(math.cos(math.radians(angle)))
    rad1=(math.sin(math.radians(angle)))

    x=x+rad
    y=y-rad1

    return(x,y)


def plus1 (x,y,angle):
    rad = (math.cos(math.radians(angle)))
    rad1 = (math.sin(math.radians(angle)))
    x = x + rad
    y = y - rad1

    if  math.sqrt((800 - x) ** 2 + (375 - y) ** 2) < 170 :
        return(True)
    else :
        return(False)

teta=90-angle
l=[0,0]
while continuer:
    continuer = quit_o(continuer)
    pygame.display.flip()
    bon=plus1(x,y,angle)
    if bon :
        x,y=angle_(x,y,angle,rebond)
    else :
        angle = changeangle(angle,teta)

        #x, y = angle_(x, y, angle, rebond)

    pygame.draw.circle(screen_surface,(255,0,0),(800,375),170,width=1)
    pygame.draw.line(screen_surface, (0, 0, 255), (x,  y), (x, y),2)

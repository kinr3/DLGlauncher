from Objects import *
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
display_width = 1260
display_height = 860
screen = pygame.display.set_mode((display_width, display_height), HWSURFACE | DOUBLEBUF | RESIZABLE | RLEACCEL)
pygame.display.set_caption('launcher')

'---------------FPS-----------------'
fps = pygame.time.Clock()
FPS = 30
'---------------mouse---------------'
mouse_ = Mouse(['mouse0.png', 'mouse1.png'], screen)

'---DynamicPositionAssignment--dpa--'
dpa = DynamicPositionAssignment(screen, (display_width, display_height))
dpa.set_relation((display_width, display_height))
'-------------text------------------'
text = Text(screen)

'---------------bg-----------------'
bg = Background(screen, 'Bg1.png', dpa)
bg.add_bg('bg_main.png')

'------------Resize----------------'
resize = []

'------------Button----------------'
b_start = Button(screen, ['B_start0.png', 'B_start1.png'], (40, 80), (30, 10), dpa)
resize.append(b_start)
'---------------Bid----------------'


def launcher():
    launcher_true = True
    size = display_width, display_height
    while launcher_true:
        mouse = pygame.mouse.get_pos()
        mouse_clikl = pygame.mouse.get_pressed()[0]
        mouse_clikr = pygame.mouse.get_pressed()[2]
        pygame.display.set_caption("Launcher. FPS: %.2f" % (fps.get_fps()))
        '#mouse = pygame.mouse.get_pos()'
        for event in pygame.event.get():
            '#print(event, event.type)'
            if event.type == 2:
                pass
            if event.type == 12:
                '#exit'
                launcher_true = False
            elif event.type == VIDEORESIZE:
                size = event.dict['size']
                dpa.set_relation(event.dict['size'])
                for re in resize:
                    re.resize()
        '---------print------------'
        '#Bg'
        screen.fill((138,138,138))
        bg.show(size, 1)
        '# MapGen'
        '# Button'
        if b_start.show(mouse_.mouse_get_rect(mouse), mouse_clikl):
            print('mouse_clikl', mouse)
        '# Mouse'
        mouse_.show_m(mouse, mouse_clikl)
        '# update'
        if mouse_clikl:
            print(mouse, '##%.2f, %.2f' % dpa.pix_to_pro(mouse))
        pygame.display.flip()
        fps.tick(FPS)


launcher()

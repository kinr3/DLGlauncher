from Objects import *
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
display_width = 1260
display_height = 860
screen = pygame.display.set_mode((display_width, display_height), HWSURFACE | DOUBLEBUF | RESIZABLE | RLEACCEL)
pygame.display.set_caption('launcher')
#.set_all(sla=True, p_on_p=dpa.pro_to_pix((0.00, 15.47)), wh=(dpa.pro_to_pix((24.92, 73.60))))
'---------------FPS-----------------'
fps = pygame.time.Clock()
FPS = 30
'---------------mouse---------------'
mouse_ = Mouse(['Mauszeiger.png', 'Mauszeiger1.png'], screen)

'---DynamicPositionAssignment--dpa--'
dpa = DynamicPositionAssignment(screen, (display_width, display_height))
dpa.set_relation((display_width, display_height))
'-------------text------------------'
text = Text(screen)

'---------------bg-----------------'
bg = Background(screen, 'Launcher.png', dpa)
bg.add_bg('Launcher1.png')


'------------Button----------------'
#b_start = Button(screen, ['B_start0.png', 'B_start1.png'], (40, 80), (30, 10), dpa)
'--------------register-------------'
checkbox_agb = Objects()


menu = Objects()
menu.set_all(sla=True, p_on_p=dpa.pro_to_pix((99.44, 3.02)), wh=(dpa.pro_to_pix((-2.22, -2.09))))

'---------------Bid----------------'


def launcher():
    launcher_true = True
    size = display_width, display_height
    strt = (0, 0)
    xy = (1, 1)
    strt_ = True
    while launcher_true:
        mouse = pygame.mouse.get_pos()
        mouse_clikl = pygame.mouse.get_pressed()[0]
        mouse_clikr = pygame.mouse.get_pressed()[2]
        pygame.display.set_caption("Launcher. FPS: %.2f" % (fps.get_fps()))
        '#mouse = pygame.mouse.get_pos()'
        events = pygame.event.get()
        for event in events:
            print(event, event.type)
            if event.type == 6:
                if strt_:  # red bpx
                    strt_ = False  # red bpx
                    strt = dpa.pix_to_pro(mouse)  # red bpx
                    xy = (1, 1)
                else:  # red bpx
                    strt_ = True
                    xy = dpa.pix_to_pro(mouse)[0] - strt[0], dpa.pix_to_pro(mouse)[1] - strt[1]  # red bpx
                    print('.set_all(sla=True, p_on_p=dpa.pro_to_pix((%.2f, %.2f)),' % strt,  # red bpx
                          'wh=(dpa.pro_to_pix((%.2f, %.2f))))' % xy)  # red bpx
                if event.type == 12:
                    '#exit'
                    launcher_true = False
        '---------print------------'
        '#Bg'
        screen.fill((138, 138, 138))
        bg.show(size, 1)
        '# MapGen'
        '# Button'
        #if b_start.show(mouse_.mouse_get_rect(mouse), mouse_clikl):
        #    print('mouse_clikl', mouse)
        '# Mouse'
        pygame.draw.rect(screen, (200, 0, 0), (dpa.pro_to_pix(strt), (dpa.pro_to_pix((xy)))))  # red bpx
        mouse_.show_m(mouse, mouse_clikl)
        '# update'
        if mouse_clikl:
            print(mouse, '##%.2f, %.2f' % dpa.pix_to_pro(mouse))
        pygame.display.flip()
        fps.tick(FPS)


launcher()
pygame.quit()

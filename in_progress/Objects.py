import pygame


class Background:

    def __init__(self, screen, image_n, dpa):
        img = pygame.image.load('image/' + str(image_n)).convert_alpha()
        self.screen = screen
        self.Bglist = [img]
        self.Bglist_ = [image_n]
        self.i = 0
        self.dpa = dpa

    def add_bg(self, image_n):
        img = pygame.image.load('image/' + str(image_n)).convert_alpha()
        self.Bglist.append(img)
        self.Bglist_.append(image_n)

    def remove_bg(self, image_n):
        img = pygame.image.load('image/' + str(image_n)).convert_alpha()
        self.Bglist.remove(img)
        self.Bglist_.remove(image_n)

    def get_list(self):
        return self.Bglist_

    def show(self, size, num=0):
        img = pygame.transform.scale(self.Bglist[num], size)
        self.screen.blit(img, (0, 0))


class DynamicPositionAssignment:
    def __init__(self, screen, size):
        self.screen = screen
        w = size[0] / 100
        h = size[1] / 100
        self.relation = {'pxW': w,
                         'pxH': h}

    def pro_to_pix(self, wh):
        pix_w = wh[0] * self.relation['pxW']
        pix_h = wh[1] * self.relation['pxH']
        return pix_w, pix_h

    def pix_to_pro(self, wh):
        pro_w = wh[0] / self.relation['pxW']
        pro_h = wh[1] / self.relation['pxH']
        return pro_w, pro_h

    def rect_to_pro(self, rect):
        pw = 0
        ph = 0
        try:
            pw = rect[2] - rect[0]
            ph = rect[3] - rect[1]
            pw = pw / self.relation['pxW']
            ph = ph / self.relation['pxH']
        except ZeroDivisionError as z:
            pass
        return pw, ph

    def set_relation(self, size):
        w = size[0] / 100
        h = size[1] / 100
        self.relation = {'pxW': w,
                         'pxH': h}

    def assignment(self, wh):
        return int(wh[0] * self.relation['pxW']), int(wh[1] * self.relation['pxH'])

    def assignment_img(self, img, wh):
        return pygame.transform.scale(img, self.assignment(wh))

    def set_img_to_pro(self, img, pro):
        return pygame.transform.scale(img, (int(pro[0] * self.relation['pxW']), int(pro[1] * self.relation['pxH'])))


class Text:

    def __init__(self, screen):
        self.screen = screen
    def show(self, text, xy, color=(0, 0, 0), size=30, text_type='Arial.ttf'):
        self.screen.blit(pygame.font.SysFont(text_type, size)
                         .render(str(text), False, color), xy)


class Objects:

    def __init__(self):
        self.mode = {'color': (255, 255, 255), 's_l_a': False,
                     'py': False, 'wh': (0, 0),'pro': (0, 0), 'p_on_p_pro': (0, 0), 'p_on_p': (0, 0),
                     'on_hit': False, 'object': None}

    def set_all(self, color=(255, 255, 255), py=False, sla=False, wh=(0, 0), p_on_p=(0, 0), obj=None, pro=(0, 0), p_on_p_pro=(0, 0)):
        self.mode['color'] = color
        self.mode['py'] = py
        self.mode['s_l_a'] = sla
        self.mode['wh'] = wh
        self.mode['p_on_p'] = p_on_p
        self.mode['object'] = obj
        self.mode['pro'] = pro
        self.mode['p_on_p_pro'] = p_on_p_pro

    def set_color(self, color):
        self.mode['color'] = color

    def set_py(self, py):
        self.mode['py'] = py

    def set_sla(self, sla):
        self.mode['s_l_a'] = sla

    def set_wh(self, wh):
        self.mode['wh'] = wh

    def set_ponp(self, p_on_p):
        self.mode['p_on_p'] = p_on_p

    def set_pro(self, pro):
        self.mode['pro'] = pro

    def set_ponp_pro(self, p_on_p_pro):
        self.mode['p_on_p_pro'] = p_on_p_pro

    def set_obj(self, objects):
        self.mode['object'] = objects

    def test_on_hit_l(self, x, y):
        if self.mode['p_on_p'][0]+self.mode['wh'][0] >= x >= self.mode['p_on_p'][1] \
                and self.mode['p_on_p'][0]+self.mode['wh'][1] >= y >= self.mode['p_on_p'][1] \
                and self.mode['p_on_p'][0]+self.mode['wh'][0] >= y <= self.mode['p_on_p'][1]+self.mode['wh'][1] \
                and self.mode['p_on_p'][0] <= x >= self.mode['p_on_p'][1]:
            self.mode['on_hit'] = True
        else:
            self.mode['on_hit'] = False
        return self.mode['on_hit']

    def load(self):
        return self.mode

    def g_rect(self):
        return pygame.Rect(self.mode['p_on_p'][0], self.mode['p_on_p'][1], self.mode['wh'][0], self.mode['wh'][1])


class Collision:

    def __init__(self):
        self.collision_ = False
        self.list1 = []

    def set_fix(self, ob2):
        ob2.mode = ob2.load()
        list1 = []
        for i in range(ob2.mode['wh'][0]+1):
            x = i + ob2.mode['p_on_p'][0]
            y = 0

            for i1 in range(ob2.mode['wh'][1]+1):
                y = i1 + ob2.mode['p_on_p'][1]
                list1.append((x, y))

        self.list1 = list1

    def collision_f(self, ob1):
        i2 = 0
        ob1.mode = ob1.load()
        while i2 != self.list1.__len__():
            a = self.list1[i2]
            i2 += 1
            if ob1.test_on_hit_l(a[0], a[1]):
                return True, a
            else:
                pass
        return False, None

    def collision(self, ob1, ob2):
        ob1.mode = ob1.load()
        ob2.mode = ob2.load()
        ob2.list = []
        a = 0
        for i in range(ob2.mode['wh'][0]+1):
            x = i + ob2.mode['p_on_p'][0]
            if i == 0 or i == ob2.mode['wh'][0]:
                a = 1

            for i1 in range(ob2.mode['wh'][1]+1):
                y = i1 + ob2.mode['p_on_p'][1]
                if a == 1:
                    ob2.list.append((x, y))
                    a = 0
                elif i1 == 0 or i1 == ob2.mode['wh'][1]:
                    ob2.list.append((x, y))
                    a = 0
        i2 = 0
        while i2 != ob2.list.__len__():
            a = ob2.list[i2]
            i2 += 1
            if ob1.test_on_hit_l(a[0], a[1]):
                return True, a
            else:
                pass
        return False, None

    @staticmethod
    def coll_rect(ob1, ob2):
        rect1 = ob1.g_rect()
        rect2 = ob2.g_rect()
        return rect1.colliderect(rect2)

    @staticmethod
    def coll_self(ob1, rect2):
        rect1 = ob1.g_rect()
        return rect1.colliderect(rect2)

    @staticmethod
    def coll_s_rect(rect1, rect2):
        return rect1.colliderect(rect2)


class Mouse:

    def __init__(self, img_s, screen):
        mouse = pygame.transform.scale(pygame.image.load('image/' + str(img_s[0])).convert_alpha(), (20, 20))
        mouse1 = pygame.transform.scale(pygame.image.load('image/' + str(img_s[1])).convert_alpha(), (20, 20))
        self.mouse = mouse, mouse1
        self.screen = screen
        pygame.mouse.set_visible(False)

    def mouse_get_rect(self, mouse):
        return self.mouse[0].get_rect().move(mouse)

    def show_m(self, mouse, click):
        if click:
            pass
            self.screen.blit(self.mouse[1], mouse)
        else:
            pass
            self.screen.blit(self.mouse[0], mouse)


class TextBox(Objects, Collision, Text):

    def __init__(self, screen, names, point, wh, dpa):
        Objects.__init__(self)
        Collision.__init__(self)
        self.screen = screen
        self.dpa = dpa
        self.pwh = dpa.pro_to_pix(wh)
        self.p_point = dpa.pro_to_pix(point)
        self.set_all(wh=self.pwh, p_on_p=self.p_point, pro=wh, p_on_p_pro=point)
        self.img = self.dpa.set_img_to_pro(pygame.image.load('image/' + str(names[0])).convert_alpha(), wh)
        self.img1 = self.dpa.set_img_to_pro(pygame.image.load('image/' + str(names[1])).convert_alpha(), wh)


class Image:

    def __init__(self, screen, name, pos, wh, dpa):
        self.pos = pos
        self.b_pos = dpa.pro_to_pix(pos)
        self.wh = wh
        self.dpa = dpa
        self.screen = screen
        self.name = name
        self.img = pygame.image.load('image/'+str(name)).convert_alpha()

    def show(self):
        img = self.dpa.set_img_to_pro(self.img, self.wh)
        self.screen.blit(img, self.dpa.pro_to_pix(self.pos))


class Button(Objects, Collision):

    def __init__(self, screen, names, point, wh, dpa):
        Objects.__init__(self)
        Collision.__init__(self)
        self.screen = screen
        self.dpa = dpa
        self.pwh = dpa.pro_to_pix(wh)
        self.p_point = dpa.pro_to_pix(point)
        self.set_all(wh=self.pwh, p_on_p=self.p_point, pro=wh, p_on_p_pro=point)
        self.img = self.dpa.set_img_to_pro(pygame.image.load('image/' + str(names[0])).convert_alpha(), wh)
        self.img1 = self.dpa.set_img_to_pro(pygame.image.load('image/' + str(names[1])).convert_alpha(), wh)
        #print(self.dpa.rect_to_pro(self.img.get_rect()))

    def resize(self):
        self.pwh = self.dpa.pro_to_pix(self.mode['pro'])
        self.p_point = self.dpa.pro_to_pix(self.mode['p_on_p_pro'])
        self.set_wh(self.pwh)
        self.set_ponp(self.p_point)

    def show(self, m_rect, click):
        img = self.dpa.set_img_to_pro(self.img, self.mode['pro'])
        self.screen.blit(img, self.dpa.pro_to_pix(self.mode['p_on_p_pro']))
        if self.coll_self(self, m_rect):
            img1 = self.dpa.set_img_to_pro(self.img1, self.mode['pro'])
            self.screen.blit(img1, self.dpa.pro_to_pix(self.mode['p_on_p_pro']))
        if click == 1:
            return self.coll_self(self, m_rect)
        else:
            return False






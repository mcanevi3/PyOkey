import pygame
import pygame.font

class Panel:
    __rect:pygame.Rect
    __surface:pygame.Surface
    __bg=(180,180,180)
    width=320
    height=300
    pos=(0,0)

    def __init__(self):
        width, height = pygame.display.get_window_size()
        self.pos=((width-self.width)//2,(height-self.height)//2)
        self.__rect=pygame.Rect((self.pos[0],self.pos[1],self.width,self.height))
        self.__surface=pygame.Surface((self.width,self.height))
        self.__surface.fill(self.__bg)
    
    def render(self,screen:pygame.Surface):
        self.__surface.fill(self.__bg)
        screen.blit(self.__surface,self.__rect)
        return self


class Button:
    _rect:pygame.Rect
    _surface:pygame.Surface
    text=""
    width=300
    height=80
    pos=(0,0)
    bg=(180,180,180)

    def __init__(self,text="Button",pos=(0,0)):
        self.pos=pos
        self._rect=pygame.Rect((self.pos[0],self.pos[1],self.width,self.height))
        self._surface=pygame.Surface((self.width,self.height))
        self._surface.fill(self.bg)
        self.text=text

    def render(self,screen:pygame.Surface):
        font_size=32
        self._surface.fill(self.bg)
        font=pygame.font.SysFont('Arial', font_size, bold=False)
        text_surface = font.render(self.text, True, (0, 0, 0))
        
        self._surface.blit(text_surface,(10,font_size//2))
        self._rect=pygame.Rect((self.pos[0],self.pos[1],self.width,self.height))
        screen.blit(self._surface,self._rect)

        return self

    def event_handler(self,event,callback):
        (x, y)=pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._rect.collidepoint(x, y):
                callback(self,event)
            
        if event.type == pygame.MOUSEMOTION:
            if self._rect.collidepoint(x, y):
                self.bg=(130,130,180)
            else:
                self.bg=(180,180,180)
                
        return self
    


class Label:
    _rect:pygame.Rect
    _surface:pygame.Surface
    text=""
    width=300
    height=80
    pos=(0,0)

    def __init__(self,text="Label",pos=(0,0)):
        self.pos=pos
        self._rect=pygame.Rect((self.pos[0],self.pos[1],self.width,self.height))
        self._surface=pygame.Surface((self.width,self.height)).convert_alpha()
        self._surface.fill((0,0,0,0))
        self.text=text

    def render(self,screen:pygame.Surface):
        font_size=32
        self._surface.fill((0,0,0,0))
        font=pygame.font.SysFont('Arial', font_size, bold=False)
        text_surface = font.render(self.text, True, (0, 0, 0,255))
        
        self._surface.blit(text_surface,(10,font_size//2))
        self._rect=pygame.Rect((self.pos[0],self.pos[1],self.width,self.height))
        screen.blit(self._surface,self._rect)

        return self
    
    def event_handler(self,event,callback):
        pass


class Progressbar:
    _rect:pygame.Rect
    _surface:pygame.Surface
    bg=(50,170,50)
    __percent=50
    width=300
    height=30
    pos=(0,0)

    def __init__(self,pos=(0,0)):
        self.pos=pos

    def render(self,screen:pygame.Surface):
        self._rect=pygame.Rect((self.pos[0],self.pos[1],self.width*self.__percent/100,self.height))
        self._surface=pygame.Surface((self.width*self.__percent/100,self.height))
        self._surface.fill(self.bg)
        screen.blit(self._surface,self._rect)

        rect=pygame.Rect((self.pos[0],self.pos[1],self.width*self.__percent/100,self.height//2))
        surface=pygame.Surface((self.width*self.__percent/100,self.height//2), pygame.SRCALPHA)
        surface.fill((255,255,255,100))
        screen.blit(surface,rect)

        return self

    def set_percent(self,percent):
        self.__percent=percent
        if self.__percent>100:
            self.__percent=100
        elif self.__percent<0:
            self.__percent=0
        return self
    
    def get_percent(self):
        return self.__percent
    
    def increment(self,val=1):
        self.__percent+=val
        if self.__percent>100:
            self.__percent=100
        elif self.__percent<0:
            self.__percent=0
        return self
    
    def decrement(self,val=1):
        self.increment(-val)
        return self
    
    def event_handler(self,event,callback):
        pass

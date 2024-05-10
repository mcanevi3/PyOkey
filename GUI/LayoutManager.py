import pygame
import pygame.font

class VStack:
    __parent=None
    children=[]
    padd_x=20
    padd_y=20
    h=0
    def __init__(self,parent):
        self.__parent=parent
        self.h=0

    def add(self,obj):
        obj.pos=(self.__parent.pos[0]+self.padd_x,self.__parent.pos[1]+self.padd_y+self.h)
        self.children.append(obj)
        self.h+=obj.height
        return self
    
    def render(self,screen:pygame.Surface):
        for child in self.children:
            child.render(screen)
        return self
    
    def event_handler(self,event,callback):
        for child in self.children:
            child.event_handler(event,callback)
        return self


class HStack:
    __parent=None
    children=[]
    padd_x=20
    padd_y=20
    w=0
    def __init__(self,parent):
        self.__parent=parent

    def add(self,obj):
        obj.pos=(self.__parent.pos[0]+self.padd_x+self.w,self.__parent.pos[1]+self.padd_y)
        self.children.append(obj)
        self.w+=obj.width+self.padd_x
        return self
    
    def render(self,screen:pygame.Surface):
        for child in self.children:
            child.render(screen)
        return self
    
    def event_handler(self,event,callback):
        for child in self.children:
            child.event_handler(event,callback)
        return self

class Grid:
    __parent=None
    children=[]
    padd_x=20
    padd_y=20
    w=0
    h=0
    def __init__(self,parent,crow:int,ccol:int):
        self.__parent=parent
        self.w=self.__parent.width//(ccol+1)
        self.h=self.__parent.height//(crow+1)

    def add(self,row,col,obj):
        obj.pos=(self.__parent.pos[0]+self.padd_x+self.w*col,self.__parent.pos[1]+self.padd_y+self.h*row)
        self.children.append(obj)
        return self
    
    def render(self,screen:pygame.Surface):
        for child in self.children:
            child.render(screen)
        return self
    
    def event_handler(self,event,callback):
        for child in self.children:
            child.event_handler(event,callback)
        return self
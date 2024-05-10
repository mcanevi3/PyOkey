import pygame
import time
from pygame.locals import *

from GUI import Component
from GUI import LayoutManager

class App:
    FPS=60
    prev_time=time.time()
    TARGET_FPS=60
    dt=0

    def __init__(self):
        self.running = True
        self.screen = None
        
        self.clock=pygame.time.Clock()

    def on_init(self):
        self.running = True
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.size = self.width, self.height = pygame.display.get_window_size()
        print(f"Screen size is {self.width}x{self.height}")

        self.panel1=Component.Panel()
        self.layout=LayoutManager.VStack(self.panel1)
        self.layout.add(Component.Button(text="Play"))
        self.layout.add(Component.Button(text="Settings"))
        self.layout.add(Component.Button(text="Quit"))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running=False
                pass
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            else:
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        
        self.layout.event_handler(event=event,callback=self.handle_menu)
                    
    def handle_menu(self,obj,e):
        if type(obj)==Component.Button:
            if obj.text=="Play":
                print("Play game.")
            elif obj.text=="Settings":
                print("Settings...")
            elif obj.text=="Quit":
                print("Quit...")
                self.running=False

        return self
    
    def on_loop(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now
        #self.clock.tick(self.FPS)

    def on_render(self):
        deltaTime = self.dt * self.TARGET_FPS

        self.panel1.render(self.screen)
        self.layout.render(self.screen)

        pygame.display.flip()
                                       
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while( self.running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
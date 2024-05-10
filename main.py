import pygame
import time

class App:
    FPS=60
    prev_time=time.time()
    TARGET_FPS=60
    dt=0

    def __init__(self):
        self.running = True
        self.screen = None
        self.size = self.width, self.height = 1368, 768
        
        self.clock=pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
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
        
                    
    def on_loop(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now
        #self.clock.tick(self.FPS)

    def on_render(self):
        deltaTime = self.dt * self.TARGET_FPS

       
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
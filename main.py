import pygame
import time

pygame.init()

def main():
    GRAVITY = 5
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    
    #player sprite
   
    
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Grooble")
    
    clock = pygame.time.Clock()
    running = True
    player = Groob()

    while running:
        window.fill('white')
        keys = pygame.key.get_pressed()
        player.update(keys, GRAVITY, WINDOW_WIDTH, WINDOW_HEIGHT)
        window.blit(player.img, player.rect)  
        
         
        
       
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            
            
        pygame.display.update()
        clock.tick(60)  


class Groob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load("C:\\Users\\alexc\\Downloads\\Groob_img\\Untitled_Artwork 1.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (25, 25))
        self.rect = self.img.get_frect()
        self.x_velo = 0
        self.y_velo = 0
        self.onGround = False
        

    def update(self, keys, gravity, window_width, window_height):
        
        self.y_velo = gravity


        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        
        #jump
        if keys[pygame.K_SPACE] and self.onGround == True:
            
                
            self.onGround = False
           
        self.rect.y += self.y_velo

        #collisions
        if self.rect.bottom >= window_height:
            self.rect.bottom = window_height
            self.onGround = True
        
        if self.rect.right >= window_width:
            self.rect.right = window_width
        
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

            
        
          


if __name__ == "__main__":
    main()

import pygame

pygame.init()

def main():
    GRAVITY = 9.8
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    Groob_img = pygame.image.load("C:\\Users\\alexc\\Downloads\\Groob_img\\Untitled_Artwork 1.png")
    Groob_img = pygame.transform.scale(Groob_img, (25,25))
    Groob = Groob_img.get_frect()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Grooble")
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        window.fill('white')
        window.blit(Groob_img, (Groob.x,Groob.y))  
        
        keys = pygame.key.get_pressed() 
        
        if keys[pygame.K_d]:
            Groob.x += 10
        if keys[pygame.K_a]:
            Groob.x -= 10
        if keys[pygame.K_SPACE]:
            Groob.y -= 50

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            
        
        Groob.y += GRAVITY

        if(Groob.bottom >= WINDOW_HEIGHT):
            Groob.y = WINDOW_HEIGHT - Groob.height
        if(Groob.left <= 0):
            Groob.x = 0
        if(Groob.right >= WINDOW_WIDTH):
            Groob.x = WINDOW_WIDTH - Groob.width
        
        pygame.display.update()
        clock.tick(60)  



if __name__ == "__main__":
    main()

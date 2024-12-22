import pygame
import os

pygame.init()

def main():
    GRAVITY = 2.5
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    BACKGROUND_IMG = pygame.image.load('C:\\Users\\alexc\\Downloads\\Grooble\\assets\\skyandgrass.png')
    #player sprite
   
    
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Grooble")
    
    clock = pygame.time.Clock()
    running = True
    player = Groob()

    while running:
        window.fill('white')
        window.blit(BACKGROUND_IMG)
        keys = pygame.key.get_pressed()
        player.update(keys, GRAVITY, WINDOW_WIDTH, WINDOW_HEIGHT)
        window.blit(player.img, player.rect)  
        player.draw_debug_bounds(window)
        
         
        
       
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            
            
        pygame.display.update()
        clock.tick(60)  


class Groob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.state = 'idle'
        #not finsihed
        self.animations = {
            "idle": self.load_animation_frames("groob art/idle ani_cropped"),
            "walking": self.load_animation_frames("groob art/walking ani_cropped"),
            
        }
        self.frame_index = 0
        self.img = self.animations[self.state][self.frame_index]
        self.rect = self.img.get_frect()
        self.x_velo = 0
        self.y_velo = 0
        self.onGround = False
        self.animation_timer = 0
        
    
    
    
        
    def load_animation_frames(self, folder_path):
        frames = []
        for file_name in sorted(os.listdir(folder_path)):
            if file_name.endswith(".png"):  # Adjust for your file extension
                frame = pygame.image.load(os.path.join(folder_path, file_name)).convert_alpha()
                original_size = frame.get_size()
                scale_factor = 100 / original_size[1]  # Scale based on height while maintaining aspect ratio
                new_width = int(original_size[0] * scale_factor)
                frame = pygame.transform.scale(frame, (new_width, 100))
                frames.append(frame)
        return frames
    
    def update_animation(self):
        current_frames = self.animations[self.state]
        self.animation_timer += 1
        if self.animation_timer >= 10:  
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(current_frames)
            self.img = current_frames[self.frame_index]

    def update_state(self,keys):
        if keys[pygame.K_a] or keys[pygame.K_d]:
            self.state = 'walking'
        else:
            self.state = 'idle'
            
            
    def update(self, keys, gravity, window_width, window_height):
        self.update_state(keys)
        self.update_animation()
        
        # gravity
        self.rect.y += self.y_velo
        
        
        #correcting the hitbox
        self.rect.right - 100
        self.rect.left + 100
        
        
        if not self.onGround:
            self.y_velo += gravity
        #move l/r
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
            
        
        #jump
        if keys[pygame.K_SPACE] and self.onGround:
            
            self.y_velo -= 25
            self.onGround = False
           
        

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

            
        
          

    def draw_debug_bounds(self, surface):
        # Draw the collision rect in red
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)
        
        # Draw the full image bounds in blue
        image_rect = self.img.get_rect(topleft=self.rect.topleft)
        pygame.draw.rect(surface, (0, 0, 255), image_rect, 1)
        
        # Draw center point
        center_x = self.rect.centerx
        center_y = self.rect.centery
        pygame.draw.circle(surface, (0, 255, 0), (center_x, center_y), 2)


if __name__ == "__main__":
    main()

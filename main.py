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
    proj = egg()
    while running:
        window.blit(BACKGROUND_IMG, (0, 0))
        keys = pygame.key.get_pressed()
        player.update(keys, GRAVITY, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        proj.update(GRAVITY, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        if proj.rect.colliderect(player.rect):
            proj.hit = True
            
        if not proj.hit or (proj.hit and not proj.animation_complete):
            window.blit(proj.img, proj.rect)
            
        window.blit(player.img, player.rect)
        
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

            
        
            '''

    def draw_debug_bounds(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)
        
        image_rect = self.img.get_rect(topleft=self.rect.topleft)
        pygame.draw.rect(surface, (0, 0, 255), image_rect, 1)
        
        center_x = self.rect.centerx
        center_y = self.rect.centery
        pygame.draw.circle(surface, (0, 255, 0), (center_x, center_y), 2)
            '''
class egg(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.frame_index = 0
        self.frames = self.load_animation_frames("egg")
        self.img = self.frames[self.frame_index]
        self.rect = self.img.get_frect()
        self.rect.x = 100
        self.rect.y = 0
        self.animation_timer = 0
        self.hit = False
        self.y_velo = 5
        self.animation_complete = False
        
    def load_animation_frames(self, folder_path):
        frames = []
        for file_name in sorted(os.listdir(folder_path)):
            if file_name.endswith(".png"):
                frame = pygame.image.load(os.path.join(folder_path, file_name)).convert_alpha()
                original_size = frame.get_size()
                scale_factor = 50 / original_size[1]  # Changed from 100 to 50 for half the size
                new_width = int(original_size[0] * scale_factor)
                frame = pygame.transform.scale(frame, (new_width, 50))  # Changed height to 50
                frames.append(frame)
        return frames
    
    def update_animation(self):
        self.animation_timer += 1
        if self.animation_timer >= 10:  
            self.animation_timer = 0
            if self.frame_index < len(self.frames) - 1:
                self.frame_index += 1
                self.img = self.frames[self.frame_index]
                if self.frame_index == len(self.frames) - 1:
                    self.animation_complete = True

    
            
    def update(self, gravity, window_width, window_height):
        if self.hit:
            self.update_animation()
        
        if not self.hit:
            self.rect.y += 5
        
        #collisions
        if self.rect.bottom >= window_height:
            self.rect.bottom = window_height
            self.hit = True
        
        if self.rect.right >= window_width:
            self.rect.right = window_width
        
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

if __name__ == "__main__":
    main()
    
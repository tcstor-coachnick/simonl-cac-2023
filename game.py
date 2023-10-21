import pygame
from cannon import Cannon
from bullet import Bullet
from enemy import Enemy 
#importing from the other files ( other pys)
class Game:
    def __init__(self):
        pygame.init()
        self.window_w = 1080
        self.window_h = 1000
        self.window = pygame.display.set_mode((self.window_w, self.window_h))
        #game window for displaying
        self.cannon = Cannon()


        self.bullets = []
        
        self.shoot_event = pygame.event.custom_type()
        pygame.time.set_timer(self.shoot_event, self.cannon.atk_spd)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.enemy = Enemy(50, 50, self.window_h, self.window_w, "", 3, self.cannon.x, self.cannon.y, self.cannon.width, self.cannon.height)

        #fps & how many bullets we can shoot ( also made a timer for it)



    def main_game_loop(self):
        while True:
            self.clock.tick(self.fps)
            self.event_handler()
            self.window.fill((0,0,0))
            self.draw_cannon()
            for bullet in self.bullets : 
                bullet.move()
            self.enemy.move()
            self.draw_bullet()
            self.draw_enemy()
            pygame.display.update()

    def event_handler(self):
        #grabs a list of all events
        event_list = pygame.event.get()
        #loop through every event that has
        #happened and handle

        self.cannon.calculate_direction()

        for event in event_list:
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
            
                quit()
                #whenever you exit it closes instantly
    
            if event.type == self.shoot_event:
                new_bullet = Bullet(self.cannon.x, self.cannon.y, self.cannon.width, self.cannon.height, 5, 10, "", 10, 10, self.cannon.direction)
                self.bullets.append(new_bullet)
                #bulletS so you could have multiple bullets on your game screen
            
        
    def draw_cannon(self):
        #step 1: Construct a square
        square = pygame.Rect(self.cannon.x, self.cannon.y, self.cannon.width, self.cannon.height)
        #step 2 : draw the square on the window
        pygame.draw.rect(self.window, (0, 255, 0), square)

        #step 3: Tell the window to update
        

    def draw_bullet(self):
        for bullet in self.bullets:

            square = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)

            pygame.draw.rect(self.window, (255, 0, 0), square)
            #bullet drawing

    def draw_enemy(self):
        #step 1: Construct a square
        square = pygame.Rect(self.enemy.x, self.enemy.y, self.enemy.width, self.enemy.height)
        #step 2 : draw the square on the window
        pygame.draw.rect(self.window, (0, 255, 0), square)

        #step 3: Tell the window to update
    

       
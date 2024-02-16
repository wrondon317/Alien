import sys
import pygame
from setting import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game,and create game resouces"""
        pygame.init()
        self.setting = Settings()
        
        self.screen = pygame.display.set_mode((self.setting.screen_width,
                                              self.setting.screen_height))
        # Full screen mode 
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().heigh
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # # Set the background color
        # self.bg_color = (128,128,128)
        
    def run_game(self):
        """Start the main lopp for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
            
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self,event):
        if event.key== pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key== pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key== pygame.K_UP:
            self.ship.moving_up = True
        elif event.key== pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self,event):        
        if event.key== pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key== pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key== pygame.K_UP:
            self.ship.moving_up = False
        elif event.key== pygame.K_DOWN:
            self.ship.moving_down = False
            # watch for keyboard and mouse events

    def _update_screen(self):        
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()            
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
            
        
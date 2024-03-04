class Settings:
    '''A class to store all setting for Alien Invasion'''
    
    def __init__(self):
        '''Initialize the game's settings'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (4, 37, 75)
        
        # Ship settings
        self.ship_limit = 3
        
        # bullets settings
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (255, 204, 0)
        self.bullets_allowed = 3
        
        #Alien Settings
        self.fleet_drop_speed = 10
  
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        # How quickly the alien point values increase
        self.score_scale = 1.1
        
        self.initialize_dynamic_settings()
    
    def increase_speed(self):
        '''Increase speed settings and alien point values'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1 
        self.alien_points = 50   
        
        
        
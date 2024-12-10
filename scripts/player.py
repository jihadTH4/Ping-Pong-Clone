import pygame
from pygame.locals import *
from pygame.sprite import Sprite


class Player(Sprite):
    """Base Player class"""

    def __init__(self, ai_settings, screen, color, position, key_up, key_down):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Player rect and initial position
        self.rect = pygame.Rect(
            0, 0, ai_settings.player_width, ai_settings.player_height)
        self.color = color
        self.set_position(position)

        # Movement keys
        self.key_up = key_up
        self.key_down = key_down

        # Goal flag
        self.goal = False

    def set_position(self, position):
        """Set player position based on side ('left' or 'right')"""
        if position == 'left':
            self.rect.left = self.screen_rect.left + self.ai_settings.player_margin
        elif position == 'right':
            self.rect.right = self.screen_rect.right - self.ai_settings.player_margin

        self.rect.centery = self.screen_rect.centery

    def update(self):
        """Update player position based on key presses"""
        keys = pygame.key.get_pressed()

        if keys[self.key_up]:
            self.rect.centery -= self.ai_settings.player_speed_factor
        if keys[self.key_down]:
            self.rect.centery += self.ai_settings.player_speed_factor

        # Keep player within screen bounds
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(self.screen_rect.bottom, self.rect.bottom)

    def draw(self):
        """Draw the player on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


# Example of how to instantiate the players
class Player1(Player):
    def __init__(self, ai_settings, screen, color):
        super().__init__(ai_settings, screen, color,
                         position='right', key_up=K_UP, key_down=K_DOWN)


class Player2(Player):
    def __init__(self, ai_settings, screen, color):
        super().__init__(ai_settings, screen, color,
                         position='left', key_up=K_w, key_down=K_s)

"""button is module for making buttons for
 pygame's games using pygame.font"""
import pygame.font


class Button():
    def __init__(self, screen, msg: str, button_color: tuple, posx=0, posy=0, text_color=(255, 255, 255), font_size=48):
        """Initialize button attributes."""
        self.screen = screen
        self.posx = posx
        self.posy = posy
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont("consolas", font_size)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        if self.posx == 0 and self.posy == 0:
            self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn ``msg`` into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, False, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

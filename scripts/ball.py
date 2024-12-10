import pygame


class Ball:
    """Initialize Ball attributes"""

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # ball settings
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.height = ai_settings.ball_height
        self.color = ai_settings.ball_color
        self.rect.center = self.screen_rect.center
        self.speed = ai_settings.ball_speed_factor

    def update(self):
        """Update the ball pos on the screen"""
        self.rect.move_ip(self.speed)

    def check_top_bottom_edges(self):
        """Check if the ball hit the edges"""
        return (self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.height)

    def draw(self):
        """Draw the ball to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect, 50, 50)

    def center_ball(self):
        """Center the ball on the screen."""
        self.rect.center = self.screen_rect.center

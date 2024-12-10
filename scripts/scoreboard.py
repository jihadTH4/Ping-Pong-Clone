import pygame.font


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (225, 255, 225)
        self.font = pygame.font.SysFont(None, 55)

        self.prep_p1_score()
        self.prep_p2_score()

    def prep_p1_score(self):
        """Turn the score into a rendered image."""
        self.score_str = str(self.stats.player1_score)

        self.score_p1_image = self.font.render(self.score_str, True, self.text_color,
                                               self.ai_settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_p1_rect = self.score_p1_image.get_rect()
        self.score_p1_rect.centerx = self.screen_rect.centerx + 50
        self.score_p1_rect.centery = self.screen_rect.centery

    def prep_p2_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.player2_score)

        self.score_p2_image = self.font.render(score_str, True, self.text_color,
                                               self.ai_settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_p2_rect = self.score_p2_image.get_rect()
        self.score_p2_rect.centerx = self.screen_rect.centerx - 50
        self.score_p2_rect.centery = self.screen_rect.centery
        
    def show_score(self):
        self.screen.blit(self.score_p1_image, self.score_p1_rect)
        self.screen.blit(self.score_p2_image, self.score_p2_rect)

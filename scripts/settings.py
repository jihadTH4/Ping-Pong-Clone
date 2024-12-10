
class Settings:
    """A class to store all settings for Ping Pong."""

    def __init__(self):
        """Initialize the game's static settings."""

        # screen settings
        self.screen_width = 920
        self.screen_height = 550
        self.bg_color = (0, 0, 0)
        self.frames = 60

        # players setting
        self.player_width = 15
        self.player_height = 75
        self.player_color = (225, 225, 225)
        self.player_speed_factor = 7
        self.player_margin = 20  # Distance from screen edge

        # ball settings
        self.ball_width = 10
        self.ball_height = 10
        self.ball_radius = 10.0
        self.ball_color = (225, 225, 225)  # White
        self.ball_speed_factor = [7, 7]

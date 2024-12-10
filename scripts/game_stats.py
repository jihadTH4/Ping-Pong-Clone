
class GameStats:
    """Track statistics for Ping Pong."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings

        # Start Ping Pong in an inactive state.
        self.game_active = False
        self.player1_score = 0
        self.player2_score = 0

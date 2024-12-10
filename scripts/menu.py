from scripts.button import Button


class Menu:

    def __init__(self, screen) -> None:
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.Ping_Pong_label = Button(self.screen, "Ping Pong", (0, 0, 0),
                                      self.screen_rect.centerx-100, self.screen_rect.centery -
                                      150, (255, 255, 255), 64
                                      )
        self.playe_button = Button(self.screen, "Play", (0, 225, 0))
        self.exit_button = Button(self.screen, "Exit", (225, 0, 0),
                                  self.screen_rect.centerx-100, self.screen_rect.centery+40)

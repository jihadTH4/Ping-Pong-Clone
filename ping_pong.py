""" Ping Pong game made by @``Jihad Thabit`` A.K.A @``B7locy`` """
import pygame
from pygame.sprite import Group
from scripts.settings import Settings
import scripts.game_functions as gf
from scripts.game_stats import GameStats
from scripts.scoreboard import Scoreboard
from scripts.player import *
from scripts.ball import Ball
from scripts.menu import Menu


def run_game():
    """Run the main loop of the game"""
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen_rect = screen.get_rect()

    pygame.display.set_caption("Ping Pong")

    # Setting the game icon
    icon = pygame.image.load('ball_icon.icon')
    icon.set_colorkey((0, 0, 0))
    pygame.display.set_icon(icon)

    # statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # game objects
    menu = Menu(screen)
    player1 = Player1(ai_settings, screen, (225, 0, 0))
    player2 = Player2(ai_settings, screen, (0, 0, 255))
    players = Group(player1, player2)
    ball = Ball(ai_settings, screen)
    clock = pygame.time.Clock()

    # main loop
    while True:
        gf.check_events(menu.playe_button, menu.exit_button,
                        stats)
        if stats.game_active:
            players.update()
            gf.update_ball(ball, player1, player2)

        gf.update_screen(ai_settings, screen, stats, menu.playe_button,
                         menu.exit_button,
                         menu.Ping_Pong_label, player1, player2, players,
                         ball, sb, screen_rect)
        clock.tick(ai_settings.frames)


if __name__ == "__main__":
    run_game()

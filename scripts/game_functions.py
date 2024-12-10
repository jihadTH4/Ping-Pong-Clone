import sys
import pygame
import time
from pygame.locals import *
from pygame.time import Clock


def check_events(play_button, exit_button, stats):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        elif (event.type == KEYDOWN and event.key == K_ESCAPE) and stats.game_active:
            stats.game_active = False
            pygame.mouse.set_visible(True)

        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_buttons(play_button, exit_button, stats, mouse_x, mouse_y)

        elif (event.type == KEYDOWN and event.key == K_ESCAPE) and not stats.game_active:
            stats.game_active = True
            pygame.mouse.set_visible(False)


def check_buttons(play_button, exit_button, stats, mouse_x, mouse_y):
    """Check the button on the main menu if it gets clicked."""
    buttons_clicked = {
        "Play": play_button.rect.collidepoint(mouse_x, mouse_y),
        "Exit": exit_button.rect.collidepoint(mouse_x, mouse_y),
    }

    if buttons_clicked["Play"] and not stats.game_active:
        start_game(stats)

    elif buttons_clicked["Exit"] and not stats.game_active:
        sys.exit()


def update_screen(ai_settings, screen, stats,
                  play_button, exit_button,
                  Ping_Pong, player1, player2,
                  players, ball, sb, screen_rect):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        Ping_Pong.draw()
        play_button.draw()
        exit_button.draw()
    elif stats.game_active:
        pygame.draw.line(screen, (255, 255, 255), (screen_rect.centerx,
                         0), (screen_rect.centerx, screen_rect.bottom))
        sb.show_score()
        ball.draw()
        for player in players:
            player.draw()
        scoring(stats, sb, ball, player1, player2)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

    # Set the frames of the game to 60
    clock = Clock()
    clock.tick(60)


def update_ball(ball, player1, player2):
    """Update the ball movements on the screen."""
    ball.update()

    if ball.check_top_bottom_edges():
        ball.speed[1] = -ball.speed[1]
    if check_player_ball_collision(player1, player2, ball):
        ball.speed[0] = -ball.speed[0]


def start_game(stats):
    """Make the game active `True`."""
    # Hide the mouse cursor.
    pygame.mouse.set_visible(False)
    stats.game_active = True


def check_player_ball_collision(player1, player2, ball):
    """Check if the player hit the ball."""
    # We check ball speed to avoid the bug that makes the ball stick with the player.
    return ball.rect.colliderect(player1.rect) and ball.speed[0] > 0 \
        or ball.rect.colliderect(player2.rect) and ball.speed[0] < 0


def scoring(stats, sb, ball, player1, player2):
    """Check the players' goals and do scoring system."""
    check_players_goal(ball, player1, player2)
    if player1.goal:
        time.sleep(0.3)
        stats.player1_score += 1
        sb.prep_p1_score()
        center_objects(ball, player1, player2)
        player1.goal = False

    elif player2.goal:
        time.sleep(0.3)
        stats.player2_score += 1
        sb.prep_p2_score()
        center_objects(ball, player1, player2)
        player2.goal = False


def check_players_goal(ball, player1, player2):
    """Check if the ball hit the left or right edge of the screen."""
    if ball.rect.left < 0:
        player1.goal = True

    elif ball.rect.right > ball.screen_rect.right:
        player2.goal = True


def center_objects(ball, player1, player2):
    """Center the ball, player1, and player2."""
    ball.center_ball()
    player1.set_position("right")
    player2.set_position("left")

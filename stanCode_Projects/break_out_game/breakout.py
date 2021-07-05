"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    lives = NUM_LIVES
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    while True:
        pause(FRAME_RATE)
        if lives == 0:
            break
        if graphics.game_start:
            graphics.ball.move(dx, dy)
            if graphics.ball.y >= graphics.window.height:
                lives -= 1
                graphics.ball.x = (graphics.window_width - graphics.ball_radius * 2) // 2
                graphics.ball.y = (graphics.window_height - graphics.ball_radius * 2) // 2
                graphics.game_start = False
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                dx = -dx
            if graphics.get_paddle_at():
                dy = -dy
            if graphics.get_brick_at():
                graphics.window.remove(graphics.brick)
                dy = -dy


if __name__ == '__main__':
    main()
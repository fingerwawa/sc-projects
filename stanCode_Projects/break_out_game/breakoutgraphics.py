"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Width of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(self.window_width-paddle_width)//2, y=(self.window_height-paddle_offset))
        self.paddle.color = "black"
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2,
                          x=(self.window_width-ball_radius*2)//2, y=(self.window_height-ball_radius*2)//2)
        self.ball_radius = BALL_RADIUS
        self.ball.color = "black"
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball)
        self._dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self._dx = -self._dx
        self._dy = INITIAL_Y_SPEED
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmousemoved(self.mouse_tracker)
        self.game_start = False
        onmouseclicked(self.move_the_ball)
        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                if j == 0 or j == 1:
                    self.brick.color = "red"
                    self.brick.filled = True
                    self.brick.fill_color = "red"
                elif j == 2 or j == 3:
                    self.brick.color = "orange"
                    self.brick.filled = True
                    self.brick.fill_color = "orange"
                elif j == 4 or j == 5:
                    self.brick.color = "yellow"
                    self.brick.filled = True
                    self.brick.fill_color = "yellow"
                elif j == 6 or j == 7:
                    self.brick.color = "green"
                    self.brick.filled = True
                    self.brick.fill_color = "green"
                else:
                    self.brick.color = "blue"
                    self.brick.filled = True
                    self.brick.fill_color = "blue"
                self.window.add(self.brick, x=i*(brick_width+brick_spacing),
                                y=brick_offset+(j*(brick_height+brick_spacing)))

    def mouse_tracker(self, m):
        if m.x+self.paddle.width <= self.window.width:
            self.paddle.x = m.x
        else:
            self.paddle.x = m.x-self.paddle.width

    def move_the_ball(self, m2):
        if not self.game_start:
            self.game_start = True

    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    def get_paddle_at(self):
        if self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius) \
                or self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y + 2 * self.ball_radius) \
                is self.paddle:
            return True

    def get_brick_at(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None \
                and self.window.get_object_at(self.ball.x, self.ball.y) is not self.paddle:
            self.brick = self.window.get_object_at(self.ball.x, self.ball.y)
            return True
        elif self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y) is not None \
                and self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y) is not self.paddle:
            self.brick = self.window.get_object_at(self.ball.x, self.ball.y)
            return True


if __name__ == '__main__':
    main()
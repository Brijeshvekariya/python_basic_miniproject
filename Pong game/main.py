from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Rectangle, Ellipse
from kivy.clock import Clock
from kivy.core.window import Window
import random

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 3
PADDLE_SPEED = 80

# Create the game window
Window.size = (WIDTH, HEIGHT)
Window.title = "Pong Game"

class PongGame(Widget):
    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self.score = 0
        self.highscore = 0
        self.reset_button = Button(text="Reset", pos=(350, 394), size=(100, 40))
        self.reset_button.bind(on_press=self.reset_game)
        self.reset_button.opacity = 0
        self.game_over_label = Label(text="GAME-OVER", pos=(340, 310), color=(1, 1, 1, 1))
        self.game_over_label.font_size = 36  # Set the font size to 36
        self.game_over_label.bold = True # set game-over text to bold
        self.game_over_label.opacity = 0
        self.game_over = False

        self.background_image = Image(source="assets/BG.png", size=(WIDTH, HEIGHT))
        self.add_widget(self.background_image)

        # Create separate rectangles for the left and right paddles
        self.left_paddle = Rectangle(pos=(50, HEIGHT // 2 - PADDLE_SPEED // 2), size=(10, 100))
        self.right_paddle = Rectangle(pos=(WIDTH - 50 - 10, HEIGHT // 2 - PADDLE_SPEED // 2), size=(10, 100))
        self.ball = Ellipse(pos=(WIDTH // 2 - 15, HEIGHT // 2 - 15), size=(30, 30))

        self.canvas.add(self.left_paddle)
        self.canvas.add(self.right_paddle)
        self.canvas.add(self.ball)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        self.add_widget(self.reset_button)
        self.add_widget(self.game_over_label)

        self.ball_dx = BALL_SPEED * random.choice((1, -1))
        self.ball_dy = BALL_SPEED * random.choice((1, -1))

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            self.move_left_paddle_up()
        elif keycode[1] == 's':
            self.move_left_paddle_down()
        elif keycode[1] == 'up':
            self.move_right_paddle_up()
        elif keycode[1] == 'down':
            self.move_right_paddle_down()

    def _on_keyboard_up(self, keyboard, keycode):
        # Stop the paddles from moving when keys are released
        if keycode[1] in ('w', 's'):
            self.left_paddle_speed = 0
        elif keycode[1] in ('up', 'down'):
            self.right_paddle_speed = 0

    def move_left_paddle_up(self):
        # Move the left paddle up
        x, y = self.left_paddle.pos
        new_y = y + PADDLE_SPEED
        if new_y >= 0:
            self.left_paddle.pos = (x, new_y)

    def move_left_paddle_down(self):
    # Move the left paddle down
        x, y = self.left_paddle.pos
        new_y = y - PADDLE_SPEED
        if new_y >= 0:
            self.left_paddle.pos = (x, new_y)


    def move_right_paddle_up(self):
        # Move the right paddle up
        x, y = self.right_paddle.pos
        new_y = y + PADDLE_SPEED
        if new_y >= 0:
            self.right_paddle.pos = (x, new_y)

    def move_right_paddle_down(self):
        # Move the right paddle down
        x, y = self.right_paddle.pos
        new_y = y - PADDLE_SPEED
        if new_y >= 0:
            self.right_paddle.pos = (x, new_y)

    def reset_game(self, instance):
        if self.game_over:
            self.score = 0
            self.ball.pos = (WIDTH // 2 - 15, HEIGHT // 2 - 15)
            self.reset_button.opacity = 0
            self.game_over_label.opacity = 0
            self.game_over = False

    def update(self, dt):
        if not self.game_over:
            ball_x, ball_y = self.ball.pos
            ball_x += self.ball_dx
            ball_y += self.ball_dy
            self.ball.pos = (ball_x, ball_y)

            if ball_y <= 0 or ball_y >= HEIGHT - 30:
                self.ball_dy *= -1

            ball_center_x, ball_center_y = (ball_x + 15, ball_y + 15)

            # Check collision for left paddle
            if (
                ball_center_x <= self.left_paddle.pos[0] + 10
                and ball_center_y >= self.left_paddle.pos[1]
                and ball_center_y <= self.left_paddle.pos[1] + 100
            ):
                self.ball_dx *= -1
                self.score += 1
                if self.highscore < self.score:
                    self.highscore = self.score

            # Check collision for right paddle
            if (
                ball_center_x >= self.right_paddle.pos[0]
                and ball_center_y >= self.right_paddle.pos[1]
                and ball_center_y <= self.right_paddle.pos[1] + 100
            ):
                self.ball_dx *= -1
                self.score += 1
                if self.highscore < self.score:
                    self.highscore = self.score

            if ball_x <= 0 or ball_x >= WIDTH - 30:
                self.game_over = True
                self.reset_button.opacity = 1
                self.game_over_label.opacity = 1

class PongApp(App):
    def build(self):
        return PongGame()
    
if __name__ == '__main__':
    PongApp().run()

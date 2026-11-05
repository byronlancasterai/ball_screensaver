"""A ball bouncing inside a rectangle. Waiting for the corner."""
import random
import pyglet

WINDOW = 640
BALL_R = 12
BALL_SPEED = 220.0


class Ball:
    def __init__(self, x, y, vx, vy, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx
        elif self.x + self.radius > WINDOW:
            self.x = WINDOW - self.radius
            self.vx = -self.vx

        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.vy
        elif self.y + self.radius > WINDOW:
            self.y = WINDOW - self.radius
            self.vy = -self.vy


def main():
    window = pyglet.window.Window(WINDOW, WINDOW, caption="ball")
    label = pyglet.text.Label(
        "bounce", font_size=14, x=WINDOW - 12, y=WINDOW - 24,
        anchor_x="right", anchor_y="top",
    )
    ball = Ball(WINDOW / 2, WINDOW / 2, BALL_SPEED, BALL_SPEED * 0.7, BALL_R)
    ball_label = pyglet.text.Label(
        "\u25CF", font_size=40, color=(77, 179, 255, 255),
        x=WINDOW / 2, y=WINDOW / 2,
    )

    @window.event
    def on_draw():
        window.clear()
        label.draw()
        ball_label.x = ball.x
        ball_label.y = ball.y
        ball_label.draw()

    def update(dt):
        ball.update(dt)

    pyglet.clock.schedule_interval(update, 1 / 60)
    pyglet.app.run()


if __name__ == "__main__":
    main()

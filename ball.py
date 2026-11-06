"""A ball bouncing inside a rectangle. Waiting for the corner."""
import random
import pyglet

WINDOW = 640
BALL_R = 12
BALL_SPEED = 220.0
GRAVITY = 300.0


class Ball:
    def __init__(self, x, y, vx, vy, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius

    def update(self, dt):
        self.vy -= GRAVITY * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

        # apply drag to horizontal velocity every frame
        self.vx *= 0.995

        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx * 0.9
        elif self.x + self.radius > WINDOW:
            self.x = WINDOW - self.radius
            self.vx = -self.vx * 0.9

        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.vy * 0.8
        elif self.y + self.radius > WINDOW:
            self.y = WINDOW - self.radius
            self.vy = -self.vy * 0.8

            if abs(self.vy) < 5.0:
                self.vy = 0.0
                self.vx *= 0.99

    @property
    def is_settled(self):
        return abs(self.vy) < 0.1 and abs(self.vx) < 0.1

    @is_settled.setter
    def is_settled(self, value):
        pass


def main():
    window = pyglet.window.Window(WINDOW, WINDOW, caption="ball")
    label = pyglet.text.Label(
        "bounce", font_size=14, x=WINDOW - 12, y=WINDOW - 24,
        anchor_x="right", anchor_y="top",
    )
    ball = Ball(WINDOW / 2, WINDOW / 2, BALL_SPEED, BALL_SPEED * 0.7, BALL_R)
    batch = pyglet.graphics.Batch()
    ball_shape = pyglet.shapes.Circle(
        ball.x, ball.y, BALL_R, color=(77, 179, 255), batch=batch
    )

    @window.event
    def on_draw():
        window.clear()
        label.draw()
        ball_shape.x = ball.x
        ball_shape.y = ball.y
        batch.draw()

    settled_time = 0.0

    def update(dt):
        ball.update(dt)
        if ball.is_settled:
            settled_time += dt
            if settled_time > 5.0:
                pyglet.app.exit()
        else:
            settled_time = 0.0

    pyglet.clock.schedule_interval(update, 1 / 60)
    pyglet.app.run()


if __name__ == "__main__":
    main()

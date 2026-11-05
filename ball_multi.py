"""Multiple balls bouncing inside a rectangle. A screensaver."""
import random
import pyglet

WINDOW = 640
BALL_R = 12
BALL_SPEED = 220.0
NUM_BALLS = 8

COLORS = [
    (255, 80, 80, 255),
    (80, 255, 80, 255),
    (80, 80, 255, 255),
    (255, 255, 80, 255),
    (255, 80, 255, 255),
    (80, 255, 255, 255),
    (255, 160, 80, 255),
    (160, 80, 255, 255),
]


class Ball:
    def __init__(self, x, y, vx, vy, radius, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color

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


def random_ball():
    angle = random.uniform(0, 6.283)
    speed = random.uniform(BALL_SPEED * 0.5, BALL_SPEED * 1.5)
    vx = speed * __import__('math').cos(angle)
    vy = speed * __import__('math').sin(angle)
    x = random.uniform(BALL_R, WINDOW - BALL_R)
    y = random.uniform(BALL_R, WINDOW - BALL_R)
    color = random.choice(COLORS)
    return Ball(x, y, vx, vy, BALL_R, color)


import pyglet.shapes

def main():
    window = pyglet.window.Window(WINDOW, WINDOW, caption="balls")
    balls = [random_ball() for _ in range(NUM_BALLS)]
    shapes_list = []
    for ball in balls:
        shape = pyglet.shapes.Circle(
            x=ball.x, y=ball.y,
            radius=ball.radius,
            color=(ball.color[0], ball.color[1], ball.color[2])
        )
        shapes_list.append(shape)

    @window.event
    def on_draw():
        window.clear()
        for i, ball in enumerate(balls):
            shapes_list[i].x = ball.x
            shapes_list[i].y = ball.y
            shapes_list[i].draw()

    def update(dt):
        for ball in balls:
            ball.update(dt)

    pyglet.clock.schedule_interval(update, 1 / 60)
    pyglet.app.run()


if __name__ == "__main__":
    main()

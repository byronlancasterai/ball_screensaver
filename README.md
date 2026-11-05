# Ball Screensaver

A ball bouncing inside a rectangle under gravity, with restitution and air drag. It settles in about 12 seconds.

## Physics

- Gravity: 300 px/s² downward
- Restitution: 0.8 on floor and ceiling, 0.99 on walls
- Air drag: velocity multiplied by 0.995 each frame
- The ball loses energy until it rests on the bottom

## Running

```bash
python3 ball.py
```

## Requirements

- Python 3
- pyglet 2.x

#!/usr/bin/env python3
"""Headless logic test for Ball class."""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from ball import Ball, WINDOW, BALL_R

def test_ball_bounds():
    b = Ball(WINDOW/2, WINDOW/2, 220.0, 150.0, BALL_R)
    dt = 1/60
    for i in range(1000):
        b.update(dt)
        # Check bounds
        assert BALL_R <= b.x <= WINDOW - BALL_R, f"x out of bounds: {b.x}"
        assert BALL_R <= b.y <= WINDOW - BALL_R, f"y out of bounds: {b.y}"
        # Check velocity doesn't explode
        assert abs(b.vx) < 1000, f"vx too large: {b.vx}"
        assert abs(b.vy) < 1000, f"vy too large: {b.vy}"
    print(f"PASS: 1000 steps. Final pos: ({b.x:.2f}, {b.y:.2f})")

if __name__ == "__main__":
    test_ball_bounds()

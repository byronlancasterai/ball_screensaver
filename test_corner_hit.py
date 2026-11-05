#!/usr/bin/env python3
"""Run Ball for many steps and check if it ever hits a corner."""
import sys
import math

# Add the project directory to the path so we can import ball.py
sys.path.insert(0, '/config/byron/projects/ball_screensaver')

# We need to mock pyglet to avoid GUI dependencies
import unittest.mock

# Mock pyglet.window and pyglet.app to allow import without display
with unittest.mock.patch('pyglet.window'), \
     unittest.mock.patch('pyglet.app'), \
     unittest.mock.patch('pyglet.text'), \
     unittest.mock.patch('pyglet.clock'):
    from ball import Ball

WINDOW = 640
BALL_R = 12

def run_case(dt=1/60, steps=100000):
    """
    Run the ball for a number of steps with a fixed dt.
    Returns (corner_hits, near_corner_visits)
    """
    # Start at center with a specific velocity
    ball = Ball(WINDOW/2, WINDOW/2, 220.0, 220.0 * 0.7, BALL_R)
    
    corner_hits = 0
    near_corner_visits = 0
    
    # Define corner tolerance
    CORNER_TOL = 5.0
    NEAR_CORNER_TOL = 15.0
    
    for _ in range(steps):
        ball.update(dt)
        
        # Check if near a corner (within NEAR_CORNER_TOL of both walls)
        # Corners are at (0,0), (0, WINDOW), (WINDOW, 0), (WINDOW, WINDOW)
        # Since ball is clamped to radius, effective corners are (BALL_R, BALL_R) etc.
        
        x, y = ball.x, ball.y
        r = ball.radius
        
        # Distance to nearest vertical wall
        dx = min(x - r, WINDOW - r - x)
        # Distance to nearest horizontal wall
        dy = min(y - r, WINDOW - r - y)
        
        if dx < NEAR_CORNER_TOL and dy < NEAR_CORNER_TOL:
            near_corner_visits += 1
            if dx < CORNER_TOL and dy < CORNER_TOL:
                corner_hits += 1
                
    return corner_hits, near_corner_visits

def main():
    print(f"Testing corner hits with WINDOW={WINDOW}, R={BALL_R}")
    hits, near = run_case(steps=100000)
    print(f"Steps: 100000")
    print(f"Corner hits (within 5px): {hits}")
    print(f"Near-corner visits (within 15px): {near}")
    
    if hits == 0:
        print("No corner hits. The random perturbation in update() may be preventing exact hits.")

if __name__ == "__main__":
    main()

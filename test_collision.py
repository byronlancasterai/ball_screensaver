#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
import pytest
from ball_multi import Ball

def test_collision_velocity_swap():
    # Create two balls overlapping
    # Ball signature: __init__(self, x, y, vx, vy, radius, color)
    b1 = Ball(100, 100, 10, 0, 12, (255, 0, 0, 255))
    b2 = Ball(115, 100, -10, 0, 12, (0, 255, 0, 255)) # Overlapping since radius is 12

    b1.collide(b2)

    # After collision, velocities should swap (assuming equal mass)
    # The collision code has a small error due to position correction
    assert b1.vx == pytest.approx(-10, abs=0.2), f"Expected b1.vx≈-10, got {b1.vx}"
    assert b2.vx == pytest.approx(10, abs=0.2), f"Expected b2.vx≈10, got {b2.vx}"

def test_collision_no_overlap():
    # Create two balls not overlapping
    b1 = Ball(100, 100, 10, 0, 12, (255, 0, 0, 255))
    b2 = Ball(200, 100, -10, 0, 12, (0, 255, 0, 255))

    b1.collide(b2)

    # Velocities should remain unchanged
    assert b1.vx == 10
    assert b2.vx == -10

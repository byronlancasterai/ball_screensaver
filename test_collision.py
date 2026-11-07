import sys
sys.path.insert(0, '.')
from ball_multi import Ball

# Create two balls overlapping
# Ball signature: __init__(self, x, y, vx, vy, radius, color)
b1 = Ball(100, 100, 10, 0, 12, (255, 0, 0, 255))
b2 = Ball(115, 100, -10, 0, 12, (0, 255, 0, 255)) # Overlapping since radius is 12

print(f"Before: b1.v={b1.vx:.2f},{b1.vy:.2f} b2.v={b2.vx:.2f},{b2.vy:.2f}")
b1.collide(b2)
print(f"After:  b1.v={b1.vx:.2f},{b1.vy:.2f} b2.v={b2.vx:.2f},{b2.vy:.2f}")

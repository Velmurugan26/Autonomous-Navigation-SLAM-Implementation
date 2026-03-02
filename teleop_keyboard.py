#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg = """
Keyboard Teleoperation
----------------------
Use WASD keys to move the robot:
    W/S : Move Forward / Backward
    A/D : Turn Left / Right
CTRL+C to quit
"""

moveBindings = {
    'w': (1, 0),
    's': (-1, 0),
    'a': (0, 1),
    'd': (0, -1),
}

def getKey():
    """Read a single keypress from keyboard."""
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

settings = termios.tcgetattr(sys.stdin)

def main():
    rospy.init_node('teleop_keyboard')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    speed = 0.2  # Linear speed
    turn = 0.5   # Angular speed

    try:
        print(msg)
        while True:
            key = getKey()
            twist = Twist()
            if key in moveBindings.keys():
                linear = moveBindings[key][0] * speed
                angular = moveBindings[key][1] * turn
                twist.linear.x = linear
                twist.angular.z = angular
            else:
                twist.linear.x = 0
                twist.angular.z = 0

            pub.publish(twist)

            if key == '\x03':  # CTRL+C
                break
    except Exception as e:
        print(e)
    finally:
        twist = Twist()
        pub.publish(twist)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        print("\nTeleoperation node terminated.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python
#encoding: utf8

import sys, termios, rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

class KeyRun():
    def __init__(self):
        self.cmd_vel = rospy.Publisher('/cmd_vel',Twist,queue_size=1)

    def keyin(self):
        fd = sys.stdin.fileno()

        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)

        new[3] &= ~termios.ICANON
        new[3] &= ~termios.ECHO

        try:
            termios.tcsetattr(fd, termios.TCSANOW, new)
            self.key = sys.stdin.read(1)

        finally:
            termios.tcsetattr(fd, termios.TCSANOW, old)

        return key

    def run(self):
        rate = rospy.Rate(10)
        data = Twist()

        while not rosppy.is_shutdown():
            k = keyin()

            if k == 'w':
                data.linear.x = 0.2
            else:
                data.linear.x = 0.0

            self.cmd_vel.publish(data)
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('keyboard_test1')
    rospy.wait_for_service('/motor_on')
    rospy.wait_for_service('/motor_off')
    rospy.on_shutdown(rospy.ServiceProxy('/motor_off',Trigger).call)
    rospy.ServiceProxy('/motor_on',Trigger).call()
    KeyRun().run()

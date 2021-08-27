#!/usr/bin/env python
#encoding: utf8

import sys, termios, rospy
from pimouse_keyboard_run.msg import key_val

def Publish_key(str):
    pub = rospy.Publisher('keyboard_value', key_val, queue_size=1)
    r = rospy.Rate(10)

    while not rospy.is_shutdown():
        if str != None:
            rospy.loginfo(str)
            pub.publish(str)
        r.sleep()

def Key_Input():
    fd = sys.stdin.fileno()

    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)

    new[3] &= ~termios.ICANON
    new[3] &= ~termios.ECHO

    try:
        termios.tcsetattr(fd, termios.TCSANOW, new)
        str = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old)

    return str


if __name__ == '__main__':
    rospy.init_node('keyboard_input1')
    try:
        Publish_key(Key_Input())
    except rospy.ROSInterruptException: pass

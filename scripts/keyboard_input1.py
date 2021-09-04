#!/usr/bin/env python
#encoding: utf8

import sys, rospy, termios
from pimouse_keyboard_run.msg import key_val

if __name__ == '__main__':
    pub = rospy.Publisher('keyboard_value', key_val, queue_size=1)
    rospy.init_node('keyboard_input2')
    r = rospy.Rate(5)
    
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)

    new[3] &= ~termios.ICANON
    new[3] &= ~termios.ECHO

    while not rospy.is_shutdown():
        try:
            termios.tcsetattr(fd, termios.TCSANOW, new)
            str = sys.stdin.read(1)
            if str != None:
                rospy.loginfo(str)
                pub.publish(str)

        except rospy.ROSInterruptException: pass

        finally:
            termios.tcsetattr(fd, termios.TCSANOW, old)

        r.sleep()

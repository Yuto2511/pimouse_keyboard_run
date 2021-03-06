#!/usr/bin/env python
#encoding: utf8

import rospy
from pimouse_keyboard_run.msg import key_val

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.key)
    print(data.key)

def listener():
    rospy.init_node('keyboard_read1')
    rospy.Subscriber("keyboard_value", key_val, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

#!/usr/bin/env python
#encoding: utf8

import rospy
from pimouse_keyboard_run.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)

def listener():
    rospy.init_node('test_sub', anonymous=True)

    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
